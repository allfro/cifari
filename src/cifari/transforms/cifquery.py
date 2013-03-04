#!/usr/bin/env python

from canari.framework import configure
from common.entities import CIFQuery, CIFEntry
from canari.config import config
from cif import Client


__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2012, CIFari Project'
__credits__ = ['Nadeem Douba']

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'


@configure(
    label='To CIF Entries [CIF]',
    description='This transform gets CIF entries for the specified CIF query.',
    uuids=['cifari.v2.CIFQueryToCIFEntry_CIF'],
    inputs=[( "Collective Intelligence", CIFQuery )],
    debug=True
)
def dotransform(request, response):

    c = Client(host=config['cif/host'], apikey=config['cif/apikey'])

    r = c.GET(
        request.value,
        severity=request.fields.get('cifquery.severity', ''),
        confidence=request.fields.get('cifquery.confidence', ''),
        restriction=request.fields.get('cifquery.restriction', ''),
        guid=request.fields.get('cifquery.guid', ''),
        simple=True
    ) or {'feed': {'entry': []}}

    for e in r['feed']['entry']:
        ce = CIFEntry(e.get('address', e.get('malware_md5', '')))
        for k in e:
            setattr(ce, k, e[k] or '')
        response += ce
    return response
