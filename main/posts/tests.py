from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@gmail.com",
            password="secret",
        )
        
        cls.post = Post.objects.create(
            author=cls.user,
            title="A good title",
            body="Should I move into Samsung?",
        )
    
    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Should I move into Samsung?")
        self.assertEqual(str(self.post), "A good title")
