from django.shortcuts import render, redirect

# Create your views here.

def Q1(request):
    manufacturers = ['Toyota', 'Ford', 'Tesla', 'BMW', 'Honda']
    return render(request, 'q1/home.html', {'manufacturers': manufacturers})

def result(request):
    manufacturer = request.POST.get('manufacturer')
    model_name = request.POST.get('model_name')
    
    context = {
        'manufacturer': manufacturer,
        'model_name': model_name,
    }
    return render(request, 'q1/result.html', context)

def first_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        subject = request.POST.get('subject')

        request.session['user_data'] = {
            'name': name,
            'roll': roll,
            'subject': subject
        }
        return redirect('second_page')

    subjects = ['Mathematics', 'Physics', 'Chemistry', 'Social']
    return render(request, 'q2/firstPage.html', {'subjects': subjects})

def second_page(request):
    data = request.session.get('user_data', {})
    return render(request, 'q2/secondPage.html', {'data': data})