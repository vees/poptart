from django.db import models
import string
ALPHABET = string.ascii_lowercase + string.ascii_uppercase + string.digits
ALPHABET_REVERSE = dict((c, i) for (i, c) in enumerate(ALPHABET))
BASE = len(ALPHABET)

# Create your models here.
class Shortlink(models.Model):
	location = models.URLField(verify_exists=True, unique=True, db_index=True, max_length=200, null=False, blank=False)

