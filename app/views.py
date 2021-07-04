from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import MyPersonalData, Blog, Portfolio
from .forms import ContactMe

from django.http import HttpResponse, request
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def home(request):
    return render(request, 'home.html')


def about(request):
    data = MyPersonalData.objects.get(pk=1)
    return render(request, 'about.html', {"data": data})


def blog(request):
    posts = Blog.objects.all().order_by('-date')
    item_name = request.GET.get('item_name')

    if item_name != '' and item_name is not None:
        posts = posts.filter(title__icontains=item_name)
    return render(request, 'blog.html', {'posts': posts})


class BlogView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 6

    def get_queryset(self):
        item_name = self.request.GET.get('item_name', '')
        object_list = Blog.objects.filter(
            Q(title__icontains=item_name) |
            Q(content__icontains=item_name)
        )
        return object_list


class BlogDetailView(DetailView):
    model = Blog

def contact(request):
    form = ContactMe()
    return render(request, 'contact.html', {'form': form})


def portfolio(request):
    works = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'works': works})


def sendmail(request):
    if request.method == 'POST':
        template = render_to_string('email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'subject': request.POST['subject'],
            'message': request.POST['message'],

        })
        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['mccuyper@gmail.com']
        )
        email.fail_silently = False
        email.send()
    return HttpResponse('Email has been sent successfully!')
