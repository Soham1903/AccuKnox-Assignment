# models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from django.core.exceptions import ValidationError

class MyModel(models.Model):
    name = models.CharField(max_length=255)

class RelatedModel(models.Model):
    my_model = models.ForeignKey(MyModel, on_delete=models.CASCADE)
    related_data = models.CharField(max_length=255)

# Signal handler to create a related model instance
@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    print("Signal handler triggered: Creating RelatedModel")
    RelatedModel.objects.create(my_model=instance, related_data="Related to " + instance.name)

# views.py
from django.db import transaction
from myapp.models import MyModel, RelatedModel


try:
    with transaction.atomic():
        print("Creating MyModel instance...")
        my_model_instance = MyModel.objects.create(name="Test")
        
       
        raise ValidationError("Forcing a rollback")
except ValidationError:
    print("Transaction rolled back due to error.")


print("MyModel count:", MyModel.objects.count()) 
print("RelatedModel count:", RelatedModel.objects.count())
