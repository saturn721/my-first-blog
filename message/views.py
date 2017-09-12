from django.shortcuts import render
from django.http import HttpResponse
from .models import Ordering
from .forms import OrderingForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
import urllib
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
         
        if not form['author']:
            errors.append('Заполните имя')
        if '@' not in form['email']:
            errors.append('Введите корректный e-mail')
        if not form['message']:
            errors.append('Введите сообщение')
             
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
                Ordering.objects.create(author=form['author'], email=form['email'], title=form['title'], text=form['message']).send
                form = {}
                return render(request, 'message/message.html', {'errors': errors, 'form':form})
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

         
    return render(request, 'message/message.html', {'errors': errors, 'form':form})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})