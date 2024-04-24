# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class DiagramVersion(models.Model):
    _name = "diagram.version"
    _description = "Stores Diagram xml data"
    _order = "create_date DESC"
    _rec_name = "name"

    name = fields.Char(copy=False, compute="_compute_name", store=True)
    diagram_xml = fields.Text()

    @api.depends('create_date')
    def _compute_name(self):
        for rec in self:
            timezone = self._context.get('tz') or self.env.user.partner_id.tz or 'UTC'
            self_tz = self.with_context(tz=timezone)
            date = fields.Datetime.context_timestamp(self_tz, rec.create_date)
            rec.name = _(f"{rec.task_id.name} - {date.strftime('%Y-%m-%d %H:%M:%S')}")
