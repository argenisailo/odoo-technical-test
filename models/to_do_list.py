from odoo import models, fields, api

class ToDoList(models.Model):
    _name = 'to.do.list'

    title = fields.Char(string='Title')
    description = fields.Text(string='Description')