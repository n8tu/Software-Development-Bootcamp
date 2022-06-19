from django.db import models
import datetime


class ShowManager(models.Manager):

    def show_validator(self,data):
        errors = {}
        if len(data['title']) < 2:
            errors['title'] = "cannot be less than 2 characters!"
        else:
            try:
                if data['show_id']:
                    show = Show.objects.get(id=data['show_id'])
                    if data['title'] == show.title :
                        pass
                    else:
                        show = Show.objects.get(title__iexact=data['title'])
                        errors['title'] = "is taken please try another one"  
                else:
                    show = Show.objects.get(title__iexact=data['title'])
                    errors['title'] = "is taken please try another one"     
            except: 
                pass
        if len(data['network']) < 2:
            errors['network'] = "cannot be less than 3 characters!"
        if 0 < len(data['description']) and len(data['description']) < 9:
            errors['description'] = "must be at least 10 characters!"
        if len(data['release_date']) > 0:
            _releaseDate = datetime.datetime.strptime(data['release_date'],'%Y-%m-%d')
            _todayDate = datetime.datetime.today()
            if _todayDate < _releaseDate:
                errors['release_date'] = "date should be in the past!"
        else:
            errors['release_date'] = "Field is required!"

        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    description = models.TextField(default="No description is set.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()



