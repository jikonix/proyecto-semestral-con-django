from django.db import models
import datetime
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.

class Comidas(models.Model):
    item= models.CharField(max_length=20, unique=True, null=False, default=None) 
    precio= models.PositiveIntegerField(null=False, default=None)
    agregado= models.BooleanField(null=False, default=False)
    fecha_ingreso= models.DateField(default=datetime.date.today(), null=False)
    imagen = models.ImageField(null=True)
    slug= models.SlugField(null=False, unique=True, default=None)

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.item}-{self.fecha_ingreso}")
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("item", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.item
    


