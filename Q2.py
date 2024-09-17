# models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading

class MyModel(models.Model):
    name = models.CharField(max_length=255)
  
@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()} for {instance.name}")

# views.py
from myapp.models import MyModel
import threading

print(f"Caller thread ID: {threading.get_ident()}")

my_model_instance = MyModel.objects.create(name="Test")
