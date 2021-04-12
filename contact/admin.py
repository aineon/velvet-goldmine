from django.contrib import admin
from .models import ReceivedMessage, NewsletterSubscription


class ReceivedMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'date_sent',)


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed',)


admin.site.register(NewsletterSubscription, NewsletterAdmin)
admin.site.register(ReceivedMessage, ReceivedMessageAdmin)
