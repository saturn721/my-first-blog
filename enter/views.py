from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Entering
from .forms import EnteringForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
import urllib.request
import json
from django.conf import settings
from django.contrib import messages

def enter(request):
    form ={}
    if request.POST: #capcha monero
        form['token'] = request.POST.get('token') #take token from hidden input form
        token = form['token']
        print(token)
<<<<<<< Updated upstream
        enter_date = {'secret': '', 'token': token, 'hashes': 256}
=======
        enter_date = {'secret': 'fe6ri5jt15bDX5PqfZjaOsdfOLXv0wk6', 'token': token, 'hashes': 256}
>>>>>>> Stashed changes
        data = urllib.parse.urlencode(enter_date).encode()
        req = urllib.request.Request('https://api.coinhive.com/token/verify', data = data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        if result['success'] == True:
            Entering.objects.create(token=form['token'],).send
            print(result)
            return render(request, 'message/en/index.html')
        else:
            print(result)
            return render(request, 'enter/enter.html')
    return render(request, 'enter/enter.html')


# Create your views here.
