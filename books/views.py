# Create your views here.
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import Book, Section

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')  # Redirect to the dashboard page after login
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    books = Book.objects.all()  # Retrieve all Book objects
    return render(request, 'dashboard.html', {'books': books})

def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        book = Book.objects.create(title=title, author=request.user)
        return redirect('dashboard')
    return render(request, 'create_book.html')

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    sections = Section.objects.filter(book=book)
    return render(request, 'book_detail.html', {'book': book, 'sections': sections})

def edit_section(request, section_id):
    section = Section.objects.get(pk=section_id)
    if request.method == 'POST':
        section.content = request.POST['content']
        section.save()
        return redirect('edit_section', book_id=section.book.id)
    return render(request, 'edit_section.html', {'section': section})
