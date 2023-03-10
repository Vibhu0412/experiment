from pyexpat import model
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View

from django.contrib import messages
from .forms import ContactForm, SubscriptionEmailForm
# from mainapp.forms import ContactForm
from . import models
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

from django.core.exceptions import ValidationError
from django.core.validators import validate_email


# Create your views here.
def home(request):
    if request.POST.get("form_type") == 'contact_form':
        print('Contact Main Page')
        if request.method == 'POST':
            name = request.POST['name']
            mobile = request.POST['mobile']
            sender = request.POST['email']

            subject = request.POST['subject']
            message = request.POST['message']

            try:
                validate_email(sender)
                s = models.contact(name=name, mobile=mobile, email=sender, subject=subject, looking_for=message)
                s.save()
                messages.success(request, 'Thanks for connecting! Will reach out soon.', extra_tags='contact_msg')
            except ValidationError as e:
                messages.error(request, 'Please Enter a valid email!', extra_tags='contact_msg')
                print("bad email, details:", e)
            else:
                print("good email")
            return HttpResponseRedirect('/#contact-form')

            # s = models.contact(name=name, mobile=mobile, email=sender, subject=subject, looking_for=message)
            # s.save()

            # message = f'Name : {request.POST["name"]}:\n Mobile : {request.POST["mobile"]}:\n Email : {request.POST["email"]}\n Message : {request.POST["message"]}'
            # send_mail(subject, message, settings.EMAIL_HOST_USER, ['vaibhav.purohit@tecblic.com'], fail_silently=False)
            # return render(request, 'index.html')

    elif request.POST.get("form_type") == 'subscribe_form':
        subscrip_mail = request.POST['sub_email']
        print("Subscription MAIL : " + str(subscrip_mail))
        if subscrip_mail != "":
            p = models.SubscriptionEmail(subemail=subscrip_mail)
            p.save()
            messages.success(request, 'Thanks for subscribing!', extra_tags='subscribe_msg')
        else:
            messages.error(request, 'Please Enter a valid email!', extra_tags='subscribe_msg')
        return HttpResponseRedirect('/#subscribe-form')
    else:
        return render(request, 'index.html')
    # form = SubscriptionEmailForm()
    # return render(request, "index.html", {"form": form})


def services(request):
    return render(request, 'service.html')


def technology(request):
    return render(request, 'technology.html')


def blog(request):
    return render(request, 'blog.html')


def aboutus(request):
    return render(request, 'about.html')


def contactus(request):
    if request.POST.get("form_type") == 'contact_form':
        print('Contact Main Page')
        if request.method == 'POST':
            name = request.POST['name']
            mobile = request.POST['mobile']
            sender = request.POST['email']

            subject = request.POST['subject']
            message = request.POST['message']

            try:
                validate_email(sender)
                s = models.contact(name=name, mobile=mobile, email=sender, subject=subject, looking_for=message)
                s.save()
                messages.success(request, 'Thanks for connecting! Will reach out soon.', extra_tags='contact_msg')
            except ValidationError as e:
                messages.error(request, 'Please Enter a valid email!', extra_tags='contact_msg')
                print("bad email, details:", e)
            else:
                print("good email")
            return HttpResponseRedirect('#contact-form')

            # s = models.contact(name=name, mobile=mobile, email=sender, subject=subject, looking_for=message)
            # s.save()
            # message = f'Name : {request.POST["name"]}:\n Mobile : {request.POST["mobile"]}:\n Email : {request.POST["email"]}\n Message : {request.POST["message"]}'
            # send_mail(subject, message, settings.EMAIL_HOST_USER, ['vaibhav.purohit@tecblic.com'], fail_silently=False)
            # return redirect('contactus')
    elif request.POST.get("form_type") == 'subscribe_form':
        subscrip_mail = request.POST['sub_email']
        if subscrip_mail != "":
            p = models.SubscriptionEmail(subemail=subscrip_mail)
            p.save()
            messages.success(request, 'Thanks for subscribing!', extra_tags='subscribe_msg')
        else:
            messages.error(request, 'Please Enter a valid email!', extra_tags='subscribe_msg')
        return HttpResponseRedirect('#subscribe-form')
    else:
        return render(request, 'contact.html')


def aiml(request):
    return render(request, 'ai-service.html')


def odoo(request):
    return render(request, 'odoo.html')


def python(request):
    return render(request, 'python.html')


def robotic(request):
    return render(request, 'Robotic.html')


def BusinessConsulting(request):
    return render(request, 'consulting.html')


def BusinessIntelligence(request):
    return render(request, 'Business-Intelligence.html')


def hire(request):
    return render(request, 'hire.html')


def pwa(request):
    return render(request, 'pwa-development.html')


def AI(request):
    return render(request, 'ai.html')


def RPA(request):
    return render(request, 'rpa.html')


def PythonTechnology(request):
    return render(request, 'python-1.html')


def Django(request):
    return render(request, 'django.html')


def Golang(request):
    return render(request, 'golang.html')


def Flutter(request):
    return render(request, 'flutter.html')


def ReactJs(request):
    return render(request, 'react.html')


def oddocrm(request):
    return render(request, 'blog-1.html')


def aimlblog(request):
    return render(request, 'blog-3.html')


def Oddofuture(request):
    return render(request, 'blog-2.html')


def oddocrm(request):
    return render(request, 'blog-1.html')


def aimlblog(request):
    return render(request, 'blog-3.html')


def Oddofuture(request):
    return render(request, 'blog-2.html')


@csrf_exempt
def Contactdata(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        sender = request.POST['email']

        subject = request.POST['subject']
        message = request.POST['message']

        s = models.contact(name=name, mobile=mobile, email=sender, subject=subject, looking_for=message)
        s.save()
        print(s)
        message = f'Name : {request.POST["name"]}:\n Mobile : {request.POST["mobile"]}:\n Email : {request.POST["email"]}\n Message : {request.POST["message"]}'
        send_mail(subject, message, settings.EMAIL_HOST_USER, ['vaibhav.purohit@tecblic.com'], fail_silently=False)
        return redirect('/')

    # return render(request, 'blog-1.html')


def Blog_1(request):
    return render(request, 'blog-1.html')


def Blog_2(request):
    return render(request, 'blog-2.html')


def Blog_3(request):
    return render(request, 'blog-3.html')


def NewsLetter(request):
    # print(request.GET['sub_email'])
    # if request.get("form_type") == 'subscribe_form':
    #     print('Subscribe Clicked')
    if request.POST.get("form_type") == 'subscribe_form':
        # subscrip_mail = request.POST['sub_email']
        subscrip_mail = request.POST['sub_email']
        print(subscrip_mail)
        p = models.SubscriptionEmail(subemail=subscrip_mail)
        p.save()
        # p = models.SubscriptionEmail.objects.create(subemail=subscrip_mail)
        return redirect('/')
    else:
        print("Inside ELSE")
    return render(request, 'contact.html')

    # form = SubscriptionEmailForm(request.POST)
    # if form.is_valid():
    #     form.save()
    #     subemail = form.get('sub_email')
    #     print(subemail)
    #     return redirect('/')

    # if subemail is not None:
    #     subemail = models.SubscriptionEmail(subemail=subemail)
    #     print(subemail)
    #     subemail.save()
    #     subject = 'New Subscription Request'
    #     message = "Please initiate the subscription for me!"
    #     send_mail(subject, message, subemail, [settings.EMAIL_HOST_USER], fail_silently=False)
