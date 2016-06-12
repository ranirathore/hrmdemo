from django.db import models
import datetime
# Create your models here.

class Candidate(models.Model):
    resume = models.CharField(max_length=3)
    name = models.CharField(max_length=30)
    mobile = models.IntegerField(max_length=10)
    email = models.CharField(max_length=30)
    work_experience = models.CharField(max_length=10)
    analytics_exp = models.CharField(max_length=10)
    current_location = models.CharField(max_length=10)
    corrected_location = models.CharField(max_length=10)
    nearest_city = models.CharField(max_length=10)
    prefered_location = models.CharField(max_length=10)
    ctc = models.CharField(max_length=10)
    current_employer = models.CharField(max_length=20)
    current_designation = models.CharField(max_length=30)
    skill = models.CharField(max_length=50)
    ug_cource = models.CharField(max_length=10)
    ug_institute = models.CharField(max_length=20)
    trier1 = models.CharField(max_length=10)
    ug_passing_year = models.CharField(max_length=10)
    pg_cource = models.CharField(max_length=10)
    pg_institute = models.CharField(max_length=20)
    trier1 = models.CharField(max_length=10)
    pg_passing_year = models.CharField(max_length=10)
    post_pg_cource = models.CharField(max_length=10)
    correct_post_pg = models.CharField(max_length=10)
    
    def __str__(self):             
        return self.name



class Downloaddetail(models.Model):
    user_id = models.CharField(max_length=3)
    total_downloads = models.IntegerField(max_length=2,default=0)
    date = models.DateField(default=datetime.date.today)