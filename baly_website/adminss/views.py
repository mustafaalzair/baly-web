from discount.models import *
from users.models import Vendor,Driver
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import *
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from django.db.models import Count
from django.http import JsonResponse
import json
from contact.models import Contact
from django.urls import reverse
import openpyxl


# Create your views here.


@login_required(login_url='login_admin')
def discount_table(request):
    context={
        'discount':Discounts.objects.all().order_by('-id')
    }
    return render(request,'discount_table.html',context=context)


@login_required(login_url='login_admin')
def drivers(request):
    context={
        'Driver':Driver.objects.all().order_by('-id')
    }
    return render(request,'drivers.html',context=context)
    
    
def login_view(request):
    if request.method=='POST':
        form=CustomLoginForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('admins:admin_dashboard')
        else:
                error_message = 'المستخدم غير موجود أو البيانات غير صحيحة'
                return render(request, 'login_admin.html', {'form': form, 'error_message': error_message})
    else:
        form =CustomLoginForm()
        return render(request, 'login_admin.html', {'form': form})


@login_required(login_url='login_admin')
def register_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = form.cleaned_data.get('is_staff')
            user.is_superuser = form.cleaned_data.get('is_superuser')
            user.save()
            return redirect('login-url')
    else:
        form = CustomRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required(login_url='admins:login_admin')
def admin_dashboard(request):
  
    today = timezone.now().date()

    # احصل على الفترة الزمنية من طلب GET (أو استخدم اليوم كافتراضي)
    time_period = request.GET.get('period', 'Today')

    # حساب الفترة الزمنية استنادًا إلى الاختيار
    if time_period == 'last7days':
        start_date = today - timedelta(days=7)
        end_date = today + timedelta(days=1)  # يوم بعد اليوم الحالي لتضمين اليوم كاملًا
    elif time_period == 'Today':
        start_date = today
        end_date = today + timedelta(days=1)  # يوم بعد اليوم الحالي لتضمين اليوم كاملًا
    elif time_period == 'lastday':
        start_date = today - timedelta(days=1)
        end_date = today - timedelta(days=1)
    elif time_period == 'Last Month':
        start_date = today - relativedelta(months=1)
        end_date = today
    elif time_period == 'Last Year':
        start_date = today - relativedelta(years=1)
        end_date = today
    # استخدم start_date و end_date لتصفية السجلات
    visits = Discounts.objects.filter(created_at__range=(start_date, end_date)).count()
    total_visits=Discounts.objects.count()
    active_vendor = discount_given.objects.filter(created_at__range=(start_date, end_date)).values('vendor_name').distinct().count()
    discounts = discount_given.objects.filter(created_at__range=(start_date, end_date)).count()
    top_vendors = Discounts.objects.filter().values('vendor_name').annotate(count=Count('vendor_name')).order_by('-count')[:5]
    vendors_by_city = Vendor.objects.filter().values('city').annotate(count=Count('city')).order_by('-count')
    vendors_category = Vendor.objects.filter().values('Sub_Category').annotate(count=Count('Sub_Category')).order_by('-count')
    total_vendors = Vendor.objects.count()
    start_of_month = today -timedelta(days=30)
    new_vendors=Vendor.objects.filter(created_at__range=(start_of_month, end_date)).count()
    contact=Contact.objects.all().order_by('-id')
    #weeklyOverviewChart
    start_of_week = today -timedelta(days=6)
    weekly_discounts = Discounts.objects.filter(created_at__range=[start_of_week, today])
    chart_data = {
        'dates': [(start_of_week + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)],
        'values': [0] * 7
    }
    for discount in weekly_discounts:
        day_index = (discount.created_at - start_of_week).days
        chart_data['values'][day_index] += 1
    #-----------------------------------------------------------
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # ترجيع البيانات كـ JSON
        return JsonResponse({
            'active_vendor': active_vendor,
            'visits': visits,
            'discounts':discounts,
           
            # تأكد من تحويل البيانات إلى تنسيق مناسب إذا لزم الأمر
        })
    context = {
        'total_visits':total_visits,
        'top_5_vendors': top_vendors,
        'chart_data': json.dumps(chart_data),
        'vendor_city':vendors_by_city,
        'total_vendors':total_vendors,
        'vendors_category':vendors_category,
        'new_vendors':new_vendors,
        'contact':contact,
      
        
    }

    # تقديم القالب مع السياق
    return render(request, 'admin_dashboard.html', context=context)


@login_required(login_url='login_admin')
def delete_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    driver.delete()
    return redirect(reverse('admins:drivers')) 



 
@login_required(login_url='login_admin')
def delete_vendor(request,vendor_id):
    vendor=get_object_or_404(Vendor,id=vendor_id)
    vendor.delete()
    return redirect(reverse('admins:all_vendor'))




@login_required(login_url='login_admin')
def add_deiver(request):
    if request.method=="POST":
        excel_file=request.FILES['excel_file']
        
        wb=openpyxl.load_workbook(excel_file)
        sheet=wb.active
        
        
        for row in sheet.iter_rows(min_row=2):
            full_name=row[0].value
            rating=row[1].value
            password=row[2].value
            car=row[3].value
            color_car=row[4].value
            plate_number=row[5].value
            phone_number=row[6].value
            
            Driver.objects.create(
                full_name=full_name,rating=rating,password=password,car=car,color_car=color_car,plate_number=plate_number,phone_number=phone_number
                )
        return redirect('admins:drivers')
        
    
    return render(request,'add_deiver.html')



@login_required(login_url='login_admin')
def delete_all_driver(request):
    Driver.objects.all().delete()
    return redirect('admins:drivers')



@login_required(login_url='login_admin')
def all_vendor(request):
    vendor=Vendor.objects.all()
    context={
        'vendor':vendor
    }
    return render(request,'all_vendor.html',context=context)


@login_required(login_url='login_admin')
def add_vendor(request):
    if request.method == 'POST':
        form = Add_vendor(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admins:all_vendor')
    else:
        form = Add_vendor()
    return render(request, 'add_vendor.html', {'form': form})

    