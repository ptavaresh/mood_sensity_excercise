from django.contrib import admin
from .models import Picture


class PictureAdmin(admin.ModelAdmin):
    list_display = ['picture',
                    'latitude',
                    'longitude',
                    'timestamp',
                    'mood'
    ]


admin.site.register(Picture, PictureAdmin)