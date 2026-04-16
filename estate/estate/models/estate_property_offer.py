from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="Estate Property Offer"
    
    price = fields.Float()
    status = fields.Selection(selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)
    validity =  fields.Integer(string="Validity Days", default=7)
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    
    @api.depends("validity")
    def _compute_date_deadline(self):
        for rec in self:
            create_date = rec.create_date or fields.Date.today()
            rec.date_deadline = create_date + relativedelta(days=rec.validity)
    
    def _inverse_date_deadline(self):
        fmt = '%Y-%m-%d'

        for rec in self:
            rec.validity = (rec.date_deadline - (fields.Date.to_date(rec.create_date) or fields.Date.today())).days
    