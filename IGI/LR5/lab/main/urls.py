from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import ProfileView
from . import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('news', views.news, name='news'),
    path('contact', views.contacts),    
    path('reviews', views.reviews, name='reviews'),
    path('create_reviews', views.create_reviews),    
    path('animals', views.animals),
    path('sales', views.sales),
    path('bySale', views.BySale),
    path('create_news', views.create_news),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('news/<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'), 
    path('admin_dashboard', views.admin_dashboard),
    path('stats', views.stats),
    path('vacation', views.Vacation),
    path('qaa', views.Qaa)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)