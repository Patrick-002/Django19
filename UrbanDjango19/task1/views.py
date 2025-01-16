from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserRegister
from .models import *


class Platform(TemplateView):
    template_name = 'fourth_task/platform.html'


class Games(TemplateView):
    template_name = 'fourth_task/games.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        games = Game.objects.all()
        # titles_list = []
        # for game in games:
        #     titles_list.append(game.title)

        context['games'] = games

        return context



class Cart(TemplateView):
    template_name = 'fourth_task/cart.html'


def sign_up_by_django(request):
    info = {}
    users = Buyer.objects.all()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = "Пароли не совпадают"
                info['form'] = UserRegister()
                return render(request, 'fourth_task/registration_page.html', info)
            if int(age) < 18:
                info['error'] = "Вы должны быть старше 18"
                info['form'] = UserRegister()
                return render(request, 'fourth_task/registration_page.html', info)
            for buyer in users:
                if username == buyer.name:
                    info['error'] = "Пользователь уже существует"
                    info['form'] = UserRegister()
                    return render(request, 'fourth_task/registration_page.html', info)

            info['form'] = form
            info['message'] = f'Приветствуем, {username}!'

            Buyer.objects.create(name = username, balance = 0, age = age)
    else:
        info['form'] = UserRegister()
    return render(request, 'fourth_task/registration_page.html', info)


def sign_up_by_html(request):
    info = {'custom_form': True}
    users = Buyer.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if username and password and repeat_password and age:
            if password != repeat_password:
                info['error'] = "Пароли не совпадают"
                return render(request, 'fourth_task/registration_page.html', info)
            if int(age) < 18:
                info['error'] = "Вы должны быть старше 18"
                return render(request, 'fourth_task/registration_page.html', info)
            for buyer in users:
                if username == buyer.name:
                    info['error'] = "Пользователь уже существует"
                    return render(request, 'fourth_task/registration_page.html', info)
        else:
            return render(request, 'fourth_task/registration_page.html', info)

        Buyer.objects.create(name=username, balance=0, age=age)
        info['message'] = f'Приветствуем, {username}!'
    return render(request, 'fourth_task/registration_page.html', info)


def news(request):
    return render(request, 'fourth_task/news.html')
