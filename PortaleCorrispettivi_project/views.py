from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from PortaleCorrispettivi.models import *


def HomePage(request):
	return render(request,'HomePage.html', )


def loadingPageMonitoraggio(request):
	link_monitoraggio = linkportale.objects.filter(tag='portale-monitoraggio')[0].link
	return render(request, 'loading_gif/loading_1.html', {'link_monitoraggio':link_monitoraggio})


@login_required(login_url='login')
def loadingPageAnalisi(request):
	link_analisi = linkportale.objects.filter(tag='portale-analisi')[0].link
	return render(request, 'loading_gif/loading_2.html', {'link_analisi':link_analisi})


@login_required(login_url='login')
def loadingPageCorrispettivi(request):
	return render(request, 'loading_gif/loading_3.html')
