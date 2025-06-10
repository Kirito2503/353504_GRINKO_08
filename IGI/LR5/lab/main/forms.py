from .models import News, Reviews, Animal, Sales, QaA, Vacationss
from django.forms import ModelForm
from .models import phone_regex
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django import forms


class QaaForm(ModelForm):
    class Meta:
        qaa = QaA
        fields = ['quation', 'answer']


class VacationForm(ModelForm):
    class Meta:
        vacation = Vacationss
        fields = ['name', 'title', 'money']


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'anons', 'full_text', 'image']


class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        mark = {mark: mark for mark in range(1, 6)}
        fields = ['review', 'mark']   

        widgets = {
            'text' : forms.Textarea,
            'mark': forms.Select(choices=mark),

        }        


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['species', 'number', 'house', 'image']


class SalesForm(ModelForm):
    class Meta:
        model = Sales  
        fields = ['title', 'sale', 'time']      


class RegisterForm(UserCreationForm):
    phone_number = forms.CharField(
        required=True,
        label="Номер телефона",
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+375 \(29\) \d{3}-\d{2}-\d{2}$',
                message="Формат: +375 (29) XXX-XX-XX"
            )
        ]
    )
    age = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Укажите дату рождения"
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        

    def save(self, commit=True):
        user = super().save(commit)
        age = self.cleaned_data.get('age')

        return user


class StafRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    phone_number = forms.CharField(
        max_length=19,
        validators=[phone_regex],
        help_text="Формат: +375 (29) XXX-XX-XX"
    )
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Укажите дату рождения"
    )
    animal = forms.CharField(
        help_text="Укажите вид животного"
    )
    image = forms.ImageField()

    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'password1', 
            'password2', 
            'phone_number', 
            'birth_date',
            'animal',
        ]        