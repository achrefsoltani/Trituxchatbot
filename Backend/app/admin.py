from django.contrib import admin
from .models import Choice,Chat,User,Client,Chatbot

# Register your models here.
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("title_en","title_fr","response_fr")

admin.site.register(Chat)
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Chatbot)

