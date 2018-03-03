from django.db import models

# Create your models here.
class item_type(models.Model):
    title = models.CharField(max_length=255)
    pid = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    sort = models.IntegerField(default=0)
    top = models.IntegerField(default=0)
    icon = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    ascription_type = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'items'
        ordering = ['-id']