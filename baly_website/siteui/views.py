from django.shortcuts import render,redirect
from users.models import Vendor,Driver
from post.models import posts
from users.decorators import driver_required
from django.shortcuts import get_object_or_404






def home(request):
    #If the user is a driver, he cannot access this page 
    user_type = request.session.get('user_type')
 
    if user_type == 'driver':
        return redirect('users:driver_profile')
    context={
        'user':Vendor.objects.all(),
        'user_last':Vendor.objects.all().order_by('-id')[:3],
        'three_posts':posts.objects.filter(type='post').order_by('-id')[:3],
        'logo':posts.objects.filter(type='logo'),
        'competition':posts.objects.filter(type='competition').order_by('-id')[:1],
        'video':posts.objects.filter(type='video').order_by('-id')[:3]
        
    }
    
    return render(request, 'home.html', context=context)


@driver_required
def show(request,pk):
    
        context={
            'vendor':Vendor.objects.get(pk=pk),
            'last_four_vendor':Vendor.objects.all()[:3],
            'logo':posts.objects.filter(type='logo')[:1]
        }
        return render(request,'show.html',context=context)



def showpost(request,pk):
        context_post={
            
            'posts':posts.objects.get(pk=pk),
            'last_four_posts':posts.objects.exclude(type ='logo').order_by('-id')[:3] ,
            'logo':posts.objects.filter(type='logo')[:1] ,   
        }
        return render(request,'show_post.html',context=context_post)
    
    
    
    
  

                 


