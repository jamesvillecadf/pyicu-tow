from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout

def signin( request):
    userName = request.POST.get('username')
    passWord = request.POST.get('password') 

    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request, user)
                request.session['usertype'] = 'mgr'

                return JsonResponse({'ret': 0})
            else:
                return JsonResponse({'ret': 1, 'msg': 'Please log in with an administrator account'})
        else:
            return JsonResponse({'ret': 0, 'msg': 'User has been disabled'})
        
    else:
        return JsonResponse({'ret': 1, 'msg': 'Username or password is incorrect'})


def signout( request):
    logout(request)
    return JsonResponse({'ret': 0})
