# Copyright (c) 2006 L. C. Rees
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#
#    2. Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
#    3. Neither the name of the Portable Site Information project nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''Berkeley Source Database Store.

shove's psuedo-URL for BSDDB stores follows the form:

bsddb://<path>

Where the path is a URL path to a BSDDB database. Alternatively, a native
pathname to a BSD database can be passed as the 'engine' argument.
'''

import bsddb
from urllib import url2pathname
try:
    import cPickle as pickle
except ImportError:
    import pickle
from shove import synchronized
from shove.store import SyncStore

__all__ = ['BsdStore']


class BsdStore(SyncStore):
    
    '''Class for Berkeley Source Database Store.'''

    def __init__(self, engine, **kw):
        super(BsdStore, self).__init__(engine, **kw)
        if engine.startswith('bsddb://'):
            engine = url2pathname(engine.split('://')[1])
        self._store = bsddb.hashopen(engine)
        self.sync = self._store.sync

    @synchronized
    def __getitem__(self, key):
        return super(BsdStore, self)[key]

    @synchronized
    def __setitem__(self, key, value):
        super(BsdStore, self)[key] = value

    @synchronized
    def __delitem__(self, key):
        del super(BsdStore, self)[key]