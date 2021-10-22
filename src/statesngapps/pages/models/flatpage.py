from django.contrib.flatpages.models import FlatPage as BaseFlatPageModel

class FlatPage(BaseFlatPageModel):
    class Meta:
        proxy = True
