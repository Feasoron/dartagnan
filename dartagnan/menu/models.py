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
    isOnSale = models.BooleanField()
    salePrice = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Hours(models.Model):
    isOpen = models.BooleanField()
    open = models.TimeField(null=True)
    closed = models.TimeField(null=True)


class Address(models.Model):
    class Meta:
        verbose_name_plural = "addresses"
    streetAddress = models.CharField()
    city = models.CharField()
    state = models.CharField(max_lenght=2)
    zipCode = models.CharField(max_length=10)
    restaurant = models.ForeignKey(RestaurantInfo)

    def __unicode__(self):
        return self.streetAddress + ' ' + self.city + ', ' + self.state + ' ' + self.zipCode


class RestaurantInfo(models.Model):
    name = models.CharField(max_length=100)
    aboutUs = models.CharField()
    founded = models.DateField()


    def __unicode__(self):
        return self.name


