from django.shortcuts import render
from .models import Student
from django.views.generic import *
from .forms import StudentModelForm
class Homeview(CreateView):
    model = Student
    fields = ['rn', 'name', 'marks']
    success_url = '/studentlist/'

class StudentListView(ListView):
    model = Student

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['rn', 'name', 'marks']
    success_url = '/updatesuccess/'

class SuccessUpdate(TemplateView): #this is how we can create Template View to render after successful updation.
    template_name = 'firstapp/successupdate.html'


class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/studentlist/'




