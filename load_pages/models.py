# coding=utf-8
from __future__ import unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField



class ArticleIndexPage(Page):

    body = RichTextField()


class ArticlePage(Page):

    text = RichTextField()
    preview = RichTextField()
    date = models.DateField(u"Дата статьи")

    parent_page_types = ['ArticleIndexPage']
