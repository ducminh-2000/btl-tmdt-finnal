from django.shortcuts import redirect, render

from shop.form import SignUpForm
from shop.models import *


# ------------------------------- CUSTOMER -----------------------------------


def signup(request):
    try:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                customer = Customer()
                user = User()
                customer.full_name = form.cleaned_data['full_name']
                customer.phone_number = form.cleaned_data['phone_number']
                customer.gender = form.cleaned_data['gender']
                customer.address = form.cleaned_data['address']
                user.email = form.cleaned_data['email']
                user.username = form.cleaned_data["username"]
                raw_password = form.cleaned_data['password1']
                user.set_password(raw_password)
                customer.user = user
                user.save()
                customer.save()

                return redirect('login')
        else:
            form = SignUpForm()

        return render(request, 'customer/signup.html', {'form': form})
    except Exception:
        form = SignUpForm()

        return render(request, 'customer/signup.html', {'form': form})



