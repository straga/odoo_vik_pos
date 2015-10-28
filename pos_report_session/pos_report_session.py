# -*- coding: utf-8 -*-

from openerp.report import report_sxw
from openerp.osv import osv, fields
import logging
import time
_logger = logging.getLogger(__name__) # Need for message in console.


class report_session_ext(report_sxw.rml_parse):

    def _get_user_names(self):
        user_obj = "dummy_user"
        return user_obj


    def __init__(self, cr, uid, name, context):
        super(report_session_ext, self).__init__(cr, uid, name, context=context)

        self.total = 0.0
        self.localcontext.update({
            'get_user_names': self._get_user_names,

        })

class pos_report_session_ext(osv.AbstractModel):
    _name = 'report.pos_report_session.report_session_summary_ext'
    _inherit = 'report.abstract_report'
    _template = 'pos_report_session.report_session_summary_ext'
    _wrapped_report_class = report_session_ext