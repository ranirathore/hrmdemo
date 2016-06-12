from django.contrib import admin

# Register your models here.
from .models import Candidate,Downloaddetail

admin.site.register(Candidate)
admin.site.register(Downloaddetail)

