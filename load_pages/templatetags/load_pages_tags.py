from django import template

from load_pages.models import ArticleIndexPage

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    return context['request'].site.root_page


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('load_pages/tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.inclusion_tag('load_pages/tags/top_menu.html', takes_context=True)
def top_menu(context, calling_page=None):

    menuitems = ArticleIndexPage.objects.live().in_menu()
    for menuitem in menuitems:
        if calling_page.url == menuitem.url:
            menuitem.active = True

    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        'request': context['request'],
    }
