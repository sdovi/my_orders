from django.shortcuts import render
from .models import News
from base.models import *
from about_university.models import QabulLink
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def newsview(request):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    qabullink = QabulLink.objects.first()

    if request.method == 'POST' and 'search-ad' in request.POST:
        newss = News.objects.filter(
            Q(title__icontains=request.POST['search-ad'])
        )[::-1]
    else:
        newss = News.objects.all()[::-1]
    page = request.GET.get('page', 1)
    paginator = Paginator(newss, 9)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {
        'qabullink': qabullink,
        'news': news,
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
    }
    return render(request, 'blog.html', context=context)

def news_detailview(request, pk):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    qabullink = QabulLink.objects.first()

    news = News.objects.all()[::-1][:6]
    try:
        new = News.objects.get(pk=pk)
        new.count += 1
        new.save()
    except Exception as e:
        new['title'] = _('Object does not find! Sorry.')
    context = {
        'qabullink': qabullink,
        'new': new,
        'news': news,
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
    }
    return render(request, 'blog-detail.html', context=context)