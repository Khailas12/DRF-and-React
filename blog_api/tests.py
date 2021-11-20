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
        
        
    def create_post(self):
        self.test_category = Category.objects.create(name='main')
        
        self.test_user1 = User.objects.create_user(
            username='test_user_1', password='1235456'
        )
        
        data = {
            "title": "new",
            "author": 1,
            "excerpt": "new",
            "content": "new"
        }
        
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)