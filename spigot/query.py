import urllib
import hmac
import sys
import urllib
import urllib2

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('simple.ini')

hmackey = parser.get('spigot', 'hmackey')

urltoshrink = raw_input("Encode: ")
calchmac = hmac.new(hmackey,urltoshrink).hexdigest()
get_params = {
        'url' : urltoshrink,
        'hmachash'   : calchmac,
    }
params = urllib.urlencode(get_params)
r = urllib2.Request("http://4ve.es/api/new/?%s" % params)
f = urllib2.urlopen(r)
print f.read()
