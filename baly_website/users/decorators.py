from django.shortcuts import redirect

def driver_required(view_func):
    def wrapper(request, *args, **kwargs):
        user_type = request.session.get('user_type')
        
        if user_type != 'driver' :
            return redirect('users:login')
        
        return view_func(request, *args, **kwargs)
    
    return wrapper





def vendor_required(view_func):
    def wrapper(request, *args, **kwargs):
        user_type = request.session.get('user_type')
        
        if user_type != 'vendor' :
            return redirect('users:login')
        
        return view_func(request, *args, **kwargs)
    
    return wrapper