# -*- coding: utf-8 -*-

import floppyforms as forms
from ionyweb.forms import ModuloModelForm
from models import PageApp_Group

class PageApp_GroupForm(ModuloModelForm):

    class Meta:
        model = PageApp_Group