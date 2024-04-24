# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class DiagramVersion(models.Model):
    _inherit = "diagram.version"
    
    task_id = fields.Many2one('project.task')