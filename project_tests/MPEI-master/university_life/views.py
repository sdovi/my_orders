from django.shortcuts import render
from base.models import *
from .models import *
from about_university.models import QabulLink
from django.utils.translation import gettext_lazy as _

def univer_life_view(request, slug=None):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    qabullink = QabulLink.objects.first()

    if slug == 'culture':
        query = Culture.objects.all().first()
    if slug == 'health-and-sport':
        query = HealthAndSport.objects.all().first()
    if slug == 'campus':
        query = Campus.objects.all().first()
    if slug == 'psycological-support':
        query = PsycoSupport.objects.all().first()
    
    context = {
        'qabullink': qabullink,
        'query': query,
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
    }
    return render(request, 'universal.html', context=context)
