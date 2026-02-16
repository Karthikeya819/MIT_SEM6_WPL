from django.shortcuts import render
import base64
# Create your views here.
state_dict = {}

def Q1(request):

    if request.method == 'POST':
        try:
            a = state_dict['a'] = float(request.POST.get('a'))
            b = state_dict['b'] = float(request.POST.get('b'))
            opr = state_dict['opr'] = request.POST.get('opr')

            if opr == '0':
                state_dict['ans'] = a+b
            elif opr == '1':
                state_dict['ans'] = a-b
            elif opr == '2':
                state_dict['ans'] = a*b
            elif opr == '3':
                state_dict['ans'] = a/b

        except Exception:
            pass
    return render(request, 'q1.html', state_dict)

def Q2(request):
    if request.method == 'POST':
        try:
            context = {}
            context['title'] = request.POST.get('title')
            context['subtitle'] = request.POST.get('subtitle')
            context['background_color'] = request.POST.get('bgcolor')
            context['font_color'] = request.POST.get('fontcolor')
            context['font_siz'] = request.POST.get('fontsize')
            image_data = None
            if request.FILES.get('image'):
                image = request.FILES['image']
                image_bytes = image.read()
                image_data = f'data:image/png;base64,{base64.b64encode(image_bytes).decode("utf-8")}'

            context['image'] = image_data

            return render(request, 'cover.html', context)
        except Exception:
            pass

def home(request):
    return render(request, 'q3/home.html')

def metadata(request):
    return render(request, 'q3/metadata.html')

def reviews(request):
    return render(request, 'q3/reviews.html')

def publisher(request):
    return render(request, 'q3/publisher.html')

from django.shortcuts import render, redirect

def A1(request):
    context = {}

    if request.method == "POST":
        context['name'] = request.POST.get("name", "")
        context['message'] = request.POST.get("message", "")
        context['styles'] = request.POST.getlist("style")
        context['color'] = request.POST.get("color", "black")

        context['text'] = f"Name: {context['name']} | Message: {context['message']}"

    return render(request, "a1.html", context)



