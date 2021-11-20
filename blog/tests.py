from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


class TestCreatePost(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='main')

        testuser1 = User.objects.create_user(
            username='test_user', password='123456789')
        testuser1.save()

        
        test_post = Post.objects.create(
            category_id=1,
            title='hello world',
            excerpt='Post Excerpt',
            content='Gotham is great',
            slug='some-title',
            author_id=1,
            status='published',
        )
        test_post.save()
        
    
    def test_blog_content(self):
        post = Post.post_objects.get(id=1)
        category = Category.objects.get(id=1)
        
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        
        self.assertEqual(author, 'test_user')
        self.assertEqual(excerpt, 'Post Excerpt')
        self.assertEqual(title, 'hello world')
        self.assertEqual(content, 'Gotham is great')
        self.assertEqual(status, 'published')
        
        self.assertEqual(str(post), 'hello world')
        self.assertEqual(str(category), 'main')