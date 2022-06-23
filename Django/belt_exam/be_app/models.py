from django.db import models
import re
import bcrypt
import datetime

class UserManager(models.Manager):
    def register_validation(self,postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors['fname'] = "First Name must be more than 2 characters "

        if len(postData['lname']) < 2:
            errors['lname'] = "Last Name must be more than 2 characters "

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email is not valid"
        else:
            try:
                user = User.objects.get(email__iexact=postData['email'])
                errors['email'] = "Email is already registered try to login!"  
            except:
                pass

        if postData['password'] != postData['confirm_password']:
            errors["passwords"] = "passwords are not matched!" 

        if len(postData['password']) < 8:
            errors["password"] = "password should be at least 8 characters" 
        
        return errors

    def login_validation(self,postData):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email is not valid"
        else:
            try:
                user = User.objects.get(email__iexact=postData['email'])
                if not bcrypt.checkpw(postData['password'].encode(),user.password.encode()):
                    errors['login'] = "Email or Password is incorrect !"
            except:
                errors['login'] = "Email or Password is incorrect !"
        
        return errors

class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()



class TripManager(models.Manager):
    def validation(self,postData):
        errors = {}
        if len(postData['destination']) < 3:
            errors['destination'] = "Destination must be more than 3 characters"

        if len(postData['plan']) < 3:
            errors['plan'] = "Plan must be more than 5 characters"

        if postData['start_date'] and postData['end_date']:
            start_date = datetime.datetime.strptime(postData['start_date'],"%Y-%m-%d") 
            end_date = datetime.datetime.strptime(postData['end_date'],"%Y-%m-%d") 

            if start_date < datetime.datetime.today():
                errors['start_date'] = "Start date should not be in the past !"

            if end_date < start_date: 
                errors['end_date'] = "The trip shouldn't end before it starts !"
        else:
            errors['dates'] = "All dates are required !"

        
        return errors

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    plan = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,related_name="trip_information",on_delete=models.CASCADE)
    joined_the_trip = models.ManyToManyField(User,related_name="trips")
    objects = TripManager()

