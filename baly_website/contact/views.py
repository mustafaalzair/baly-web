from django.shortcuts import render,redirect
from users.models import Vendor
from .forms import Formcontact
# Create your views here.



def contact(request):
    user_type = request.session.get('user_type')
    vendor_id = request.session.get('vendor_id')

    if user_type != 'vendor' or vendor_id is None:
        return redirect('some_error_page')
    vendor = Vendor.objects.get(id=vendor_id)
    if request.method == 'POST':
        form = Formcontact(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:vendor_profile")
    else:
        form = Formcontact()

    context = {
        'vendor': vendor,
        'form': form  # تقديم النموذج في السياق
    }
    return render(request, 'contact.html', context=context)
