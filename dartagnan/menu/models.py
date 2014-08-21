from django.db import models
import datetime


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


class RestaurantInfo(models.Model):
    name = models.CharField(max_length=100)
    aboutUs = models.TextField(max_length=10000)
    founded = models.DateField()

    def __unicode__(self):
        return self.name


class Location(models.Model):
    class Meta:
        verbose_name_plural = "addresses"

    streetAddress = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipCode = models.CharField(max_length=10)
    restaurant = models.ForeignKey(RestaurantInfo)

    monday_opens_at = models.TimeField(null=True, blank=True)
    monday_closes_at = models.TimeField(null=True, blank=True)

    tuesday_opens_at = models.TimeField(null=True, blank=True)
    tuesday_closes_at = models.TimeField(null=True, blank=True)

    wednesday_opens_at = models.TimeField(null=True, blank=True)
    wednesday_closes_at = models.TimeField(null=True, blank=True)

    thursday_opens_at = models.TimeField(null=True, blank=True)
    thursday_closes_at = models.TimeField(null=True, blank=True)

    friday_opens_at = models.TimeField(null=True, blank=True)
    friday_closes_at = models.TimeField(null=True, blank=True)

    saturday_opens_at = models.TimeField(null=True, blank=True)
    saturday_closes_at = models.TimeField(null=True, blank=True)

    sunday_opens_at = models.TimeField(null=True, blank=True)
    sunday_closes_at = models.TimeField(null=True, blank=True)

    def is_open_at(self, day_to_check, time_of_day):

        hours_for_today = self.openDays.first(name=day_to_check).hours

        return hours_for_today.open <= time_of_day <= hours_for_today.closed

    def __unicode__(self):
        return self.streetAddress + ' ' + self.city + ', ' + self.state + ' ' + self.zipCode




