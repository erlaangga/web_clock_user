from odoo import api, fields, models


class Partner(models.Model):
	_inherit = "res.partner"

	show_clock = fields.Boolean("Show clock", default=True)
	show_clock_type = fields.Selection([('quartz', 'Quartz'), ('mechanical', 'Mechanical')], 'Movement', default="quartz")


class Users(models.Model):
	_inherit = "res.users"

	# User can write on a few of his own fields (but not his groups for example)
	SELF_WRITEABLE_FIELDS = ['signature', 'action_id', 'company_id', 'email', 'name', 'image', 'image_medium', 'image_small', 'lang', 'tz', 'show_clock', 'show_clock_type']
	# User can read a few of his own fields
	SELF_READABLE_FIELDS = ['signature', 'company_id', 'login', 'email', 'name', 'image', 'image_medium', 'image_small', 'lang', 'tz', 'tz_offset', 'groups_id', 'partner_id', '__last_update', 'action_id', 'show_clock', 'show_clock_type']

	show_clock = fields.Boolean(related='partner_id.show_clock', inherited=True, context={'user_preference': True})
	show_clock_type = fields.Selection(related='partner_id.show_clock_type', inherited=True, context={'user_preference': True})

