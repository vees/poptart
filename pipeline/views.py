from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
import links

# Create your views here.
def redirect(request, shortlink):
	try:
		location = links.fetch_link(shortlink)
	except:
		return HttpResponseNotFound(content='This link caused an error, Jim')
	if location==False:
		return HttpResponseNotFound(content='This link has not been defined yet')
	return HttpResponseRedirect(location) 

def index(request):
	return HttpResponseRedirect('https://vees.net/')

