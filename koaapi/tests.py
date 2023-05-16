from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Point
from .serializers import PointSerializer

class ClosestPointsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    # def test_closest_points_api_valid_input(self):
    #     url = reverse('closest-points')
    #     data = '2,2;-1,30;20,11;4,5'

    #     response = self.client.post(url, {'points': data}, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #     expected_result = '2,2;4,5'
    #     self.assertEqual(response.data['closest_points'], expected_result)

    #     # Verify that the points are saved in the database
    #     self.assertEqual(Point.objects.count(), 4)
    def test_closest_points_api_valid_input(self):
        url = reverse('closest-points')
        data = {'points': '2,2;-1,30;20,11;4,5'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        point = Point.objects.last()
        serializer = PointSerializer(point)
        expected_data = {
                'id': 1,
                'all_points': '2,2;-1,30;20,11;4,5',
                'closest_points': '2,2;4,5'
            }

        self.assertEqual(response.data, expected_data)


    def test_closest_points_api_invalid_input(self):
        url = reverse('closest-points')
        data = '2,2;-1,30;20'  # Missing one point

        response = self.client.post(url, {'points': data}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Verify that the points are not saved in the database
        self.assertEqual(Point.objects.count(), 0)
