#!/usr/bin/env python

from canari.maltego.message import Entity, EntityField, EntityFieldType

__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2012, CIFari Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'

__all__ = [
    'CIFEntity',
    'CIFQuery'
]


class CIFEntity(Entity):
    namespace = 'cifari'


@EntityField(name='cifquery.confidence', propname='confidence', displayname='Confidence', type=EntityFieldType.Integer)
@EntityField(name='cifquery.severity', propname='severity', displayname='Severity')
class CIFQuery(CIFEntity):
    pass


@EntityField(name='cifentry.address', propname='address')
@EntityField(name='cifentry.malware_md5', propname='malware_md5', displayname='Malware MD5')
@EntityField(name='cifentry.alternativeid', propname='alternativeid')
@EntityField(name='cifentry.alternativeid_restriction', propname='alternativeid_restriction')
@EntityField(name='cifentry.confidence', propname='confidence')
@EntityField(name='cifentry.description', propname='description')
@EntityField(name='cifentry.detecttime', propname='detecttime')
@EntityField(name='cifentry.guid', propname='guid')
@EntityField(name='cifentry.uuid', propname='uuid', displayname='UUID')
@EntityField(name='cifentry.impact', propname='impact')
@EntityField(name='cifentry.portlist', propname='portlist')
@EntityField(name='cifentry.protocol', propname='protocol')
@EntityField(name='cifentry.purpose', propname='purpose')
@EntityField(name='cifentry.relatedid', propname='relatedid')
@EntityField(name='cifentry.restriction', propname='restriction')
@EntityField(name='cifentry.severity', propname='severity')
@EntityField(name='cifentry.source', propname='source')
class CIFEntry(CIFEntity):
    pass
