from django.shortcuts import render,redirect,HttpResponse
from .models import News,Student
from .forms import CreateNewsForm,CreateStudentForm

def index(request):
    infos = News.objects.all()
    context ={
        'infos': infos,
}
    return render(request,'main/index.html',context)

def news(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'main/News/news.html', context)

def updateView(request, id):
    news = News.objects.get(id=id)

    if request.method == 'POST':
        form = CreateNewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect(to='main:index')
        return HttpResponse("Invalid data")

    form = CreateNewsForm(instance=news)
    context={'form':form}
    return render(request, 'main/index2.html', context)

def deleteView(request,id):
    news = News.objects.get(id=id)
    news.delete()
    return redirect(to='main:index')
####################################


def student(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'main/News/student.html', context)


def student_updateView(request, id):
    students = Student.objects.get(id=id)

    if request.method == 'POST':
        form = CreateStudentForm(request.POST, instance=students)
        if form.is_valid():
            form.save()
            return redirect(to='main:index')
        return HttpResponse("Invalid data")

    form = CreateStudentForm(instance=students)
    context={'form':form}
    return render(request, 'main/index2.html', context)

def student_deleteView(request,id):
    students = Student.objects.get(id=id)
    students.delete()
    return redirect(to='main:index')