from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
from .models import Point

class ClosestPointsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.access_token = AccessToken.for_user(self.user)
         # Create some sample Point objects for testing
        self.point1 = Point.objects.create(all_points='2,2;-1,30;20,11;4,5', closest_points='2,2;4,5')
        self.point2 = Point.objects.create(all_points='1,1;3,3;5,5', closest_points='1,1;3,3')
    
    def test_closest_points_api_invalid_input(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token))
        response = self.client.get('/api/closest-points/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        url = reverse('closest-points')
        data = '2,2;-1,30;20'  # Missing one point

        # response = self.client.post(url, {'points': data}, format='json')
        response = self.client.post('/api/closest-points/', {'points': data})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Verify that just the 2 points we created are saved in the database
        self.assertEqual(Point.objects.count(), 2)
        
     
    def test_closest_points_api_valid_input(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token))
        
        # Make a GET request to ensure the initial state of the API
        response = self.client.get('/api/closest-points/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        url = reverse('closest-points')
        data = {'points': '2,2;-1,30;20,11;4,5'}
        
        # Make a POST request to the API endpoint with the input data
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Define the expected data for the created object
        expected_data = {
            'id': response.data['id'],
            'all_points': '2,2;-1,30;20,11;4,5',
            'closest_points': '2,2;4,5'
            }
        
        # Compare relevant fields of the response data with the expected data
        self.assertEqual(response.data['id'], expected_data['id'])
        self.assertEqual(response.data['all_points'], expected_data['all_points'])
        self.assertEqual(response.data['closest_points'], expected_data['closest_points'])

      
    def test_get_points(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token))
        response = self.client.get('/api/closest-points/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Make a GET request to the endpoint
        response = self.client.get('/api/closest-points/')
        
        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Assert the response data contains the expected points
        expected_data = [
            {
                'id': self.point1.id,
                'all_points': '2,2;-1,30;20,11;4,5',
                'closest_points': '2,2;4,5',
            },
            {
                'id': self.point2.id,
                'all_points': '1,1;3,3;5,5',
                'closest_points': '1,1;3,3',
            }
        ]
        self.assertCountEqual(response.data, expected_data)
