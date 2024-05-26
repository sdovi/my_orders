from django.shortcuts import render
from base.models import *
from about_university.models import QabulLink
from .models import *
from django.utils.translation import gettext_lazy as _

def science_view(request, slug=None):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    qabullink = QabulLink.objects.first()

    if slug == 'research':
        query = ResearchAndDev.objects.all().first()
    if slug == 'infrastructure':
        query = ScientInfrastructure.objects.all().first()
    if slug == 'journals':
        query = Journals.objects.all().first()
    if slug == 'scientific-cert':
        query = ScientificCert.objects.all()
    if slug == 'scientific-events':
        query = ScientEvents.objects.all()
    
    context = {
        'qabullink': qabullink,
        'query': query,
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
    }
    if slug == 'scientific-cert':
        return render(request, 'scientific-cert.html', context=context)
    elif slug == 'scientific-events':
        return render(request, 'scientific-events.html', context=context)
    else:
        return render(request, 'universal.html', context=context)

def scientific_event_detail(request, pk):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    qabullink = QabulLink.objects.first()

    query = ScientEventDetail.objects.get(scientevent_id=pk)
    context = {
        'qabullink': qabullink,
        'query': query,
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
    }
    return render(request, 'universal.html', context=context)