from django.shortcuts import render
from base.models import *
from about_university.models import QabulLink
from .models import *
from django.utils.translation import gettext_lazy as _

def international_view(request, slug=None):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    qabullink = QabulLink.objects.first()

    if slug == 'preparing-foreigners':
        query = PreparingForeigners.objects.all().first()
    if slug == 'organization-CIS':
        query = OrganizationCIS.objects.all().first()
    if slug == 'cooperation':
        query = Cooperation.objects.all().first()
    if slug == 'graduates':
        query = Graduates.objects.all().first()
    if slug == 'students-foreign-program':
        query = AboutMPEIStudentsForeignPrograms.objects.all().first()
    if slug == 'information':
        query = Information.objects.all().first()
    if slug == 'global-energy-association':
        query = GlobalEnergyAssociation.objects.all().first()
    if slug == 'registration-for-amo':
        query = RegistrationForAMO.objects.all().first()
    if slug == 'foreign-programs':
        query = ForeignPrograms.objects.all()
    
    context = {
        'qabullink': qabullink,
        'query': query,
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
    }
    if slug == 'foreign-programs':
        return render(request, 'foreign-programs.html', context=context)
    else:
        return render(request, 'universal.html', context=context)

def foreign_program_detail(request, pk):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    qabullink = QabulLink.objects.first()

    try:
        query = ForeignProgramDetail.objects.get(foreignprograms_id=pk)
    except Exception as e:
        query = 'Not found'
    context = {
        'qabullink': qabullink,
        'query': query,
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
    }
    return render(request, 'universal.html', context=context)
