from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_on']  # Orders posts by creation date, newest first

    def get_absolute_url(self):
        """Returns the URL to access a particular post instance."""
        return reverse('blog_post_detail', args=[self.slug])

    def __str__(self):
        """String representation of the Post object."""
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']  # Orders comments by creation date, oldest first

    def __str__(self):
        """String representation of the Comment object."""
        return f'Comment by {self.name} on {self.post}'

from django.db import models
from django.urls import reverse

# class FAQ(models.Model):
    # question = models.TextField()
    # answer = models.TextField()
    # created_on = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ['-created_on']  # Orders FAQs by creation date, newest first

    # def __str__(self):
    #     return self.question
    
    
    #Assessment work*

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField(blank=True, null=True)  # WYSIWYG editor support
    question_hi = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def get_translated_text(self, lang='en'):
        """Retrieve translated question and answer based on the specified language."""
        if lang == 'hi':
            return {
                'question': self.question_hi or self.question,
                'answer': self.answer_hi or self.answer,
            }
        elif lang == 'bn':
            return {
                'question': self.question_bn or self.question,
                'answer': self.answer_bn or self.answer,
            }
        return {
            'question': self.question,
            'answer': self.answer,
        }