from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from base.models import *
from about_university.models import QabulLink
from .models import *

@login_required
def schedule(request):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    qabullink = QabulLink.objects.first()

    query = Faculty.objects.all()
    context = {
        'qabullink': qabullink,
        'query': query,
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
    }
    return render(request, 'schedule.html', context=context)

@login_required
def group(request, pk):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    qabullink = QabulLink.objects.first()

    query = Group.objects.filter(faculty_id=pk)

    context = {
        'qabullink': qabullink,
        'query': query,
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
    }
    return render(request, 'group.html', context=context)

def edu(request, slug=None):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    qabullink = QabulLink.objects.first()

    if slug == 'edu-program':
        query = EduProgram.objects.all().first()
    if slug == 'training-degree':
        query = TreResults.objects.all().first()
    if slug == 'additional-edu':
        query = AdditionalEdu.objects.all().first()
    if slug == 'dist-edu':
        query = DistanceEdu.objects.all().first()
    if slug == 'emp-and-internship':
        query = EmpAndInternship.objects.all().first()
    if slug == 'final-qua':
        query = FinalQua.objects.all().first()
    if slug == 'official-docs':
        query = OfficialDocs.objects.all().first()

    context = {
        'qabullink': qabullink,
        'query': query,
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
    }
    return render(request, 'universal.html', context=context)