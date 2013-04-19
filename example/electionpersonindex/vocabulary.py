from five import grok
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from Products.CMFCore.utils import getToolByName
from plone.i18n.normalizer import idnormalizer

def make_terms(items):
    """ Create zope.schema terms for vocab from tuples """
    terms = [ SimpleTerm(value=pair[0], token=pair[0], title=pair[1]) for pair in items ]
    return terms
    
    
@grok.provider(IContextSourceBinder)
def gender_vocab(context):
    catalog = getToolByName(context, 'portal_catalog')
    # Get catalog brain objects of all accommondation content
    index = catalog._catalog.getIndex("electionperson_gender")
    items = index.items()
    result = []
    for item in items:
        entry = (item[0], item[0])
        result.append(entry)
    # Convert tuples to SimpleTerm objects
    terms = make_terms(result)
    return SimpleVocabulary(terms)
