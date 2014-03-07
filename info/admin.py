from django.contrib import admin

from info.models import PledgeClass, Brother, Department, Major, Officer, HeldPosition, Position, Job, JobType

# Register your models here.

admin.site.register(Brother)
admin.site.register(PledgeClass)
admin.site.register(Department)
admin.site.register(Major)
admin.site.register(Officer)
admin.site.register(HeldPosition)
admin.site.register(Position)
admin.site.register(Job)
admin.site.register(JobType)