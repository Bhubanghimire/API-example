from django.contrib import admin
from .models import Vote,Poll,Choice

# Register your models here.
admin.site.register(Vote)
admin.site.register(Poll)
admin.site.register(Choice)