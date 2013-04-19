from example.electionperson.interfaces import IElectionPerson
from Products.CMFCore.utils import getToolByName
from plone.indexer import indexer


@indexer(IElectionPerson)
def electionperson_firstName(object, **kw):
    catalog = getToolByName(object, 'portal_catalog')
    return object.firstName
    
@indexer(IElectionPerson)
def electionperson_lastName(object, **kw):
    catalog = getToolByName(object, 'portal_catalog')
    return object.lastName
    
    
@indexer(IElectionPerson)
def electionperson_gender(object, **kw):
    catalog = getToolByName(object, 'portal_catalog')
    return object.gender
    
    

