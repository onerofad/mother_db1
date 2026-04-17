from django.db import models

# Create your models here.
class Register(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    about = models.CharField(max_length=255, default='')
    state = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    picture = models.TextField(max_length=255, default='')
    sendemail = models.BooleanField(default=False)
    sendphone = models.BooleanField(default=False)
    no = models.BooleanField(default=False)
    customer = models.CharField(max_length=255, default='')
    payment_method = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.firstname
    
class MakeRequest(models.Model):
    selectedStartDate = models.CharField(max_length=255, default='')
    startTime = models.CharField(max_length=255, default='')
    endTime = models.CharField(max_length=255, default='')
    watcher_role = models.TextField()
    mother_name = models.CharField(max_length=255, default='')
    child_no = models.IntegerField(default=0)
    child_option2 = models.CharField(max_length=255, default='')
    rate_hour = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255, default='')
    email_to = models.CharField(max_length=255, default='', blank=True)
    location = models.CharField(max_length=255, default='')
    address = models.TextField(default='')
    zipcode = models.CharField(max_length=255, default='')
    picture = models.TextField(default='')
    picture2 = models.TextField(default='')
    watcher_name = models.CharField(max_length=255, default='')
    status = models.BooleanField(default=False)
    confirm = models.BooleanField(default=False)


    def __str__(self):
        return self.email
    
class Support(models.Model):
    email = models.CharField(max_length=255)
    helpText = models.TextField()

    def __str__(self):
        return self.helpText
    
class RegisterWatcher(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    phoneno = models.CharField(max_length=255)
    dob = models.CharField(max_length=255, default='')
    gender = models.CharField(max_length=255, default='')
    state = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    skills = models.TextField(max_length=255, default='')
    about = models.TextField(max_length=255, default='')
    picture = models.TextField(max_length=255, default='')
    hour_rate = models.CharField(max_length=255, default='')
    cpr = models.BooleanField(default=False)
    firstaid = models.BooleanField(default=False)
    backcheck = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    sendemail = models.BooleanField(default=False)
    sendphone = models.BooleanField(default=False)
    no = models.BooleanField(default=False)


    def __str__(self):
        return self.firstname
    
class Chats(models.Model):
    chat = models.CharField(max_length=255)
    sender_email = models.CharField(max_length=255, default='')
    received_email = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.chat

class Cards(models.Model):
    firstname = models.CharField(max_length=255, default='')
    lastname = models.CharField(max_length=255, default='')
    address1 = models.CharField(max_length=255, default='')
    address2 = models.CharField(max_length=255, default='', blank=True)
    country = models.CharField(max_length=255, default='')
    state = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    zipcode = models.CharField(max_length=255, default='')
    mobile = models.CharField(max_length=255, default='')
    cardnumber = models.CharField(max_length=255, default='')
    expirationdate = models.CharField(max_length=255, default='')
    cvv = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255, default='')
    plan = models.CharField(max_length=255, default='', blank=True)

    def __str__(self):
        return self.cardnumber

class Payment(models.Model):
    amount = models.CharField(max_length=10)
    currency = models.CharField(max_length=10, default="usd")
    stripe_payment_id = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_email = models.EmailField()

class Payments(models.Model):
    amount = models.FloatField(max_length=10, default=0)
    currency = models.CharField(max_length=10, default="usd")
    payment_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    customer_id = models.CharField(max_length=255, null=True, blank=True)
    payment_method = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    to_email = models.EmailField(default="")
    request_id = models.IntegerField(default=0, blank=True, null=True)
    


