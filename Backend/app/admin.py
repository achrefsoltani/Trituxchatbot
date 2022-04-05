from django.contrib import admin
from .models import Choice,Chat,Message

# Register your models here.




@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("title_en","title_fr","response_fr")

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender','type','content','choice_id','date','chat')


class MessageInlineAdmin(admin.TabularInline):
    model = Message
    readonly_fields = ['sender','chat','type','content','choice_id','date']
    extra = 0

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('date','language')
    inlines = [MessageInlineAdmin]
    readonly_fields = ['date','language']

