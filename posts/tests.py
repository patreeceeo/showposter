from django.test import TestCase
from posts.utils import get_slug
from posts.models import Post

class PostModelTestCase(TestCase):
    def test_slug(self):
        """should auto assign unique slug"""
        post = Post.objects.create(
                date_of_show='2066-06-06',
                alternate_text='woohoo!'
        )
        self.assertIsNot(post.slug, '');
        self.assertTrue(type(post.slug) is str);

