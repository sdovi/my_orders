from django.shortcuts import render, HttpResponse
from .models import *
from base.models import *

def about_university_view(request, slug=None):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    qabullink = QabulLink.objects.first()

    if slug == 'introduce-MEI':
        query = IntroduceMEI.objects.all().first()
    if slug == 'official-information':
        query = LegalInfo.objects.all().first()
    if slug == 'WEB-resource':
        query = WEBresource.objects.all().first()
    if slug == 'partners':
        query = Partners.objects.all().first()
    if slug == 'honorable-p':
        query = Honorary.objects.all()
    
    context = {
        'qabullink': qabullink,
        'query': query,
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
    }
    if slug == 'honorable-p':
        return render(request, 'card.html', context=context)
    else:
        return render(request, 'universal.html', context=context)

