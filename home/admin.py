from django.contrib import admin

from .models import signup,ContactsInformations,DietForm

class signupService(admin.ModelAdmin):
        list_display=('username','mobile_no','email','password')
class ContactService(admin.ModelAdmin):
                    list_display=('name','email','message')

class DietFormService(admin.ModelAdmin):
        list_display=('name','gender','age','bmi','diseases','foodType')

# Register your models here.
admin.site.register(signup,signupService)
# admin.site.register(contactEnquiry,ContactService)
admin.site.register(ContactsInformations,ContactService)

admin.site.register(DietForm,DietFormService)
