from django.db import models

# Create your models here.
class Test(models.Model):
    """
    Test Model 
    """

    class Meta:
        verbose_name_plural = "Test"

    name = models.CharField(max_length=254)
    
    def __str__(self):
        return self.name