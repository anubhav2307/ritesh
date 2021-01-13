import requests,json
from django.shortcuts import render,redirect
from .forms import CityForm,GeoForm

def city_weather(request):
	form = CityForm()
	if request.method == 'POST':
		form = CityForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			name=cd['City']
			api_url = f"http://api.openweathermap.org/data/2.5/weather?q={name}&appid=0f316a6608839d6365ca2c9ebd7703d5"
			api = requests.get(api_url).json()
			print (api)
			form=CityForm()
			if api['cod']==200:
				context = {'temp_min':api['main']['temp_min']-273.15,'temp_max':api['main']['temp_max']-273.15,'humidity':api['main']['humidity'],'visibility':api['visibility']/1000,'form':form}
				return render(request,'city_weather.html',context)
			else:
				return redirect('city_weather')

	context={'form':CityForm()}		
	return render(request,'city_weather.html',context)


def geograph_weather(request):
	form = GeoForm()
	if request.method == 'POST':
		form = GeoForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			lati = cd['Latitude']
			longi = cd['Longitude']
			api_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lati}&lon={longi}&appid=0f316a6608839d6365ca2c9ebd7703d5"
			api = requests.get(api_url).json()
			print (api)
			form = GeoForm()
			if api['cod']==200:
				context = {'temp_min':api['main']['temp_min']-273.15,'temp_max':api['main']['temp_max']-273.15,'humidity':api['main']['humidity'],'visibility':api['visibility']/1000,'name':api['name'],'form':form}
				return render(request,'geographical_weather.html',context)
	form = GeoForm()			
	return render(request,'geographical_weather.html',{'form':form})

