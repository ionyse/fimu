# -*- coding: utf-8 -*-

from django.template import RequestContext
from ionyweb.website.rendering.utils import render_view

# from ionyweb.website.rendering.medias import CSSMedia, JSMedia, JSAdminMedia
MEDIAS = (
    # App CSS
    # CSSMedia('page_group.css'),
    # App JS
    # JSMedia('page_group.js'),
    # Actions JSAdmin
    # JSAdminMedia('page_group_actions.js'),
    )

def index_view(request, page_app):
    liste = ['Tata', 'titi', 'toto']
    return render_view('page_group/index.html',
                       { 'object': page_app,
                         'ma_liste': liste },
                       MEDIAS,
                       context_instance=RequestContext(request))

