from django.shortcuts import render, redirect
from .models import News, Reviews, Animal, Staf, Sales, Profile, QaA, Vacationss
from .forms import *
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_http_methods
from django.http import Http404, JsonResponse
import requests, datetime ,calendar
from dateutil.relativedelta import relativedelta
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
import statistics
import base64
from io import BytesIO
matplotlib.use('Agg')


def Vacation(request):
    Vacations = Vacationss.objects.all()

    return render(request, 'vacation.html' ,{'Vacations': Vacations})



def Qaa(request):
    Qaas = QaA.objects.all()

    return render(request, 'qaa.html' ,{'Qaas': Qaas})


def stats(request):
    if request.user.is_staff:
        birth_dates = list(Staf.objects.values_list('birth_date', flat=True))
        ages = [relativedelta(datetime.now(), bd).years for bd in birth_dates]
        average_age = sum(ages) / len(ages) if ages else 0
        median_age = statistics.median(ages) if ages else 0

        plt.figure(figsize=(8, 4))
        plt.bar(range(1, len(ages)+1), ages, color='skyblue')
        plt.axhline(average_age, color='red', linestyle='--', label=f'Avarage: {average_age:.2f}')
        plt.axhline(median_age, color='green', linestyle=':', label=f'Median: {median_age}')
        plt.xlabel('Users')
        plt.ylabel('Age')
        plt.title('Users age')
        plt.legend()

        buffer = BytesIO()
        plt.tight_layout()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        age_chart = base64.b64encode(buffer.read()).decode('utf-8')
        buffer.close()
        plt.close()

        age_context = {
            'average_age': average_age,
            'median_age': median_age,
            'chart': age_chart,
        }

        return render(request, 'stats.html', {
            'age_context': age_context,
        })

    return redirect('main')
    


def BySale(request):
    sales = Sales.objects.all()

    return render(request, 'bySale.html', {'sales' : sales})


def home(request):

    news = News.objects.all()
    cal = calendar.TextCalendar()    
    
    return render(request, 'home.html', {'news': news.last, 'cal': cal.formatmonth(2025, 5)})


def admin_dashboard(request):
    
    animal = Animal.objects.all()    
    staf = Staf.objects.all()

    return render(request, 'admin_dashboard.html', {'animal':animal, 'staf':staf})


def about(request):

    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    
    joke = ""
    if response.status_code == 200:
        data = response.json()
        joke = data.get("joke", "No joke found.")
    else:
        joke = "Failed to get a joke."

    response = requests.get("https://favqs.com/api/qotd")
    quote = None

    if response.status_code == 200:
        data = response.json()
        quote = data['quote']['body']
    
    return render(request, 'about.html', {
        'joke': joke,
        'quote' : quote,
    })


def news(request):
    news = News.objects.all() 
    return render(request, 'news.html', {'news': news})


def contacts(request):
    staf = Staf.objects.all()
    return render(request, 'contacts.html', {'staf': staf})


def animals(request):
    animal = Animal.objects.all()
    return render(request, 'animals.html', {'animal': animal})


class NewsDetailView(DetailView):
    model = News
    template_name = 'details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'update_view.html'

    fields = ['title', 'anons', 'full_text', 'image']


class NewsDeleteView(DeleteView):
    model = News
    success_url = '/news'
    template_name = 'delete_view.html' 


def create_news(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Форма заполнена некорректно'

    form = NewsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'create_news.html', data)


def reviews(request):
    reviews = Reviews.objects.all() 
 
    return render(request, 'reviews.html', {'reviews': reviews})


def create_reviews(request):
    error = ''
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
        else:
            error = 'Форма заполнена некорректно'

    form = ReviewForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'create_reviews.html', data)


def sales(request):
    sales = Sales.objects.all()
    return render(request, 'sales.html', {'sales': sales})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            birthdate = form.cleaned_data['age']
            age = relativedelta(datetime.now(), birthdate).years
            if age < 18 :
                error = 'Форма заполнена некорректно'
                return redirect('register')
            form.save()
            return redirect('login')  
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})


class ProfileView(LoginRequiredMixin, DetailView):
    model = Staf
    template_name = 'profile.html'
    context_object_name = 'staf'

    def get_object(self):
        return self.request.user.staf 