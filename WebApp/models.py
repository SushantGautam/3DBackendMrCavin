from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import DateTimeField
from django.db.models import FileField
from django.db.models import TextField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Question(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    Model = models.FileField(upload_to="upload/files/")
    name = models.TextField(max_length=100)
    Option1 = models.TextField()
    Option2 = models.TextField()
    Option3 = models.TextField()
    Option4 = models.TextField()


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('WebApp_question_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('WebApp_question_update', args=(self.slug,))


