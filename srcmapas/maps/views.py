from django.http import HttpResponse
from django.shortcuts import render
# from django.utils import simplejson
import json as simplejson
from django.utils.timesince import timesince
from .models import Ubicacion
from .forms import UbicacionForm
from django.core import serializers

def index(request):
	forms = UbicacionForm()
	ubicaciones = Ubicacion.objects.all().order_by('-fechaI')
	return render(request, 'maps/index.html', {'form': forms, 'ubicaciones': ubicaciones})

def testeJson(request):
	querySet = Ubicacion.objects.all()
	# fields = ['nombre', 'lat', 'lng']
	querySet = serializers.serialize('json', querySet, fields=('nombre','latI', 'lngI'))
	return HttpResponse(querySet, content_type="application/json")

def testeJson2(request):
	# data = json.dumps({ 'participant_specific_donation' : info , 'participant_specific_milestone' : info1 })
	querySet2 = {'ok': True, 'msg': 'mensagem transmitida com sucesso'}
	querySet2 = simplejson.dumps(querySet2)
	return HttpResponse(querySet2, content_type="application/json")

def coords_save(request):
	if request.is_ajax():
		form =UbicacionForm(request.POST)
		if form.is_valid():
			form.save()
			ubicaciones = Ubicacion.objects.all().order_by('-fechaI')

			dataTexto = '<url id="ubicacionesList">'
			for ubicacion in ubicaciones:
				dataTexto += '<li>%s, %s, hace %s</li>' % (ubicacion.nombre, ubicacion.user, timesince(ubicacion.fechaI))
			dataTexto += '</url>'
		
			dataTexto2 = simplejson.dumps({'ok':True, 'msg': dataTexto})			

		else:
			dataTexto2 = {'ok':False, 'msg': 'Deves llenar los datos'}			
			dataTexto2 = simplejson.dumps(dataTexto2)
		
		return HttpResponse(dataTexto2, content_type='application/json')
