from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Acronym, Suggestions, Users

class AcronymModelTestCase(TestCase):
    def setUp(self):
        self.acronym1 = Acronym.objects.create(acronym_name='HTTP', full_form='Hypertext Transfer Protocol', description='A protocol for transferring data over the web', location='USA', phone_number='1234567890', email='http@example.com', website='http://www.example.com')
        self.acronym2 = Acronym.objects.create(acronym_name='API', full_form='Application Programming Interface', description='A set of protocols and tools for building software applications', location='Canada', phone_number='7987654321', email='api@example.com', website='http://www.example.com')
    
    def test_acronym_name(self):
        self.assertEqual(str(self.acronym1), 'HTTP - Hypertext Transfer Protocol')
        self.assertEqual(str(self.acronym2), 'API - Application Programming Interface')
    
    def test_acronym_full_form(self):
        self.assertEqual(self.acronym1.full_form, 'Hypertext Transfer Protocol')
        self.assertEqual(self.acronym2.full_form, 'Application Programming Interface')
    
    def test_acronym_description(self):
        self.assertEqual(self.acronym1.description, 'A protocol for transferring data over the web')
        self.assertEqual(self.acronym2.description, 'A set of protocols and tools for building software applications')
    
    def test_acronym_location(self):
        self.assertEqual(self.acronym1.location, 'USA')
        self.assertEqual(self.acronym2.location, 'Canada')
    
    def test_acronym_phone_number(self):
        self.assertEqual(self.acronym1.phone_number, '1234567890')
        self.assertEqual(self.acronym2.phone_number, '7987654321')
    
    def test_acronym_email(self):
        self.assertEqual(self.acronym1.email, 'http@example.com')
        self.assertEqual(self.acronym2.email, 'api@example.com')
    
    def test_acronym_website(self):
        self.assertEqual(self.acronym1.website, 'http://www.example.com')
        self.assertEqual(self.acronym2.website, 'http://www.example.com')
    
    def test_acronym_created_on(self):
        self.assertIsNotNone(self.acronym1.created_on)
        self.assertIsNotNone(self.acronym2.created_on)

class UsersModelTestCase(TestCase):
    def setUp(self):
        self.user1 = Users.objects.create(user_name='user1', user_type='admin', email='user1@example.com', password='password1')
        self.user2 = Users.objects.create(user_name='user2', user_type='user', email='user2@example.com', password='password2')
    
    def test_user_user_name(self):
        self.assertEqual(self.user1.user_name, 'user1')
        self.assertEqual(self.user2.user_name, 'user2')
    
    def test_user_user_type(self):
        self.assertEqual(self.user1.user_type, 'admin')
        self.assertEqual(self.user2.user_type, 'user')
    
    def test_user_email(self):
        self.assertEqual(self.user1.email, 'user1@example.com')
        self.assertEqual(self.user2.email, 'user2@example.com')
    
    def test_user_password(self):
        self.assertEqual(self.user1.password, 'password1')
        self.assertEqual(self.user2.password, 'password2')

class SuggestionsModelTestCase(TestCase):
    def setUp(self):
        self.suggestion1 = Suggestions.objects.create(acronym_name='HTTP', full_form='Hypertext Transfer Protocol', description='A protocol for transferring data over the web', location='USA', phone_number=1234567890, email='http@example.com', website='http://www.example.com', suggested_by_name='user1', suggested_by_email='user1@example.com', status='approved')
        self.suggestion2 = Suggestions.objects.create(acronym_name='API', full_form='Application Programming Interface', description='A set of protocols and tools for building software applications', location='Canada', phone_number=9876543218, email='api@example.com', website='http://www.example.com', suggested_by_name='user2', suggested_by_email='user2@example.com', status='rejected')
    
    def test_suggestion_acronym_name(self):
        self.assertEqual(self.suggestion1.acronym_name, 'HTTP')
        self.assertEqual(self.suggestion2.acronym_name, 'API')
    
    def test_suggestion_full_form(self):
        self.assertEqual(self.suggestion1.full_form, 'Hypertext Transfer Protocol')
        self.assertEqual(self.suggestion2.full_form, 'Application Programming Interface')
    
    def test_suggestion_description(self):
        self.assertEqual(self.suggestion1.description, 'A protocol for transferring data over the web')
        self.assertEqual(self.suggestion2.description, 'A set of protocols and tools for building software applications')
    
    def test_suggestion_location(self):
        self.assertEqual(self.suggestion1.location, 'USA')
        self.assertEqual(self.suggestion2.location, 'Canada')
    
    def test_suggestion_phone_number(self):
        self.assertEqual(self.suggestion1.phone_number, 1234567890)
        self.assertEqual(self.suggestion2.phone_number, 9876543218)
    
    def test_suggestion_email(self):
        self.assertEqual(self.suggestion1.email, 'http@example.com')
        self.assertEqual(self.suggestion2.email, 'api@example.com')
    
    def test_suggestion_website(self):
        self.assertEqual(self.suggestion1.website, 'http://www.example.com')
        self.assertEqual(self.suggestion2.website, 'http://www.example.com')
    
    def test_suggestion_suggested_by_name(self):
        self.assertEqual(self.suggestion1.suggested_by_name, 'user1')
        self.assertEqual(self.suggestion2.suggested_by_name, 'user2')
    
    def test_suggestion_suggested_by_email(self):
        self.assertEqual(self.suggestion1.suggested_by_email, 'user1@example.com')
        self.assertEqual(self.suggestion2.suggested_by_email, 'user2@example.com')
    
    def test_suggestion_status(self):
        self.assertEqual(self.suggestion1.status, 'approved')
        self.assertEqual(self.suggestion2.status, 'rejected')



# class UserSignupTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.signup_url = reverse('user_signup')
#         self.valid_payload = {
#             'user_name': 'testuser',
#             'email': 'testuser@example.com',
#             'password': 'testpassword',
#             'user_type': 'customer'
#         }
#         self.invalid_payload = {
#             'user_name': '',
#             'email': '',
#             'password': '',
#             'user_type': ''
#         }

#     def test_valid_signup(self):
#         response = self.client.post(
#             self.signup_url,
#             data=self.valid_payload,
#             format='json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Users.objects.count(), 1)
#         self.assertEqual(Users.objects.get().user_name, 'testuser')

#     def test_invalid_signup(self):
#         response = self.client.post(
#             self.signup_url,
#             data=self.invalid_payload,
#             format='json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)