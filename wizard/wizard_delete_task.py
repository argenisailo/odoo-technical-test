from odoo import models, fields, api
from odoo.exceptions import UserError

class WizardDeleteTask(models.TransientModel):
    _name = 'wizard.delete.task'
    _description = 'Wizard to Delete Task'

    title = fields.Char(string='Task Title', required=True)

    def action_delete_task(self):
        task = self.env['to.do.list'].search([('title', '=', self.title)], limit=1)
        if task:
            task.unlink()
        else:
            raise UserError('Task with title "%s" not found' % self.title)
        return {'type': 'ir.actions.act_window_close'}
