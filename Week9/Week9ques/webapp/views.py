from django.shortcuts import render, redirect
from .forms import RegisterForm, VoteForm, CGPAForm, OrderForm, FeedbackForm

def q1(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']

            context = {
                'username': username,
                'email': email,
                'contact': contact
            }

            return render(request, "q1_success.html", context)
    else:
        form = RegisterForm()

    return render(request, "q1.html", {'form': form})

good = 0
satisfactory = 0
bad = 0

def q2(request):
    global good, satisfactory, bad

    good_per = sat_per = bad_per = 0
    active = False

    if request.method == "POST":
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.cleaned_data['vote']

            if vote == 'good':
                good += 1
            elif vote == 'satisfactory':
                satisfactory += 1
            elif vote == 'bad':
                bad += 1

            total = good + satisfactory + bad

            good_per = (good * 100) / total
            sat_per = (satisfactory * 100) / total
            bad_per = (bad * 100) / total
            active = True
    else:
        form = VoteForm()

    context = {
        'form': form,
        'good': good_per,
        'sat': sat_per,
        'bad': bad_per,
        'active': active,
    }

    return render(request, "q2.html", context)

def q3p1(request):
    if request.method == "POST":
        form = CGPAForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            marks = form.cleaned_data['marks']

            request.session['name'] = name
            request.session['marks'] = marks

            return redirect('Q3_Result')
    else:
        form = CGPAForm()

    return render(request, "q3p1.html", {'form': form})


def q3p2(request):
    name = request.session.get('name')
    marks = request.session.get('marks')

    cgpa = marks / 50

    context = {
        'name': name,
        'cgpa': cgpa
    }

    return render(request, "q3p2.html", context)

PRICE_LIST = {
    "Mobile": 10000,
    "Laptop": 50000
}

def a1(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            devices = form.cleaned_data['device']
            qty = form.cleaned_data['quantity']

            total = 0
            items = []

            for d in devices:
                price = PRICE_LIST[d] * qty
                total += price
                items.append({
                    "brand": brand,
                    "device": d,
                    "quantity": qty,
                    "amount": price
                })

            return render(request, "a1_bill_page.html", {
                "items": items,
                "total": total
            })
    else:
        form = OrderForm()

    return render(request, "a1.html", {"form": form})

def a2(request):
    message = ""

    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            course = form.cleaned_data['course']

            message = f"Thank you {name}. Your feedback for {course} has been submitted successfully."

    else:
        form = FeedbackForm()

    return render(request, "a2.html", {
        "form": form,
        "message": message
    })
