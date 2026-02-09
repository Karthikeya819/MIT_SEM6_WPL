from django.shortcuts import render
import random

def index(request):
    context = {}

    captcha = random.randint(1000, 9999)
    context['captcha'] = captcha

    if request.method == "POST":
        try:
            user_input = int(request.POST.get('inp_captcha'))
            hidden_captcha = int(request.POST.get('captcha_hidden'))

            if user_input == hidden_captcha:
                context['result'] = "Captcha verified"
            else:
                context['result'] = "Wrong captcha"
            
        except (ValueError, TypeError) as e:
            context['result'] = e

    return render(request, 'captcha.html', context)
