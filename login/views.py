from django.shortcuts import render


def index(request):
    return render(request, 'signup/signup_page.html')

def congrats(request):
    return render("Congrats, you have just signed up!")
