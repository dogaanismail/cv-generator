from django.test import TestCase, Client
from django.urls import reverse
import json
from .models import CV_data, Interests, Education, WorkExperience, Skills


class CVGenTestCase(TestCase):

    def setUp(self):
        self.client = Client()

        # Add mock data (users, skills, interests, education, work experience etc.) to your database here
        # This data will be used during the tests
        # Here is one example how to add a CV_data instance

        CV_data.objects.create(first_name="TestFirstName", last_name="TestLastName",
                               email="testemail@gmail.com", phone="1234567890",
                               about_yourself="This is a test")

    def test_index(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CV_gen/index.html')

    def test_cv_list(self):
        response = self.client.get(reverse('cv_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CV_gen/list.html')

    def test_cv_download(self):
        # Assuming there is a CV_data instance available
        cv_data = CV_data.objects.first()
        response = self.client.get(reverse('cv_download', kwargs={'num': cv_data.id, 'template': 'some_template'}))

        self.assertEqual(response.status_code, 200)

    def test_submit_POST(self):
        data = {
            "data": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john_doe@gmail.com",
                "phone": "123456789",
                "aboutYourself": "Testing...",
                "university": ["Test University"],
                "degree": ["BsCS"],
                "gpa": ["3.0"],
                "jobTitle": ["Engineer"],
                "companyName": ["Test Company"],
                "startDate": ["2000-01-01"],
                "endDate": ["2005-01-01"],
                "otherInformation": ["Test info"],
                "skills": ["Programming"],
                "interest": ["Reading"]
            }
        }

        response = self.client.post(reverse('submit'),
                                    data=json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'status': 'sucess', 'message': 'Good Job'})

    def test_submit_not_POST(self):
        response = self.client.get(reverse('submit'))

        self.assertEqual(response.status_code, 405)
        self.assertJSONEqual(response.content, {'status': 'error', 'message': 'Invalid request method'})
