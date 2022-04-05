from django.db import models

# Chatbot Model
class Chatbot(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    language = models.CharField(max_length=2, choices=[('fr','Francais'),('en','English')])

    def __str__(self):
        return self.name
    # respond to choice
    # respond to text


# Choice Model
class Choice(models.Model):
    title_fr = models.CharField(max_length=80, blank=True, null=True)
    title_en = models.CharField(max_length=80, blank=True, null=True)
    response_fr = models.TextField(blank=True, null=True)
    response_en = models.TextField(blank=True, null=True)
    link_fr = models.CharField(max_length=200, blank=True, null=True)
    link_en = models.CharField(max_length=200, blank=True, null=True)
    next_choices = models.ManyToManyField("self",symmetrical=False, related_name="previous_choices", blank=True)

    def __str__(self):
        return self.title_en

# Message Model
class Message(models.Model):
    sender = models.CharField(max_length=7,choices=[('chatbot','Chatbot'),('user','User')], null=True)
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE, related_name='messages', null=True)
    type = models.CharField(max_length=6,choices=[('text','Text'),('choice','Choice')], null=True)
    content = models.TextField(blank=True, null=True)
    choice_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add= True, null=True)

    def __str__(self):
        return 'Message sent on :' + str(self.date)

# Chat Model
class Chat(models.Model):
    language = models.CharField(max_length=2, choices=[('fr','Francais'),('en','English')], null=True)
    date = models.DateTimeField(auto_now_add= True, null=True)
    #chatbot = models.CharField(max_length=80, blank=True, null=True)
    user = models.CharField(max_length=80, blank=True, null=True)
    #user_feedback = models.CharField(max_length=80, blank=True, null=True)
    #status = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return 'Chat started on :' + str(self.date)

    #Receive_Message
    #Change status

# Chat History Model


# User Model
class User(models.Model):
    username = models.CharField(max_length=80, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.username



# Client Model (inheritance from user to be added)
class Client(models.Model):
    #username = models.CharField(max_length=80, blank=True, null=True)
    firstName = models.CharField(max_length=80, blank=True, null=True)
    lastName = models.CharField(max_length=80, blank=True, null=True)
    #email = models.CharField(max_length=80, blank=True, null=True)
    phone = models.CharField(max_length=80, blank=True, null=True)
    address = models.CharField(max_length=80, blank=True, null=True)
    organization = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.firstName

# Agent Model

# Admin Model

# Contact Request Model

# Contact Request History
