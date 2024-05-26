from django.shortcuts import render
from .models import *
from base.models import *
from about_university.models import QabulLink
from django.utils.translation import gettext_lazy as _

def scient_concil_view(request, slug=None):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    qabullink = QabulLink.objects.first()

    if slug == 'the-board-off-directors':
        query = TheBoardOfDirectors.objects.all()
    if slug == 'scientific-council':
        query = ScientificCouncil.objects.all()
    if slug == 'university-management':
        query = UniversityManagement.objects.all().first()
    if slug == 'departments-and-centers':
        query = DepartmentsAndCenters.objects.all().first()
    if slug == 'offices':
        query = OfficesAndDepartments.objects.all().first()
    if slug == 'public-organizations':
        query = PublicOrganizations.objects.all().first()
    
    context = {
        'qabullink': qabullink,
        'query': query,
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
    }
    if slug == 'scientific-council':
        return render(request, 'scient-council.html', context=context)
    if slug == 'the-board-off-directors':
        return render(request, 'the-board-off-directors.html', context=context)
    else:
        return render(request, 'universal.html', context=context)


def leaders(request):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    query = MPEIuzLeaders.objects.all()
    qabullink = QabulLink.objects.first()

    context = {
        'qabullink': qabullink,
        'query': query,
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
    }
    return render(request, 'leadership.html', context=context)

def leader_detail(request, pk):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    qabullink = QabulLink.objects.first()

    try:
        query = MPEIuzLeaderDetail.objects.get(mpeiuzLeaders_id=pk)
    except Exception as e:
        query = 'Not Found'

    context = {
        'qabullink': qabullink,
        'query': query,
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
    }
    return render(request, 'universal.html', context=context)


