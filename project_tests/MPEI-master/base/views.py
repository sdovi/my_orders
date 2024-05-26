from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseBadRequest
from ads.models import Ads
from news.models import News
from about_university.models import QabulLink
from django.db.models import Q
from science_and_innovation.models import ScientEvents

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

# def custom_error_view(request, exception=None):
#     return render(request, "500.html", status=500)

def index(request):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    introsection = IntroSection.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    qabullink = QabulLink.objects.first()
    news = News.objects.all()[::-1][:6]
    photo = carusel.objects.all()
    video1 = Video.objects.all()
    testimonials = Testimonials.objects.all()
    whychooseus = WhyChooseUs.objects.all().first()
    ads = Ads.objects.all()[::-1][:3]
    ad_odd = ads[1]
    context = {
        'qabullink': qabullink,
        'site_logo': site_logo,
        'introsection': introsection,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
        'ads': ads,
        'news': news,
        'ad_odd': ad_odd,
        'testimonials': testimonials,
        'whychooseus': whychooseus,
        "carusel": photo,
        "video": video1

    }
    return render(request, 'index.html', context=context)

def newsletterformview(request):
    if request.method == "POST":
        JoinOurNewsletterForm.objects.create(
            email=request.POST['email'],
        )
        return redirect('index')
    else:
        return HttpResponseBadRequest()

def receivedmessagesview(request):
    if request.method == "POST":
        ReceivedMessages.objects.create(
            email=request.POST['email'],
            message=request.POST['message'],
        )
        return redirect('index')
    else:
        return HttpResponseBadRequest()

def contact_view(request):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    qabullink = QabulLink.objects.first()
    if request.method == 'POST':
        ReceivedMessages.objects.create(
            email=request.POST['email'],
            phone_number=request.POST['phone_number'],
            message=request.POST['message'],
        )
        return redirect('contact')
    context = {
        'qabullink': qabullink,
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
    }
    return render(request, 'contact.html', context=context)

def faqs(request):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    qabullink = QabulLink.objects.first()

    query = FAQs.objects.all()

    context = {
        'qabullink': qabullink,
        'query': query,
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
    }
    return render(request, 'faq.html', context=context)

def search_results(request):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    qabullink = QabulLink.objects.first()
    if request.method == 'POST':
        ads = Ads.objects.filter(
            Q(name__icontains=request.POST['search']) | Q(area__icontains=request.POST['search'])
        )[::-1]
        news = News.objects.filter(
            Q(title__icontains=request.POST['search'])
        )[::-1]
        scien_event = ScientEvents.objects.filter(
            Q(name__icontains=request.POST['search'])
        )[::-1]
        context = {
            'qabullink': qabullink,
            'ads': ads,
            'news': news,
            'scien_event': scien_event,
            'site_logo': site_logo,
            'sociallinks': sociallinks,
            'contactaddress': contactaddress,
            'newslettertext': newslettertext,
        }
        return render(request, 'search-results.html', context=context)
    else:
        return HttpResponseBadRequest()