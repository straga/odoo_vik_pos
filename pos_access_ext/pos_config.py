# -*- coding: utf-8 -*-


from openerp import models, fields, api

import logging

_logger = logging.getLogger(__name__) # Need for message in console.


class on_change_function(models.Model):

    # Inhertis the model pos.config
    _inherit = 'pos.config'

    secret_access = fields.Char(string='Manager code')



