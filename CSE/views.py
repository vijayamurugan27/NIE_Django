from django.shortcuts import render

from CSE.models import Student

# Create your views here.

def home(request):
    return render(request, 'home.html')


def students(request):
    student = Student.objects.all()
    context = {'student': student}
    return render(request, 'student.html', context)




from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

class Forms(CreateView):
    model = Student
    fields = "__all__"
    template_name = 'forms.html'
    success_url = '/'

class StudentList(ListView):
    model = Student
    template_name = 'stulist.html'

class StudentDetail(DetailView):
    model = Student
    template_name = 'studetail.html'

class StudentUpdate(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'stuupdate.html'
    success_url = '/'

class StudentDelete(DeleteView):
    model = Student
    template_name = 'studelete.html'
    success_url = '/'


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')
