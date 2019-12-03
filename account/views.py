from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from account.forms import RegistrasiForm
# Create your views here.

def registrasi_view(request):
    context = {}
    if request.POST:
        form = RegistrasiForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registrasi_form'] = form
    else:
        form =RegistrasiForm()
        context['registrasi_form'] = form
    return render(request, 'account/register.html',context)


def logout_view(request):
    logout(request)
    return redirect('home')
