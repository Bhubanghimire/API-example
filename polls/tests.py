from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from polls import Apiviews
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.contrib.auth.models import User


#useing apirequestfactory
class TestPoll(APITestCase):
    def setUp(self):
        # print("bhuban1")
        self.factory = APIRequestFactory()
        self.view = Apiviews.PollViewSet.as_view({'get': 'list'})
        self.uri = '/polls/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user("asdd",email="abc@gmail.com",password="asdfad")

    def test_list(self):
        request = self.factory.get(self.uri,HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200,'Expected Response Code 200, received {0} instead.'.format(response.status_code))

    # def test_Create(self):
    #     param = {'question':"who are you?",'created_by':'1'}
    #     request = self.factory.post('/vote/',param) #,HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
    #     print(request)
    #     request.user = self.user
    #     response = self.view(request,param)
    #     print(response)
    #     # self.assertEqual(response.status_code, 201,'Expected Response Code 201, received {0} instead.'.format(response.status_code))


        
#using apiclient 
class TestPolls(APITestCase):
    def setUp(self):
        print("bhuban 2")
        self.client = APIClient()
        self.uri = '/polls/'
        user = User.objects.create_user(username="bhuban",is_staff=True,password="pass")
        self.client.login(username="bhuban", password="pass")


  
    def test_list(self):
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,'Expected Response Code 200, received {0} instead.'.format(response.status_code))

       
    def test_create(self):
        param = {'question':"who are you?",'created_by':'1'}
        response = self.client.post(self.uri,param)
        self.assertEqual(response.status_code, 201,'Expected Response Code 201, received {0} instead.'.format(response.status_code))