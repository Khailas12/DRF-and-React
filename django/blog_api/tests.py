from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from blog.models import Category, Post
from django.contrib.auth.models import User


class PostTests(APITestCase):

    def test_view_posts(self):
        url = reverse('blog_api:listcreate')    # fetch info from blog_api urls.
        response = self.client.get(url, format='json')  # status code 200 is expected.
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    
    def test_create_post(self):
        self.test_category = Category.objects.create(name='main')
        
        self.test_user1 = User.objects.create_user(
            username='test_user_1', password='123456789'
        )
        
        data = {
            "title": "new",
            "author": 1,
            "excerpt": "new",
            "content": "new",
        }
        
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_post_update(self):
        client = APIClient()
        
        self.test_category = Category.objects.create(name='main')
        self.test_user1 = User.objects.create_user(
            username='test_user1', password='123456789'
        )
        self.test_user2 = User.objects.create_user(
            username='test_user2', password='test1234'
        )
        
        test_post = Post.objects.create(
            category_id=1,
            title='hello world',
            excerpt='Post Excerpt',
            content='Gotham is great',
            slug='some-title',
            author_id=1,
            status='published',
        )
        
        client.login(
            username=self.test_user1.username, password='123456789'
        )
        
        url = reverse(
            ('blog_api:detailcreate'), kwargs={'pk': 1}
        )
        
        response = client.put(
            url,
            {
                "title": "New",
                "author": 1,
                "excerpt": "New",
                "content": "New",
                "status": "published"
            }, 
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)