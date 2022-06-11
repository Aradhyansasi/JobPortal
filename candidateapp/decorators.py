from django.shortcuts import redirect

def signin_required(fucn):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return fucn(request, *args, **kwargs)
        else:
            return redirect('signin')
    return wrapper