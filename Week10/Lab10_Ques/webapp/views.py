from django.shortcuts import render, redirect
from .models import Category, Page, Works, Lives, Institute
from .forms import CategoryForm, PageForm, WorksForm, CompanySearchForm

def index(request):
    categories = Category.objects.all()
    pages = Page.objects.all()
    return render(request, 'index.html', {
        'categories': categories,
        'pages': pages
    })


def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/webapp/')

    return render(request, 'add_category.html', {'form': form})


def add_page(request):
    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/webapp/')

    return render(request, 'add_page.html', {'form': form})


def add_work(request):
    form = WorksForm()
    message = ""

    if request.method == 'POST':
        form = WorksForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Data inserted successfully!"

    return render(request, 'add_work.html', {'form': form, 'message': message})

def search_company(request):
    form = CompanySearchForm()
    results = []

    if request.method == 'POST':
        form = CompanySearchForm(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company_name']
            works_people = Works.objects.filter(company_name=company)

            for work in works_people:
                try:
                    person = Lives.objects.get(person_name=work.person_name)
                    results.append({
                        'name': work.person_name,
                        'city': person.city
                    })
                except Lives.DoesNotExist:
                    results.append({
                        'name': work.person_name,
                        'city': "Not Found"
                    })

    return render(request, 'search_company.html', {
        'form': form,
        'results': results
    })

def institute_list(request):
    institutes = Institute.objects.all()
    return render(request, 'institutes.html', {'institutes': institutes})