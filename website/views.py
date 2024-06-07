from django.shortcuts import render
from website.models import Qrcode


def home_view(request):
    name = 'Welcom to Qrcode production site!'

    obj = Qrcode.objects.get(id=1)

    context = {
        'name': name,
        'obj': obj,
    }

    return render(request, 'qr_code/index.html', context)

