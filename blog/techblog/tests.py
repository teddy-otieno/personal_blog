from django.test import TestCase
from django.utils import timezone
from .models import *
# Create your tests here.

class PostsTests(TestCase):

    def setUp(self):
        self.dummy_user = User.objects.create(
                username = "Foo",
                password = "Bar",
                email_address = "bar@foo.com"
                )

        self.dummy_author = Author.objects.create(
                first_name = "Foo",
                last_name = "Bar",
                description = "Foo went to a Bar and bought a beer",
                email_address=  "foo@bar.com"
                )

        self.dummy_post = Post.objects.create(
                author = self.dummy_author,
                title = "Foo went to a Bar",
                content = "Foo went to a Bar and bought a beer",
                publish_status = False,
                publish_date = timezone.now()
                ) 

        self.dummy_comment = Comment.objects.create(
                comment_post_ID = self.dummy_post,
                comment_author = self.dummy_user,
                comment_date = timezone.now(),
                comment_content = "Hello I am Foo, and i didnt go to the bar last night",
                )

        self.dummy_post_like = Like.objects.create(
                like_IP = "127.0.0.1",
                liked_post = self.dummy_post
                )

        self.dummy_comment_like = Like.objects.create(
                like_IP = "127.0.0.1",
                liked_comment = self.dummy_comment,
                )

        self.dummy_tag = Tag.objects.create(
                tag_name = "Foo",
                post_taged = self.dummy_post,
                )

        self.dummy_tag_2 = Tag.objects.create(
                tag_name = "Bar",
                post_taged = self.dummy_post,
                )


    def test_post_publication(self):
        """
            Test if publication method works
        """
        self.dummy_post.publish()
        self.assertTrue(self.dummy_post.publish_status)

    def test_post_author(self):
        """
            Test Author
        """
        self.assertEqual(self.dummy_post.author, self.dummy_author)

    def test_slug_field_generation(self):
        """
            Test generation of the slug field, useful with urls
        """
        self.dummy_post.generate_slug_field()
        self.assertEqual(self.dummy_post.slug_field,"foo_went_to_a_bar" )
