from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . forms import Register_form
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, Your account has been created')
            return redirect('login')
    else:
        form = Register_form()
    return render(request,'users/register.html', {'form':form})

@login_required
def profilepage(request):
    return render(request,'users/profile.html')