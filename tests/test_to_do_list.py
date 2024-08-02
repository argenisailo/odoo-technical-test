from odoo.tests.common import TransactionCase

class TestToDoList(TransactionCase):
    def setUp(self):
        super(TestToDoList, self).setUp()
        self.ToDoList = self.env['to.do.list']
        self.WizardDeleteTask = self.env['wizard.delete.task']

    def test_name_get(self):
        # Create a test registry
        todo = self.ToDoList.create({'title': 'Test Task'})
        # Check registry's name
        self.assertEqual(todo.name_get()[0][1], 'Test Task')

    def test_action_open_delete_wizard(self):
        # Create a test registry
        todo = self.ToDoList.create({'title': 'Test Task'})
        # Execute method
        action = todo.action_open_delete_wizard()
        # Check that the action returns the right existing form
        self.assertEqual(action['res_model'], 'wizard.delete.task')

    def test_action_delete_task(self):
        # Create a test registry
        todo = self.ToDoList.create({'title': 'Test Task'})
        # Create a deleting assitant
        wizard = self.WizardDeleteTask.create({'title': 'Test Task'})
        # Execute the deleting action
        wizard.action_delete_task()
        # Verifyng that the task was deleted
        self.assertFalse(self.ToDoList.search([('title', '=', 'Test Task')]))

    def test_action_delete_task_not_found(self):
        # Create a deleting assitant
        wizard = self.WizardDeleteTask.create({'title': 'Non-existent Task'})
        # Execute the deleting action and check that the exception was raised
        with self.assertRaises(UserError):
            wizard.action_delete_task()
