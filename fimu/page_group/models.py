# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ionyweb.page.models import AbstractPageApp


class PageApp_Group(AbstractPageApp):
    
    # Define your fields here

    def __unicode__(self):
        return u'Group #%d' % (self.pk)

    class Meta:
        verbose_name = _(u"Group")


class Country(models.Model):
    """A list of countries."""
    code = models.CharField(_(u'code'), max_length=2, primary_key=True, 
                            help_text=_(u"See <a href='http://nephi.unice.fr/"
                                        u"codes_iso_pays.php' target='_blank'>"
                                        u"the country code list</a>."))

    name = models.CharField(_(u'name'), max_length=75)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = _(u'Country')
        verbose_name_plural = _(u"Countries")


class MusicStyle(models.Model):
    """A list of music type."""
    name = models.CharField(_(u'name'), max_length=30, unique=True)

    def __unicode__(self):
        return u'%s' % self.name


class Group(models.Model):
    app = models.ForeignKey(PageApp_Group, related_name="groups")

    music_style = models.ForeignKey(MusicStyle, related_name="groups")
    countries = models.ManyToManyField(Country, related_name="groups")

    code = models.CharField(_(u'code'), max_length=5, help_text=_(u"Exemple C002 ou MA201"))
    photo =  models.CharField(_("photo"), max_length=200, blank=True)

    name = models.CharField(_(u'name'), max_length=100)
    description = models.TextField(_(u'description'), blank=True)

    class Meta:
        ordering = ('code',)

    def __unicode__(self):
        return u"%s : %s" % (self.code, self.name)

    def class_css(self):
        style_class = re.search('^[a-zA-Z]+', self.code)
        return style_class.group(0)
