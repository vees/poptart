from pipeline import links
from pipeline.models import Shortlink 

for link in Shortlink.objects.all():
	print link.id, links.num_encode(link.id), link.location

