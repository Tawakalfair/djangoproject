from django.shortcuts import render
from account.models import Account
# Create your views here.

def homeView(request):
    Akun = Account.objects.all()
    context = {
        "account" : Akun
    }
    return render(request, 'personal/home.html', context)