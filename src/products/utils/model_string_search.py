########################################
#########product searching##############
########################################
from django.db.models import Q
import re
from products.models import Product

def normalize_query(query_string,
    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
    normspace=re.compile(r'\s{2,}').sub):

    '''
    Splits the query string in invidual keywords, getting rid of unecessary spaces and grouping quoted words together.
    Example:
    >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    '''

    return [normspace(' ',(t[0] or t[1]).strip()) for t in findterms(query_string)]



def get_query(query_string, search_fields):

    '''
    Returns a query, that is a combination of Q objects. 
    That combination aims to search keywords within a model by testing the given search fields.
    '''

    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query | or_query
    return query

def search_for_something(request):
    query_string = ''
    found_entries = None

    if ('search_string' in request.GET) and request.GET['search_string'].strip():
        query_string = request.GET['search_string']
        entry_query = get_query(query_string, ['description', 'tags', 'title'])
        found_entries = Product.objects.filter(entry_query)

    return found_entries
    ####################################################
################# end of product searching functions########################
#####################################################################