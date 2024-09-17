# Django Model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

class MyModel(models.Model):
    name = models.CharField(max_length=255)


@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    print(f"Signal started for {instance.name}")
    time.sleep(5) 
    print(f"Signal finished for {instance.name}")

# Django View
from myapp.models import MyModel

print("Creating a new MyModel instance...")
my_model_instance = MyModel.objects.create(name="Test")
print("Instance creation finished.")


