from django.shortcuts import render,redirect
from .models import FeedbackData
from.models import ContactData
from.models import CourseData
from django.contrib.auth import authenticate,logout,login
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method=='POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        user = authenticate(username = username1,password = password1)
        if user is not None:
            login(request,user)
            return redirect('home_page')
            return render(request,'login.html')
        else:
            return HttpResponse('invalid name or password')
            return redirect('login')
    return render(request,'login.html')

login_required(login_url='login')
def home_view(request):
    return render(request,'home.html')

def contact_view(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        company = request.POST.get('company')
        salary = request.POST.get('salary')
        location = request.POST.get('location')

        ContactData(
            fname=fname,
            lname=lname,
            email=email,
            company=company,
            salary=salary,
            location=location,

        ).save()

        return render(request, 'contact.html')

    else:
        return render(request, 'contact.html')


login_required(login_url='login')
def services_view(request):
    courses = CourseData.objects.all()
    return render(request,'services.html',{'courses':courses})
login_required(login_url='login')
def feedback_view(request):
    if request.method == "POST":
        name1 = request.POST.get('name')
        rating1 = request.POST.get('rating')
        feedback1 = request.POST.get('feedback')


        FeedbackData(
            name = name1,
            rating = rating1,
            feedback = feedback1
        ).save()



        feedbacks = FeedbackData.objects.all()
        return render(request, 'feedback.html', {'singh': feedbacks})



    else:
        feedbacks = FeedbackData.objects.all()
        return render(request, 'feedback.html', {'singh': feedbacks})


login_required(login_url='login')
def gallery_view(request):
    return render(request,'gallery.html')

def logout_page(request):
    logout(request)
    return redirect('login')

