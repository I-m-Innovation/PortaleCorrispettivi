from django.contrib import admin
from .models import *


@admin.register(Impianto)
class ImpiantoAdmin(admin.ModelAdmin):
	list_filter = ['tipo', 'proprieta']
	list_display = [field.name for field in Impianto._meta.fields]
	form = ImpiantoForm


@admin.register(Commento)
class CommentoAdmin(admin.ModelAdmin):
	list_filter = ['impianto']
	list_display = [field.name for field in Commento._meta.fields]
	form = AddCommentoForm


@admin.register(DiarioLetture)
class DiarioLettureAdmin(admin.ModelAdmin):
	list_filter = ['impianto', 'anno']
	list_display = [field.name for field in DiarioLetture._meta.fields]
	form = AddDiarioLettureForm


@admin.register(Cashflow)
class CashflowAdmin(admin.ModelAdmin):
	list_filter = ['impianto']
	list_display = [field.name for field in Cashflow._meta.fields]
	form = AddCashflowForm


@admin.register(DatiMensili)
class CashflowAdmin(admin.ModelAdmin):
	list_filter = ['impianto']
	list_display = [field.name for field in DatiMensili._meta.fields]
	form = AddDatiMensiliForm
