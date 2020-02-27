from django.db import models

# Create your models here.

class Questions(models.Model):

    CHOICES = (("1","Easy"),("2","Medium"),("3","Difficult"))
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=100)
    description = models.TextField()
    props = models.CharField(max_length=100)
    type = models.CharField(choices=CHOICES,max_length=100)
    def __str__(self):
        return self.question
    def get_choices(self):

        return self.CHOICES

class Submissions(models.Model):

    name = models.CharField(max_length=100)
    partner_name = models.CharField(max_length=100)
    code = models.TextField()

    def __str__(self):

        return self.name+self.partner_name