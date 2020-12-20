from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 
from .models import Book, Author
# Create your views here.


  
def home(request):
    return HttpResponse(request,'poko/home.html')


def create(request):
    form = BlogForm()
    if request.method=='POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')


    context= {'form' : form}
    return render(request,'poko/create.html',context)


# Create your views here.

def home(request):
    return HttpResponse('Welcome to home Page')

def about(request):
    return render(request,'poko/about.html')

class MyView(View): 
    def get(self, request):
        return HttpResponse('Contact Page')
  
class BookF(View): 
    def get(self, request):
        form  =   BooksForm()
        model = Book.objects.all()
        context = {'form' : form, 'model': model}
        return render(request, 'poko/Class_page.html',context)

    def post(self, request):
        form  =   BooksForm(request.POST)
        model = Book.objects.all()
        if form.is_valid():
            form.save()

        context = {'form' : form, 'model': model}
        return render(request, 'poko/Class_page.html',context)    




def displayBlog(request):
    blog = BlogModel.objects.all()
    context = {'blog':blog}
    return render(request,'poko/display.html',context)



def  deletelist(request,id):
    blog = get_object_or_404(BlogModel, id = id)
    if request.method =="POST":
        blog.delete()
        return redirect('/')
    context = {}
    return render(request,"poko/delete.html",context)



def updatelist(request, id):
    blog = get_object_or_404(BlogModel, id = id)
    form = BlogForm(instance = blog)
    if (request.method == 'POST'):
        form = BlogForm(request.POST,request.FILES,instance = blog)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context ={'form':form}
    return render(request,'poko/update.html',context)
    







    #govind@203
    #govindkumar
