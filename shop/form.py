from django.contrib.auth.forms import UserCreationForm
from django import forms

from shop.models import Customer

GENDER_CHOICES = (('M', 'Nam'), ('F', 'Nữ'))


class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(required=True, max_length=30, label=("Số điện thoại"))
    full_name = forms.CharField(required=True, label=("Họ tên"))
    username = forms.CharField(required=True, label=("Tên đăng nhập"))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(), label=("Giới tính"))
    password1 = forms.CharField(widget=forms.PasswordInput, label=("Mật khẩu"))
    password2 = forms.CharField(widget=forms.PasswordInput, label=("Nhập lại mật khẩu"))
    email = forms.EmailField(widget=forms.EmailInput, label=("E-mail"))
    address = forms.CharField(required=False, label=("Địa chỉ"))

    class Meta:
        model = Customer
        fields = ('full_name', 'email', 'gender', 'phone_number', 'address','username', 'password1', 'password2',)