import sys
from pipeline.models import *
sys.path.append("/home/rob/Projects/")

Shortlink.objects.all()
s=Shortlink()
s.location="http://vees.net/"
s.pk=12345
s.save()

