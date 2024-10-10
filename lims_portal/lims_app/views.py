from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from .models import*
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm,BookForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book


class CustomLoginView(LoginView):
    template_name = 'login.html'

def registerPage(request):
   if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('login')  
   else:
        form = RegistrationForm()
   return render(request, 'register.html', {'form': form})
def loginPage(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  # Redirect to home or another page
            else:
                messages.error(request, 'Invalid credentials')
                return render(request, 'login.html')
            
    else:
        return render(request, 'login.html')


def home(request):
    return render(request,"home.html",context={"current_tab": "home"})


def readers(request):
    return render(request,"readers.html",context={"current_tab": "readers"})


def shopping(request):
    return HttpResponse("Welcome to shoping")


def save_student(request):
    student_name = request.POST['student_name']
    return render(request,"welcome.html",context={'student_name':student_name})

def readers_tab(request):
 if request.method=="GET":
    readers = reader.objects.all()
    return render(request,"readers.html",context={"current_tab": "readers","readers":readers})
 else:
    query = request.POST['query']
    readers = reader.objects.raw("select * from lims_app_reader where reader_name like '%"+query+"%'")
    return render(request,"readers.html",context={"current_tab": "readers","readers":readers,"query":query})

def save_reader(request):
    reader_item = reader(reference_id=request.POST['reader_ref_id'],
                         reader_name=request.POST['reader_name'],
                         reader_cantact=request.POST['reader_contact'],
                         reader_address=request.POST['address'],
                         active=True
                         )
    reader_item.save()
    return redirect('/readers')
def books(request):
    return render(request,"books.html",context={"current_tab": "books"})
def index_view(request):
    return render(request, 'index_new.html')
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/update_book.html', {'form': form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'books/delete_book.html', {'book': book})

