from django.contrib import admin
from .models import Person, Country, State, City, Town

admin.site.register(Person)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Town)
