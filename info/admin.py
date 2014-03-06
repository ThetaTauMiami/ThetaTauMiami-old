from django.contrib import admin

from info.models import PledgeClass, Brother, Department, Major, HasMajor, Officer, HeldPosition, Position

# Register your models here.

admin.site.register(Brother)
admin.site.register(PledgeClass)
admin.site.register(Department)
admin.site.register(Major)
admin.site.register(HasMajor)
admin.site.register(Officer)
admin.site.register(HeldPosition)
admin.site.register(Position)