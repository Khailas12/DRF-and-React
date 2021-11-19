from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


class TestCreatePost(TestCase):
    
    @classmethod
    def setup_test_data(cls):
        test_category = Category.objects.create(name='initial')
        test_user_1 = User.objects.create_user(
            username='user_1', password='12345678'
        )
        test_user_1.save()
        
        test_post = Post.objects.create(
            category_id=1,
            title='hello world',
            excerpt='post excerpt',
            content='con',
            slug='title',
            author_id=1,
            status='published'
        )
        test_post.save()
        
    def test_blog_content(self, *args, **kwargs):
        
        try:
            post = Post.post_objects.get(id=1)
            category = Category.objects.get(id=1)
        except Post and Category.DoesNotExist:
            post = None
            category = None

            author = f'{post.author}'
            excerpt = f'{post.excerpt}'
            title = f'{post.title}'
            content = f'{post.content}'
            status = f'{post.status}'
            
            
        # making sure that the data ensured is the actual data is inserted into the table
        self.assertEqual(author, 'user_1')
        self.assertEqual(title, 'hello world')
        self.assertEqual(content, 'con')
        self.assertEqual(status, 'published')
        
        self.assertEqual(str(post), 'hello world')
        self.assertEqual(str(category), 'initial')