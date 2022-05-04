from django.contrib import admin
from AppTwo.models import Topic, Webpage, AccessRecord, UserProfileInfo

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
# admin.site.register(User)
admin.site.register(UserProfileInfo)