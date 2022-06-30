from django.contrib import admin
from django.http import HttpResponseRedirect
from django.template.defaulttags import url
from django.utils.html import format_html
from django.urls import reverse

from .models import Choice, Chat, Message, ContactRequest, Client, DemoRequest, Demo


# Register your models here.


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "title_en", "response_en", "title_fr", "response_fr")
    search_fields = ["title_en", "title_fr"]


class MessageInlineAdmin(admin.TabularInline):
    model = Message
    readonly_fields = ['sender', 'chat', 'type', 'choice', 'content', 'date']
    exclude = ['choice_id']
    extra = 0

    def choice(self, obj):
        return Choice.objects.get(id=obj.choice_id)


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'language', 'user', 'number_of_messages')
    inlines = [MessageInlineAdmin]
    readonly_fields = ['date', 'language']

    def number_of_messages(self, obj):
        return obj.messages.count()


@admin.register(ContactRequest)
class ContactRequest(admin.ModelAdmin):
    model = ContactRequest

    list_display = ('id', 'created_at', 'client', 'content',
                    'agent',
                    'status', 'change_status', 'responseTime')

    readonly_fields = ['content', 'agent', 'client',
                       'chat', 'closed_at', 'responseTime']

    list_filter = ('status', 'agent')

    search_fields = ["client__firstName", "client__lastName", "agent__username"]

    list_editable = ['status']

    fieldsets = (
        (
            "Client", {
                "fields": (("client", "chat"), "content")
            }
        ),
        (
            "Agent", {
                "fields": ("agent", "agentNotes")
            }
        ),
        (
            "Request Status", {
                "fields": ("status", ("closed_at", "responseTime"))
            }
        )
    )

    def change_status(self, obj):
        action = ''
        if obj.status == 'unclaimed':
            action = 'Claim'
        elif obj.status == 'claimed':
            action = 'Close'
        return format_html(
            """ <a style="display:block;margin:auto;color:blue;width:70%;font-weight:bold" 
            href="../../cs/{}" >{}</a> """,
            obj.id,
            action
        )

    def save_model(self, request, obj, form, change):
        if obj.status == 'unclaimed':
            obj.agent = None
        if getattr(obj, 'agent', None) is None:
            if obj.status == 'claimed':
                obj.agent = request.user
        obj.save()

    def get_readonly_fields(self, request, obj=None):
        if obj.status == 'closed':
            return ['content', 'agent', 'client', 'status',
                    'chat', 'closed_at', 'responseTime']
        else:
            return super(ContactRequest, self).get_readonly_fields(request, obj)


@admin.register(Client)
class Client(admin.ModelAdmin):
    list_display = ('lastName', 'firstName', 'email', 'phone')


@admin.register(DemoRequest)
class DemoRequest(admin.ModelAdmin):
    list_display = ('id', 'client', 'demo', 'created_at')





