from django.db import models
from django.core.exceptions import ValidationError
import datetime
# Create your models here.


class Candidate(models.Model):
    yearrange =  [(i, i) for i in reversed(range(1950,datetime.datetime.today().year+1))]
    resume = models.CharField(max_length=3, choices = [('yes', 'Yes'), ('no', 'No')], default = 'yes')
    name = models.CharField(max_length=30)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    work_experience = models.FloatField(default=1.0)
    analytics_exp = models.FloatField(blank=True,default=0.0)
    current_location = models.CharField(max_length=30, )
    corrected_location = models.CharField(max_length=30, )
    nearest_city = models.CharField(max_length=30, blank = True)
    prefered_location = models.CharField(max_length=10, blank = True)
    ctc = models.FloatField(blank=True,default=0.0)
    current_employer = models.CharField(max_length=50)
    current_designation = models.CharField(max_length=100)
    skill = models.TextField()
    ug_cource = models.CharField(max_length=20)
    ug_institute = models.CharField(max_length=30)
    trier1 = models.CharField(max_length=5,blank = True)
    ug_passing_year = models.IntegerField(max_length=4,choices = yearrange, default = yearrange[0])
    pg_cource = models.CharField(max_length=10,blank = True)
    pg_institute = models.CharField(max_length=30,blank = True)
    trier1 = models.CharField(max_length=10,blank = True)
    pg_passing_year = models.CharField(max_length=4, choices = yearrange, blank = True)
    post_pg_cource = models.CharField(max_length=20,blank = True)
    correct_post_pg = models.CharField(max_length=20,blank = True)
    
    def __str__(self):             
        return self.name
    
    
    
    



class Downloaddetail(models.Model):
    user_id = models.CharField(max_length=3)
    total_downloads = models.IntegerField(max_length=2,default=0)
    date = models.DateField(default=datetime.date.today)
