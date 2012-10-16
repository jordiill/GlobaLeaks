# -*- coding: UTF-8
#
#   admin
#   *****
#
#   :copyright: 2012 Hermes No Profit Association - GlobaLeaks Project
#   :author: Claudio Agosti <vecna@globaleaks.org>, Arturo Filastò <art@globaleaks.org>
#   :license: see LICENSE
#
from globaleaks.rest import answers

from globaleaks.handlers.base import BaseHandler
from globaleaks.utils import log

class AdminNode(BaseHandler):

    log.debug("[D] %s %s " % (__file__, __name__), "Class AdminNode", "BaseHandler", BaseHandler)
    # A1
    """
    Get the node main settings, update the node main settings
    """
    def get(self):
        log.debug("[D] %s %s " % (__file__, __name__), "Class AdminNode", "get")
        pass

    def post(self):
        log.debug("[D] %s %s " % (__file__, __name__), "Class AdminNode", "post")
        pass


class AdminContexts(BaseHandler):

    log.debug("[D] %s %s " % (__file__, __name__), "Class AdminContexts", "BaseHandler", BaseHandler)
    # A2
    """
    classic CURD in the 'contexts'
    """
    def get(self, context_id):
        log.debug("[D] %s %s " % (__file__, __name__), "Class AdminContexts", "get")
        pass

    def post(self, context_id):
        log.debug("[D] %s %s " % (__file__, __name__), "Class AdminContexts", "post")
        pass

    def put(self, context_id):
        log.debug("[D] %s %s " % (__file__, __name__), "Class AdminContexts", "put")
        pass

    def delete(self, context_id):
        log.debug("[D] %s %s " % (__file__, __name__), "Class AdminContexts", "delete")
        pass


class AdminReceivers(BaseHandler):
    log.debug("[D] %s %s " % (__file__, __name__), "Class AdminReceivers", "BaseHandler", BaseHandler)
    # A3
    """
    classic CURD in the 'receivers'
    """
    def get(self, context_id):
        log.debug("[D] %s %s " % (__file__, __name__), "Class AdminReceivers", "get")
        pass

    def post(self, context_id):
        log.debug("[D] %s %s " % (__file__, __name__), "Class AdminReceivers", "post")
        pass

    def put(self, context_id):
        log.debug("[D] %s %s " % (__file__, __name__), "Class AdminReceivers", "put")
        pass

    def delete(self, context_id):
        log.debug("[D] %s %s " % (__file__, __name__), "Class AdminReceivers", "delete")
        pass


class AdminModules(BaseHandler):
    log.debug("[D] %s %s " % (__file__, __name__), "Class AdminModules", "BaseHandler", BaseHandler)
    # A4
    """
    A limited CURD (we've not creation|delete, just update, with
    maybe a flag that /disable/ a module)
    """
    def get(self, context_id, module_id):
        log.debug("[D] %s %s " % (__file__, __name__), "Class AdminModules", "get")
        pass

    def post(self, context_id, module_id):
        log.debug("[D] %s %s " % (__file__, __name__), "Class AdminModules", "post")
        pass
