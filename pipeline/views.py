from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.conf import settings

import links
import hmac
import urllib

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

def set_with_secret(request):
    #return HttpResponse("Set with secret")
    urltoshrink = request.GET.get('url', None)
    hmachash = request.GET.get('hmachash',None)
    calchmac = hmac.new(settings.PIPELINE_API_SECRET,urltoshrink).hexdigest()
    #url = urllib.urldecode(urltoshrink)
    if hmachash == calchmac:
        try:
            location = links.set_link(urltoshrink)
            return HttpResponse("http://4ve.es/" + location)
        except Exception as ex:
            raise ex
            return HttpResponse("Exception %s %s" % (urltoshrink,hmachash,calchmac))
    else:
        return HttpResponse("Invalid KVP %s %s" % (urltoshrink,hmachash,calchmac))

