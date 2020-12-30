from django.contrib import admin
from .models import *

admin.site.register(CowType)
admin.site.register(Cow)
admin.site.register(CowMilking)
admin.site.register(CowMilkSale)
admin.site.register(CowPregnancy)