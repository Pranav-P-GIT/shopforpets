from django.db import models
from home.models import PetProduct

# Create your models here.
class comment(models.Model):
    pro=models.ForeignKey(PetProduct,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    cmt=models.TextField()
    date=models.DateTimeField(auto_now_add=True)


