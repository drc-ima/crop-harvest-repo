from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):

    context = {
        'form_data': {}
    }

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        print("something")
        form_data = request.POST

        context['form_data'] = form_data
        
        # if the password is not empty and the password is not the same as the confirm password
        if password and password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'user/new.html', context)
        
        # check if username already exist
        try:
            User.objects.get(username=username)
            messages.error(request, "User with this username already exist")
            return render(request, 'user/new.html', context)
        except User.DoesNotExist:
            pass
        
        add_user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        add_user.set_password(password)

        add_user.save()

        messages.success(request, 'Account registration was successful.')

        return redirect("login")

    return render(request, 'user/new.html', context)



def homepage(request):
    return render(request, 'user/homepage.html')

# read about python decorators
@login_required()
def dashboard(request):
    return render(request, 'user/dashboard.html')