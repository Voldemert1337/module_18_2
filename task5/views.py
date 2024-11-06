from django.shortcuts import render
from .forms import UserRegistrationForm
from django.http import HttpResponse
# Create your views here.
users = ['Max', 'user', 'Roza', 'Alex']


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        age = int(request.POST.get('age'))
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')


        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            return HttpResponse(f"Приветствуем, {username}!")
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            age = int(form.cleaned_data['age'])
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                return HttpResponse(f"Приветствуем, {username}!")
        else:
            info['form'] = form
    else: form = UserRegistrationForm()
    return render(request, 'fifth_task/registration_page.html', info)



