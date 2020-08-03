from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Person"


class Country(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    population = models.IntegerField(default=0)
    gdp = models.FloatField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"
        unique_together = ('name',)


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    population = models.IntegerField(default=0)
    gdp = models.FloatField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "States"
        unique_together = ('country', 'name',)


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    population = models.IntegerField(default=0)
    gdp = models.FloatField(default=0)
    pin_code = models.CharField(max_length=25)

    def __str__(self):
        return self.pin_code

    class Meta:
        verbose_name_plural = "Cities"


class Town(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    population = models.IntegerField(default=0)
    gdp = models.FloatField(default=0)
    pin_code = models.CharField(max_length=25)

    def __str__(self):
        return self.pin_code

    class Meta:
        verbose_name_plural = "Town"
