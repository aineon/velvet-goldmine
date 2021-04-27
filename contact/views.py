from django.shortcuts import (render, redirect,
                              reverse, HttpResponseRedirect)
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string, get_template

from .models import NewsletterSubscription
from .forms import ContactForm, SubscriptionForm


def contact(request):
    template = "contact/contact.html"

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Message Sent! We'll be in touch shortly!")
            instance = form.save()
            """Send email confirming message received"""
            sender_email = instance.email
            subject = render_to_string(
                'contact/confirmation_emails/message_confirmation_subject.txt',
                {'instance': instance})
            body = render_to_string(
                'contact/confirmation_emails/message_confirmation_body.txt',
                {'instance': instance,
                 'contact_email': settings.DEFAULT_FROM_EMAIL})
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [sender_email],
            )

        else:
            messages.error(request, 'Message failed to send.'
                           ' Please ensure the form is valid.')

    form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, template, context)


def newsletter_signup(request):

    news_sub_form = SubscriptionForm(request.POST or None)

    if news_sub_form.is_valid():
        instance = news_sub_form.save(commit=False)
        if (NewsletterSubscription.objects.filter(
                email=instance.email).exists()):
            messages.error(request, 'Sorry! This email address \
                           is already registered for our Newsletter.')
        else:
            instance.save()
            messages.success(request, "Congratulations! "
                             " You've been added to our mailing list!")
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [instance.email]
            subject = 'Thank You for Signing Up!'
            body = render_to_string(
                'contact/confirmation_emails/newsletter_signup_confirmation_body.txt',
                {'instance': instance})
            signup_confirmation_email = EmailMultiAlternatives(
                                                subject=subject,
                                                body=body,
                                                from_email=from_email,
                                                to=to_email)
            html_template = get_template(
                'contact/confirmation_emails/newsletter_signup_confirmation_body.html'
                ).render()
            signup_confirmation_email.attach_alternative(html_template,
                                                         'text/html')
            signup_confirmation_email.send()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def newsletter_unsubscribe(request):
    news_sub_form = SubscriptionForm(request.POST or None)

    if news_sub_form.is_valid():
        instance = news_sub_form.save(commit=False)
        if (NewsletterSubscription.objects.filter(
                email=instance.email).exists()):
            to_email = [instance.email]
            print(to_email)
            subject = render_to_string(
                'contact/confirmation_emails/newsletter_unsubscribe_confirmation_subject.txt')
            body = render_to_string(
                'contact/confirmation_emails/newsletter_unsubscribe_confirmation_body.txt',
                {'instance': instance,
                 'contact_email': settings.DEFAULT_FROM_EMAIL})
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                to_email,
            )
            NewsletterSubscription.objects.filter(
                email=instance.email).delete()
            messages.success(request, f'{instance.email} \
                             has been removed from our mailing list')

        else:
            messages.error(request, 'Sorry! That email address \
                           does not exist in our database.')

    news_sub_form = SubscriptionForm()
    template = 'contact/newsletter_unsubscribe.html'
    context = {
        'news_sub_form': news_sub_form,
    }

    return render(request, template, context)
