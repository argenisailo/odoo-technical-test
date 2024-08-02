from odoo import models, fields, api

class ToDoList(models.Model):
    _name = 'to.do.list'
    _description = 'To-do List'

    title = fields.Char(string='Title')
    description = fields.Text(string='Description')

    def action_open_delete_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Delete Task',
            'res_model': 'wizard.delete.task',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_title': self.title,
            },
        }
    
    def name_get(self):
        result = []
        for record in self:
            name = record.title
            result.append((record.id, name))
        return result