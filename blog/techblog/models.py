from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    #TODO: Make sure the passwords are hashed
    password = models.CharField(max_length=64)
    email_address = models.CharField(max_length=200)

class Author(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    description = models.TextField()

    #avatar_name: path to image
    avatar = models.CharField(max_length=200, null=True)
    email_address = models.CharField(max_length=200)

    class Meta:
        ordering = ["first_name"]
    
    def __str__(self):
        return "FName:{}, LName {}".format(self.first_name, self.last_name)

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.title = models.CharField(max_length=64)
    slug_field = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField()
    publish_status = models.BooleanField(default=False)
    publish_date = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        ordering = ["publish_date"]

    def __str__(self):
        return "{} {} \n{}".format(self.title, self.content, self.publish_status)

    def publish(self):
        self.publish_date = timezone.now()
        self.publish_status = True

        self.save
    
    def generate_slug_field(self):
        if self.title:
            title = self.title
        else: 
            return

        slug = title.lower().replace(" ", "_")
        self.slug_field = slug

        self.save()

class Comment(models.Model):
    comment_post_ID = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_date = models.DateTimeField()
    comment_content = models.TextField()

class Like(models.Model):
    like_IP = models.CharField(max_length = 20)
    liked_post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    liked_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
class Tag(models.Model):
    tag_name = models.CharField(max_length= 15)
    post_taged = models.ForeignKey(Post, on_delete=models.CASCADE)
