from django.contrib import admin
from .models import Choice,Chat,Message

# Register your models here.




@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("id","title_en","response_en","title_fr","response_fr")
    search_fields = ["title_en","title_fr"]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender','type','content','choice','date','chat')
    def choice(self, obj):
        return Choice.objects.get(id=obj.choice_id)



class MessageInlineAdmin(admin.TabularInline):
    model = Message
    readonly_fields = ['sender','chat','type','choice','content','date']
    exclude = ['choice_id']
    extra = 0
    def choice(self, obj):
        return Choice.objects.get(id=obj.choice_id)

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id','date','language','user','number_of_messages')
    inlines = [MessageInlineAdmin]
    readonly_fields = ['date','language']
    def number_of_messages(self, obj):
        return obj.messages.count()

