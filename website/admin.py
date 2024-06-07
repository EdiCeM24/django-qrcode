from django.contrib import admin
from .models import Qrcode


class QrcodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'qr_code')



admin.site.register(Qrcode, QrcodeAdmin)

