from django.shortcuts import render,redirect
from.forms import LoginFrom
from.models import Vendor,Driver
from post.models import posts
from django.contrib.auth import logout
from users.decorators import driver_required,vendor_required
import qrcode
from io import BytesIO
import base64





def login(request):
    if request.method == 'POST':
        form = LoginFrom(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password'] 

            driver = Driver.objects.filter(phone_number=phone_number, password=password).first()
            vendor = Vendor.objects.filter(phone_number=phone_number, password=password).first()

            if driver:
                request.session['user_type'] = 'driver'
                request.session['driver_id'] = driver.id
                return redirect('users:driver_profile')
            elif vendor:
                request.session['user_type'] = 'vendor'
                request.session['vendor_id'] = vendor.id
                return redirect('users:vendor_profile')
            else:
                error_message = 'المستخدم غير موجود أو البيانات غير صحيحة'
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginFrom()

    return render(request, 'login.html', {'form': form})





def logout_view(request):
    logout(request)
    return redirect('baly:home')







@driver_required     
def drivers(request):
    user_type = request.session.get('user_type')
    driver_id = request.session.get('driver_id')

    if user_type == 'driver':
        context={
            'driver': Driver.objects.get(id=driver_id),
            'last_four_vender':Vendor.objects.all().order_by('-id')[:4],
            'logo':posts.objects.filter(type='logo'),
            'three_posts':posts.objects.filter(type='post').order_by('-id')[:3],
            'video':posts.objects.filter(type='video').order_by('-id')[:3],
            'competition':posts.objects.filter(type='competition').order_by('-id')[:1]
        }
        return render(request, 'driver_profile.html', context=context)
    else:
        return redirect('login')



@driver_required
def qr_code(request):
    user_type = request.session.get('user_type')
    driver_id = request.session.get('driver_id')
    if user_type == 'driver' and driver_id:
        driver = Driver.objects.get(id=driver_id)
        
        # تحديث الرابط ليشمل driver_id
        qr_url = f"http://127.0.0.1:8000/discount/{driver.user_id}"

        # إنشاء QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # تحويل الصورة إلى بيانات base64
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        qr_image_base64 = base64.b64encode(buffer.getvalue()).decode()

        # تمرير البيانات إلى القالب
        context = {
            'qr_code': qr_image_base64
        }
        return render(request, 'qr_code.html', context)
    else:
        return redirect('users:login')
    
    
    
    
    
@driver_required    
def all_vendors(request):
    context={
        'all_vendors':Vendor.objects.all().order_by('-id')
    }
    return render(request,'all_vendors.html',context=context)




def vendor_profile(request):
    user_type=request.session.get('user_type')
    vendor_id = request.session.get('vendor_id')
    if user_type=='vendor':
        vendor=Vendor.objects.get(id=vendor_id)
        context={
            'vendor':vendor
        }
        return render(request,'vendor_profile.html',context=context)




def Terms_and_conditions(request,pk):
    vendor=Vendor.objects.get(id=pk)
    context={
        'vendor':vendor
    }
    return render(request,'Terms_and_conditions.html',context=context)


def offer_vendor(request,user_id):
    vendor=Vendor.objects.get(user_id=user_id)
    context={
        'vendor':vendor
    }
    return render(request,'offer.html',context=context)