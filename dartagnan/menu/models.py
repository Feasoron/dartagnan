from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name
