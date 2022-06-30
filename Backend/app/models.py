import datetime

from django.db import models
from django.contrib.auth import get_user_model


# Chatbot Model

class Chatbot(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    language = models.CharField(max_length=2, choices=[('fr', 'Francais'), ('en', 'English')])

    def __str__(self):
        return self.name


# Choice Model
class Choice(models.Model):
    title_fr = models.CharField(max_length=80, blank=True, null=True)
    title_en = models.CharField(max_length=80, blank=True, null=True)
    response_fr = models.TextField(blank=True, null=True)
    response_en = models.TextField(blank=True, null=True)
    link_fr = models.CharField(max_length=200, blank=True, null=True)
    link_en = models.CharField(max_length=200, blank=True, null=True)
    next_choices = models.ManyToManyField("self", symmetrical=False, related_name="previous_choices", blank=True)

    def __str__(self):
        return self.title_en


# Message Model
class Message(models.Model):
    sender = models.CharField(max_length=7, choices=[('chatbot', 'Chatbot'), ('user', 'User')], null=True)
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE, related_name='messages', null=True)
    type = models.CharField(max_length=6, choices=[('text', 'Text'), ('choice', 'Choice')], null=True)
    content = models.TextField(blank=True, null=True)
    choice_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return 'Message sent on :' + str(self.date)


# Chat Model
class Chat(models.Model):
    language = models.CharField(max_length=2, choices=[('fr', 'Francais'), ('en', 'English')], null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return "Chat started at %s:%s:%s" % (self.date.hour, self.date.minute, self.date.second)


# Client Model
class Client(models.Model):
    firstName = models.CharField(max_length=80, blank=True, null=True)
    lastName = models.CharField(max_length=80, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    phone = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.lastName + ' ' + self.firstName


# ContactRequest Model
class ContactRequest(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name="contactRequests", null=True,
                               blank=True)
    chat = models.ForeignKey('Chat', on_delete=models.SET_NULL, related_name="contactRequests", null=True, blank=True)
    content = models.TextField(blank=True, null=True)
    agent = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    agentNotes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20,
                              choices=[('unclaimed', 'Unclaimed'), ('claimed', 'Claimed'), ('closed', 'Closed')],
                              blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    responseTime = models.DurationField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.status == 'closed':
            self.closed_at = datetime.datetime.now()
            self.responseTime = self.closed_at - self.created_at.replace(tzinfo=None)
        super().save(*args, **kwargs)


# DemoRequest Model
class DemoRequest(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name="demoRequests", null=True, blank=True)
    demo = models.ForeignKey('Demo', on_delete=models.CASCADE, related_name="demoRequests", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


# Demo Model
class Demo(models.Model):
    service = models.CharField(max_length=20,
                               choices=[('1', 'service 1'), ('2', 'service2'), ('3', 'service 3')],
                               blank=True)
    date = models.DateTimeField(null=True, blank=True)
    event_id = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.get_service_display() + ' , ' + self.date.strftime("%m/%d/%Y, %H:%M:%S")
