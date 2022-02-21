from django.db import models

# Chatbot Model
class Chatbot(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    language = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.name
    # respond to choice
    # respond to text


# Choice Model
class Choice(models.Model):
    title_fr = models.CharField(max_length=80, blank=True, null=True)
    title_en = models.CharField(max_length=80, blank=True, null=True)
    response_fr = models.CharField(max_length=200, blank=True, null=True)
    response_en = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=80, blank=True, null=True)
    next_choices = models.ManyToManyField("self",symmetrical=False, related_name="previous_choices", blank=True)

    def __str__(self):
        return self.title_en



# Chat Model
class Chat(models.Model):
    language = models.CharField(max_length=80, blank=True, null=True)
    date = models.CharField(max_length=80, blank=True, null=True)
    chatbot = models.CharField(max_length=80, blank=True, null=True)
    chatbot_messages = models.CharField(max_length=80, blank=True, null=True)
    user = models.CharField(max_length=80, blank=True, null=True)
    user_messages = models.CharField(max_length=80, blank=True, null=True)
    user_feedback = models.CharField(max_length=80, blank=True, null=True)
    status = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.date

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
