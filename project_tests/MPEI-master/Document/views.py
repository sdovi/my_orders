from django.shortcuts import render


# Create your views here.


def Document_data(request):
    text = {
        "txt": 1,
        "txt2": "adsas",

    }
    return render(request, 'DocumentData.html', {"speak": text})
