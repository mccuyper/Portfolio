
from django.urls import path
from . import views
from .views import BlogView, BlogDetailView


urlpatterns = [
      path('', views.home, name='home'),
      path('about/', views.about, name='about'),
      path('blog/', BlogView.as_view(), name='blog'),
      path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
      # path('blog/', views.blog, name='blog'),
      path('contact/', views.contact, name='contact'),
      path('send_email/', views.sendmail, name='send_email'),
      path('portfolio/', views.portfolio, name='portfolio'),
]
