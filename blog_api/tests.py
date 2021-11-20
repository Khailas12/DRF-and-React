from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User


class PostTests(APITestCase):
    
    def test_view_case(self):
        url = reverse('blog_api:listcreate')    # fetch info from blog_api urls.
        response = self.client.get(url, format='json')  # ststus code 200 is expected.
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        