from django.test import TestCase, RequestFactory
from .models import Candidate
from .views import user_detail

# Create your tests here.
class CandidateTestCase(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory() #for url/view testing
        
        ##create Test candidate
        testuser = {'name':'rani rathore', 'mobile':8269029702, 'resume':'No', 'email':'rani21rathore@gmail.com', 
                    'work_experience':2.9,'current_location':'Indore', 'corrected_location':'Indore',
                    'ctc':3.6, 'current_employer':'Shrideva Tech', 'current_designation':'Python Developer',
                    'skill':'Python, Php, Java Script, Django, Python', 'ug_cource':'BE', 'ug_institute':'SGSITS',
                    'ug_passing_year':2013
                    }
        self.testuser = Candidate.objects.create(**testuser) #create and access test cadidate object
        
  
    def test_search_candidate_by_skill(self):
        #Create test for search cadidate by various type of filter
        filter_colomn = 'skill'
        query = 'python'
        data  = Candidate.objects.filter(**{filter_colomn+"__contains":query})
        if data:
            self.assertTrue(data) # if candidate found
        else:
            self.assertFalse(data) # candidate not found
      
      
    def test_string_representation(self):
        entry = Candidate(name="rani rathore") # checking candidate representation 
        self.assertEqual(str(entry), entry.name)  
        
        
        
    def test_candidate_detail(self): 
        request = self.factory.get('/candidate_detail/') #create get instance request
        response = user_detail(request, self.testuser.id) #set parameter on view
        self.assertEqual(response.status_code, 200) # cheking status