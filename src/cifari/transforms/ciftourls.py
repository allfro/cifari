#!/usr/bin/env python

from canari.maltego.entities import URL
from canari.framework import configure
from canari.maltego.message import Field
from common.entities import CIFEntry
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
    label='To URLs',
    description='Converts CIF Entries into URLs.',
    uuids=['cifari.v2.CIFEntryToURL'],
    inputs=[( "Collective Intelligence", CIFEntry )],
    debug=True
)
def dotransform(request, response):
    e = URL(request.value[:64])
    e += Field('url', request.value)
    response += e
    return response
