from django.db import models

class Topic(models.Model):
    """ the topic a user is learning about """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

class Entry(models.Model):
    """ something specific learned about the topic """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """ return a string represeantion of the model """
        return f"{self.text[:50]}..."