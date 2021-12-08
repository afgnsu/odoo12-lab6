from odoo import models, fields, api
from odoo.exceptions import UserError

class TodoTags(models.Model):
    _name = 'todo.tags'
    _description = '待辦事項_標籤'
    _rec_name = 'title'

    title = fields.Char(required=True, string="Tag name")
    note = fields.Text()

    todos_ids = fields.One2many('todo.todos', 'tag')

class Todos(models.Model):
    _name = 'todo.todos'
    _description = '待辦事項_清單'

    todo = fields.Char(required=True)
    isCompleted = fields.Boolean()
    description = fields.Text()
    
    state = fields.Selection(selection=[('draft', '草稿'),('short', '短程'),('long', '長程'),('urgent', '急件'),], string="狀態", default="draft")
    tag = fields.Many2one('todo.tags')

    @api.model
    def create(self, vals):
        if not vals.get('description'):  #如果沒有描述
            vals['description'] = '預設描述'

        if vals.get('isCompleted'):
            raise UserError('你不能建立已經完成的待辦事項！')

        return super(Todos, self).create(vals)

    def complete_todo(self):
        """Complete todo"""
        for todo in self:
            todo.isCompleted = True

    def uncomplete_todo(self):
        """Complete todo"""
        for todo in self:
            todo.isCompleted = False

