from django.shortcuts import render
from django.http import HttpResponse
from .models import Ordering
from .forms import OrderingForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
import urllib.request 
#import urllib
#import urllib2
import json
from django.conf import settings
from django.contrib import messages

#from .models import Comment
#from .forms import CommentForm
# Create your views here.


def message(request):
    errors = []
    form = {}
    if request.POST:

        form['author'] = request.POST.get('author')
        form['email'] = request.POST.get('email')
        form['title'] = request.POST.get('title')
        form['message'] = request.POST.get('message')
        form['age'] = request.POST.get('age')
        form['eye_color'] = request.POST.get('eye_color')
        form['rice'] = request.POST.get('rice')
        form['boobs'] = request.POST.get('boobs')
        form['waist'] = request.POST.get('waist')
        form['hair_color'] = request.POST.get('hair_color')
        form['taz'] = request.POST.get('taz')
        form['foot'] = request.POST.get('foot')

        if not form['author']:
            errors.append('Заполните имя')
        if '@' not in form['email']:
            errors.append('Введите корректный e-mail')
        if not form['message']:
            errors.append('Введите сообщение')
        if not form['age']:
            errors.append('chose age')

        if not errors:
            # ... сохранение данных в базу
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.RECAPTCHA_PRIVATE_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''
            if result['success']:
                Ordering.objects.create(author=form['author'], email=form['email'], title=form['title'],\
                 message=form['message'], age=form['age'], eye_color=form['eye_color'], rice=form['rice'], \
                 boobs=form['boobs'], waist=form['waist'], hair_color=form['hair_color'], taz=form['taz'], foot=form['foot']).send
                messages.success(request, 'Сообщение отправлено!')
                messages.success(request, ' Message send!')

                form = {}
                #return render(request, 'message/message.html', {'errors': errors, 'form':form})
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')


    return render(request, 'message/request.html', {'errors': errors, 'form':form})


def list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'message/en/index.html', {'posts': posts})


def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})
