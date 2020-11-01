from django.urls import path
from django.views.generic.dates import ArchiveIndexView

from .models import Article

urlpatterns = [
    path('',
         ArchiveIndexView.as_view(model=Article, date_field="pub_date"),
         name="article_archive"),
]