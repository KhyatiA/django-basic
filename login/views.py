from django.shortcuts import render
from .models import Signup

def index(request):
    details=Signup.objects.all()
    context={'details':details}
    return render(request, 'signup/signup_page.html', context)

def congrats(request):
    return render("Congrats, you have just signed up!")
