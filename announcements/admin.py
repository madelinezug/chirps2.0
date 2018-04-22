from django.contrib import admin

# Register your models here.
from .models import Individual
from .models import Announcement
from .models import Tags
from .models import AnnounceTags
from .models import SubmitTag
from .models import UserSearch
from .models import TagSearch
from .models import Save


admin.site.register(Individual)
admin.site.register(Announcement)
admin.site.register(Tags)
admin.site.register(AnnounceTags)
admin.site.register(SubmitTag)
admin.site.register(UserSearch)
admin.site.register(TagSearch)
admin.site.register(Save)
