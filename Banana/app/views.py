from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from .models import *
from .models import Blogs
from django.core.mail import send_mail



# Create your views here.
def base(request):
    return render(request,'base.html')


def home(request):
    Carousel_data = Carousel.objects.all()
    data={
        'carousel_data': Carousel_data
    }
    return render(request,'home.html',data)

def products(request):
    return render(request,'products.html')

def services(request):
    return render(request,'services.html')

def interior(request):
    Interior_products_data = Interior_products.objects.all()
    data={
        'interior_products_data':Interior_products_data
    } 
    if request.method == 'POST':
        first_name=request.POST.get('First-Name')
        last_name=request.POST.get('Last-Name')
        mbl_no=request.POST.get('Mbl_No')
        pincode=request.POST.get('Pincode')
        email=request.POST.get('Email')
        adress=request.POST.get('Adress')
        # print(contact.last_name,contact.first_name,contact.email,contact.adress,contact.pincode,contact.mbl_no)
        # return HttpResponse("{0}{1}{2}{3}{4}{5}".format(first_name,last_name,email,mbl_no,pincode,adress))
        send_mail(
            'Interior Product Customer:{0} {1}'.format(first_name,last_name),
            'First Name:{0} \nLast Name: {1}\nMobile Number: {2}\nEmail Address: {3}\npincode: {4}\naddress: {5}\n'.format(first_name,last_name,mbl_no,email,pincode,adress),
            'gauravpatil795@gmail.com',
            ['domghostgp22@gmail.com'],
            fail_silently=False,
        )
        contact = Contacts(first_name=first_name,last_name=last_name,mbl_no=mbl_no,pincode=pincode,email=email,adress=adress)
        contact.save()
    return render(request,'Interior.html',data)

def exterior(request):
    Exterior_products_data = Exterior_products.objects.all()
    data={
        'exterior_products_data':Exterior_products_data
    }
    if request.method == 'POST':
        first_name=request.POST.get('First-Name')
        last_name=request.POST.get('Last-Name')
        mbl_no=request.POST.get('Mbl_No')
        pincode=request.POST.get('Pincode')
        email=request.POST.get('Email')
        adress=request.POST.get('Adress')
        send_mail(
            'Exterior Product Customer:{0} {1}'.format(first_name,last_name),
            'First Name:{0} \nLast Name: {1}\nMobile Number: {2}\nEmail Address: {3}\npincode: {4}\naddress: {5}\n'.format(first_name,last_name,mbl_no,email,pincode,adress),
            'gauravpatil795@gmail.com',
            ['domghostgp22@gmail.com'],
            fail_silently=False,
        )
        contact = Contacts(first_name=first_name,last_name=last_name,mbl_no=mbl_no,pincode=pincode,email=email,adress=adress)
        contact.save()
        # return HttpResponse("{0}{1}{2}{3}{4}{5}".format(first_name,last_name,email,mbl_no,pincode,adress))
    return render(request,'Exterior.html',data)


def base_paint(request):
    Base_paint_products_data = Base_paint_products.objects.all()
    data={
        'base_paint_products_data':Base_paint_products_data
    } 
    if request.method == 'POST':
        first_name=request.POST.get('First-Name')
        last_name=request.POST.get('Last-Name')
        mbl_no=request.POST.get('Mbl_No')
        pincode=request.POST.get('Pincode')
        email=request.POST.get('Email')
        adress=request.POST.get('Adress')
        send_mail(
            'Base_paint Product Customer:{0} {1}'.format(first_name,last_name),
            'First Name:{0} \nLast Name: {1}\nMobile Number: {2}\nEmail Address: {3}\npincode: {4}\naddress: {5}\n'.format(first_name,last_name,mbl_no,email,pincode,adress),
            'gauravpatil795@gmail.com',
            ['domghostgp22@gmail.com'],
            fail_silently=False,
        )
        contact = Contacts(first_name=first_name,last_name=last_name,mbl_no=mbl_no,pincode=pincode,email=email,adress=adress)
        contact.save()
        # return HttpResponse("{0}{1}{2}{3}{4}{5}".format(first_name,last_name,email,mbl_no,pincode,adress))
    return render(request,'base_paint.html',data)

def blogs(request):
    Blogs_data = Blogs.objects.all()
    data={
        'blogs_data': Blogs_data
    }
    return render(request,'blogs.html',data)

def blogs_pages(request,blogs_id):
    Blogs_pages_data = Blogs.objects.get(id=blogs_id)
    data={
        'blogs_pages_data': Blogs_pages_data
    }
    print(Blogs_pages_data)
    return render(request,'blogs_pages.html',data)

def choose_color(request):
    Colors_code = Colors.objects.all()
    data={
        'colors_code':Colors_code
    }
    return render(request,'choose_color.html',data)

# def about_us(request):
#     if request.method == 'GET':
#         Name = request.GET.get('name')
#     return render(request,'about_us.html',{'name':Name})

def putty_services(request):
    return render(request,'get_in_touch_1.html')

def contact_us(request):
    return render(request,'contact_us.html')

# def Login(request):
#     try:
#         if request.method == 'POST':
#             P_Name = request.POST.get('name')
#             P_Email = request.POST.get('email')
#             P_Password  = request.POST.get('pass')
#             print(P_Name, P_Email, P_Password)
#             return HttpResponse(request, P_Name, P_Email, P_Password)
#     except:
#         pass
#     return render(request,'login.html')

def form(request):
    try:
        if request.method == 'POST':
            First_Name = request.POST.get('First-Name')
            Last_Name = request.POST.get('Last-Name')
            Mbl_No = request.POST.get('Mbl_No')
            Pincode  = request.POST.get('Pincode')
            Email  = request.POST.get('Email')
            Adress  = request.POST.get('Adress')
            Query  = request.POST.get('query')
            Paint_choice  = request.POST.get('paint_choice')
            Service_choice  = request.POST.get('service_choice')
            Message = request.POST.get('message')
            
            send_mail(
            'Customer:{0} {1}'.format(First_Name,Last_Name),
            'First Name:{0} \nLast Name: {1}\nMobile Number: {2}\nEmail Address: {3}\npincode: {4}\naddress: {5}\nQuery: {6}\nPaint_choice: {7}\nService_choice: {8}\nMessage: {9}'.format(First_Name,Last_Name,Mbl_No,Email,Pincode,Adress,Query,Paint_choice,Service_choice,Message),
            'gauravpatil795@gmail.com',
            ['domghostgp22@gmail.com'],
            fail_silently=False,
            )
            
            contact = Contacts(first_name=First_Name,last_name=Last_Name,mbl_no=Mbl_No,pincode=Pincode,email=Email,adress=Adress,other_query=Query,paint_choice=Paint_choice,service_choice=Service_choice,message=Message)
            contact.save()
            print(First_Name,Last_Name,Mbl_No,Pincode,Email,Adress,Query,Paint_choice,Service_choice,Message)
    except:
        pass

    return render(request,'thank_you.html')
    # return HttpResponse("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}".format(First_Name,Last_Name,Mbl_No,Pincode,Email,Adress,Query,Paint_choice,Service_choice,Message))