from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from secret import API_KEY

# Create your views here.


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            message = Mail(
                from_email=form.cleaned_data['from_email'],
                to_emails=form.cleaned_data['to_email'],
                subject=form.cleaned_data['subject'],
                html_content=form.cleaned_data['message'])
            try:
                # send_mail(subject, message, from_email, ['j.yanming@gmail.com'])
                sg = SendGridAPIClient(API_KEY)
                response = sg.send(message)
            except BadHeaderError as e:
                return HttpResponse(e.message)
            return redirect('success')
    return render(request, "email.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')
