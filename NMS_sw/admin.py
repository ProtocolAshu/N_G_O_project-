from django.contrib import admin
from NMS_sw.models import Student, register_Donor, renewal, Donor_avail
from NMS_sw.models import totalmoney,inventory,estimations,exphist,expenditure,Admin
# Register your models here.

admin.site.register(Student)
admin.site.register(register_Donor)
admin.site.register(renewal)
admin.site.register(Donor_avail)
admin.site.register(totalmoney)
admin.site.register(inventory)
admin.site.register(estimations)
admin.site.register(expenditure)
admin.site.register(exphist)
admin.site.register(Admin)
