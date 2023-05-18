from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Point
from .serializers import PointSerializer
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

import math

@csrf_exempt
class AjaxLoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login the authenticated user
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)

    def dispatch(self, request, *args, **kwargs):
        if not request.method == 'POST':
            return JsonResponse({'message': 'Invalid request method'}, status=400)
        return super().dispatch(request, *args, **kwargs)


class ClosestPointsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    
    def post(self, request):
        points_str = request.data.get('points')
        if not points_str:
            return Response({'error': 'Points not provided'}, status=status.HTTP_400_BAD_REQUEST)

        points = points_str.split(';')
        points_list = []
        for point in points:
            try:
                x, y = map(int, point.split(','))
                points_list.append((x, y))
            except ValueError:
                return Response({'error': f'Invalid point format: {point}'}, status=status.HTTP_400_BAD_REQUEST)

        closest_points = self.find_closest_points(points_list)
        # Create the Point object
        all_points = ';'.join(points)
        closest_points_str = ';'.join(closest_points)

        point = Point( all_points=all_points, closest_points=closest_points_str)
        point.save()

        serializer = PointSerializer(point)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get (self, request):
        points = Point.objects.all().order_by('-id')
        data = []
        for point in points:
            data.append({
                'id': point.id,
                'all_points': point.all_points,
                'closest_points': point.closest_points,
            })
        return Response(data, status=status.HTTP_200_OK)
    def find_closest_points(self, points_list):
        closest_points = []
        # Iterate over each point in the list
        for i in range(len(points_list)):
            x1, y1 = points_list[i]
            closest_point = None
            closest_distance = math.inf
            # Compare the current point with all other points
            for j in range(len(points_list)):
                if i != j:
                    x2, y2 = points_list[j]
                    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                    # Update the closest point if a smaller distance is found
                    if distance < closest_distance:
                        closest_distance = distance
                        closest_point = (x2, y2)

            # If a closest point was found, add it to the list
            if closest_point is not None:
                closest_points.append(closest_point)
        #cleanup the list
        # remove duplicates
        closest_points = list(set(closest_points))
        #flip the list
        closest_points = closest_points[::-1]
        # convert it to a string like 'x1,y1;x2,y2;x3,y3'
        closest_points = [f'{x},{y}' for x, y in closest_points]
        return closest_points