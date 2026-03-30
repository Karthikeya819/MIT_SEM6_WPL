from django.shortcuts import render, redirect
from .forms import BookForm, ProductForm
from .models import Book, Product, Human

def manage_book(request, book_id=None):
    instance = Book.objects.get(pk=book_id) if book_id else None
    
    if request.method == "POST":
        form = BookForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=instance)

    return render(request, 'book_form.html', {'form': form})

def book_list(request):
    books = Book.objects.all().prefetch_related('authors').select_related('publisher')
    return render(request, 'book_list.html', {'books': books})

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_index')
    else:
        form = ProductForm()
    return render(request, 'create_project.html', {'form': form})

def product_index(request):
    products = Product.objects.all()
    return render(request, 'product_home.html', {'products': products})

def human_management(request):
    selected_human = None
    all_humans = Human.objects.all()

    human_id = request.GET.get('human_id')
    if human_id:
        selected_human = Human.objects.filter(id=human_id).first()

    if request.method == "POST":
        current_id = request.POST.get('current_id')
        human = Human.objects.get(id=current_id)

        if 'update' in request.POST:
            human.first_name = request.POST.get('first_name')
            human.last_name = request.POST.get('last_name')
            human.phone = request.POST.get('phone')
            human.address = request.POST.get('address')
            human.city = request.POST.get('city')
            human.save()
            return redirect('human_page')

        elif 'delete' in request.POST:
            human.delete()
            return redirect('human_page')

    return render(request, 'human_page.html', {
        'all_humans': all_humans,
        'selected_human': selected_human
    })