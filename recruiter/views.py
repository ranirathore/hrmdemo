from .models import Candidate,Downloaddetail
import csv
from django.contrib import auth
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.

#Home page, show after recruiter login 
def home(request):
    ###################
    total_entry = Downloaddetail.objects.filter(date = datetime.date.today,user_id = request.user.id)
    total_downloads =  len(total_entry)
    ##################
    filter_colomn = ""
    query = ""
    fiterlist = [('current_location', 'Location'),
        ('nearest_city', 'City'),
        ('skill', 'Skill'),
        ('current_designation', 'Designation'),
        ('ug_cource', 'U.G. Course'),
        ('ctc', 'CTC'),]
    data = Candidate.objects.all()
    if request.method == 'POST':
        filter_colomn = request.POST['filter_colomn']
        query = request.POST['key_name']
        if  filter_colomn and query:
            data  = Candidate.objects.filter(**{filter_colomn+"__contains":query})
       
        if 'csv_genrate' in request.POST:
            
            if total_downloads > 9:  
                pass
                return HttpResponseRedirect('/home')
            else:
                ####
                d = Downloaddetail(user_id = request.user.id)
                d.save()
                ####
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename=search_candidate.csv'

                writer = csv.writer(response)
                writer.writerow( [ (field.get_attname_column()[0].capitalize() ) for field in Candidate._meta.fields ])
                for res in data:
                    writer.writerow(
                        [getattr(res, field.get_attname_column()[0]) for field in Candidate._meta.fields ]
                    )
                return response
            
    return render(request, 'recruiter/home.html', {'data':data, 'query':query, 'filter_colomn': filter_colomn, 'fiterlist':fiterlist,'total_downloads':total_downloads})

# For recruiter login
def user_login(request):
    msg = ''
    username = password = ''
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
       
        if user:
            if user.is_active and user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/home')
            else:
                msg = "User Disabled"
        else:
            msg = "Password Does Not Match"
   
  
    return render(request, 'recruiter/login.html', {'msg':msg})

#For recruiter logout
def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/') 

#For candidate detail
def user_detail(request,user_id):
    user_detail = Candidate.objects.get(pk=user_id)
    data =  [(field.get_attname_column()[0],getattr(user_detail, field.get_attname_column()[0])) for field in Candidate._meta.fields ]
    return render(request, 'recruiter/user_detail.html',{'data':data})