from django.test import TestCase
from posts.utils import get_slug
from posts.models import Post

class PostModelTestCase(TestCase):
    def test_slug(self):
        """should auto assign slug based on number of existing posts"""
        post = Post.objects.create(
                end_date='2066-06-06',
                alternate_text='woohoo!'
        )
        print('slug=%s' % post.slug)
        self.assertIsNot(post.slug, '');
        self.assertTrue(type(post.slug) is str);

