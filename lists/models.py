""" list models """

from django.db import models
from django.core.urlresolvers import reverse


class List(models.Model):
    """ List model """

    def get_absolute_url(self):
        """ generate and return the URL for this model instance """

        return reverse('view_list', args=[self.id])


class Item(models.Model):
    """ List item model """

    text = models.TextField()
    list = models.ForeignKey(List)

    class Meta:
        """ List item model metaclass """

        ordering = ('id', )
        unique_together = ('text', 'list')

    def __str__(self):
        """ return string representation of the instance """

        return self.text
