from django.db import models

# Create your models here.
# STATUS = (
#     (0,"Draft"),
#     (1,"Publish")
# )

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(get_user_model())
    created_on = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField()