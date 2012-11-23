# -*- coding: utf-8 -*-
from ionyweb.administration.actions.utils import get_actions_urls

from models import Country, MusicStyle, Group
# from forms import GroupForm
# from actions.views import (ImageActionAdminListView,
#                            ImageActionAdminDetailView)


urlpatterns = get_actions_urls(Country)
urlpatterns += get_actions_urls(MusicStyle)
urlpatterns += get_actions_urls(Group)
