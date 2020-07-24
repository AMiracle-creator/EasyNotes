from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import TaskForm
from django.contrib import messages
from .models import User
from rest_framework.authtoken.models import Token
import jwt


# Create your views here.
def index(request):
    isuser = request.session.get('isuser', '0')

    if isuser == '0':
        return render(request, "login/index.html")
    else:
        return HttpResponseRedirect(reverse('notes:board'))


def sign_up(request):
    if request.method == 'POST':
        t = request.POST
        if User.objects.filter(user_email=t['email']).exists():
            messages.info(request, "email is exist, please change email")
            return render(request, 'login/register.html')
        else:
            encoded = str(jwt.encode({'email': t['email'], 'passw': t['pass']}, 'secret', algorithm='HS256'))
            user = User.objects.create(user_name=t['name'], user_email=t['email'], user_pass=t['pass'],
                                       user_token=encoded)
            user.save()
            request.session['isuser'] = str(encoded)
            return HttpResponseRedirect(reverse('notes:board'))
    else:
        return render(request, 'login/register.html')


def create(request):
    isuser = request.session.get('isuser', '0')
    if isuser == '0':
        return render(request, "login/index.html")
    else:
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                user = User.objects.get(user_token=isuser)
                t = form.data
                user.noteboard_set.create(note_title=t.get('note_title'),
                                          note_text=t.get('note_title'),
                                          note_tags=t.get('note_tags'))
                user.save()
        form = TaskForm()
        context = {'form': form}
        return render(request, 'board/create.html', context)


def board(request):
    isuser = request.session.get('isuser', '0')
    if isuser == '0':
        return HttpResponseRedirect(reverse('notes:index'))
    user = User.objects.get(user_token=isuser)
    boards = user.noteboard_set.order_by('-id')
    return render(request, 'board/index.html', {'user': user, 'note': boards})


def about(request):
    isuser = request.session.get('isuser', '0')
    if isuser == '0':
        return render(request, "login/index.html")
    user = User.objects.get(user_token=isuser)

    return render(request, 'board/about.html', {'user': user})


def settings(request):
    return render(request, 'board/settings.html')


def sign_in(request):
    mail = str(request.POST['email'])
    passw = str(request.POST['pass'])

    user = User.objects.get(user_email=mail, user_pass=passw)
    encoded = str(jwt.encode({'email': mail, 'passw': passw}, 'secret', algorithm='HS256'))
    user.user_token = encoded
    user.save()

    request.session['isuser'] = str(encoded)
    return HttpResponseRedirect(reverse('notes:board'))


def logout(request):
    request.session['isuser'] = '0'
    return HttpResponseRedirect(reverse('notes:index'))
