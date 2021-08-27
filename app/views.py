from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .resources import PersonResource
from tablib import Dataset
from django.http import HttpResponse
import datetime
from django.contrib import messages

def home(request):
    return render(request,"home.html")


def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,"You have Registerd successfully")
            form.save()
    else:
        form = SignUpForm()
    return render(request,"signup.html",{"form":form})
 

def BookList(request):
    book_list = Book.objects.all()
    return render(request,"book_list.html",{'book_list':book_list})


def BookDetail(request, pk):
    book = get_object_or_404(Book, id=pk)
    try:
        stu = Student.objects.get(roll_no=request.user)
    except:
        pass
    return render(request, 'book_detail.html', {'book':book})

@login_required
def Bookupload(request):
    if request.method == 'POST':
        form = BookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            messages.success(request,"Book uploaded")
            form.save()
            return redirect(home)
    else:
        form = BookForm()
    return render(request, 'book_upload.html', {'form':form})

@login_required
def BookUpdate(request,id):
    upd=Person.objects.get(id=id)
    update=PersonForm(request.POST or None,request.FILES or None,instance=upd)
    if update.is_valid():
        messages.success(request,"Book data updated")
        update.save()
        return redirect(home)
    return render(request,"book_update.html",{"update":update}) 

@login_required
def BookDelete(request,id):
    d_book = Person.objects.get(id=id)
    d_book.delete()

    return redirect(home)

# @login_required
# def student_request_issue(request, pk):
#     obj = Book.objects.get(id=pk)
#     stu=Student.objects.get(roll_no=request.user)
#     s = get_object_or_404(Student, roll_no=str(request.user))
#     if s.total_books_due < 10:
#         message = "book has been isuued, You can collect book from library"
#         a = Borrower()
#         a.student = s
#         a.book = obj
#         a.issue_date = datetime.datetime.now()
#         obj.available_copies = obj.available_copies - 1
#         obj.save()
#         stu.total_books_due=stu.total_books_due+1
#         stu.save()
#         a.save()
#     else:
#         message = "you have exceeded limit."
#     return render(request, 'issue.html', {"obj":obj})


@login_required
def StudentCreate(request):
    if request.method == 'POST':
        form = StudentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            messages.success(request,"Student added")
            form.save()
            return redirect(home)
    else:
        form = StudentForm()
    return render(request, 'student_create.html', {'form':form})

@login_required
def StudentList(request):
    students = Student.objects.all()
    return render(request,"student_list.html",{"students":students})


@login_required
def StudentDetail(request, pk):
    student = get_object_or_404(Student, id=pk)
    
    return render(request, 'student_detail.html',{"student":student})

@login_required
def StudentUpdate(request,id):
    upd=Student.objects.get(id=id)
    update=StudentForm(request.POST or None,request.FILES or None,instance=upd)
    if update.is_valid():
        messages.success(request,"Student data Upadated")
        update.save()
        return redirect(home)
    return render(request,"student_update.html",{"update":update}) 

@login_required
def StudentDelete(request,id):
    stu_d = Student.objects.get(id=id)
    stu_d.delete()

    return redirect(home)

def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']
        
        if not new_person.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'book_create.html')

        imported_data = dataset.load(new_person.read(),format='xlsx')
        for data in imported_data:
            value = Person(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7]
            )
            messages.success(request,"Books Added")
            value.save()
    return render(request,'book_create.html')

def detail(request):
    detail_list = Person.objects.all()
    return render(request,'book_list.html',{'detail_list': detail_list})



