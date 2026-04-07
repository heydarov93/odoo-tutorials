from odoo import models, fields
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):

    _name = "estate.property"
    _description = """Represents a real estate property with its details and attributes.
    Used to manage property listings, information, and related operations."""

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From", default=fields.Date.today() + relativedelta(months=3), copy=False)
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection(string="Garden Orientation", selection=[
        ('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
    active = fields.Boolean(default=True)
    property_type_id = fields.Many2one(comodel_name="estate.property.type", string="Property Type")
    partner_id = fields.Many2one(comodel_name="res.partner", string="Buyer", copy=False)
    user_id = fields.Many2one(comodel_name="res.users", string="Salesman", default=lambda self: self.env.user)
    property_tag_ids = fields.Many2many('estate.property.tag', string="Property Tags")
    state = fields.Selection(selection=[
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled'),        
    ], required=True, copy=False, default="new")
