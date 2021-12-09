from odoo import models, fields, api
from odoo.exceptions import UserError

class TodoTags(models.Model):
    _name = 'todo.tags'
    _description = '待辦事項_標籤'
    _rec_name = 'title'

    title = fields.Char(required=True, string="標籤名")
    note = fields.Text()

    todos_ids = fields.One2many('todo.todos', 'tag')

class Todos(models.Model):
    _name = 'todo.todos'
    _description = '待辦事項_清單'

    todo = fields.Char(required=True, string="待辦清單")
    isCompleted = fields.Boolean(string="已完成?")
    description = fields.Text(string="說明")
    
    state = fields.Selection(selection=[('draft', '草案'),('short', '短計畫'),('long', '長計畫'),('urgent', '急件'),], string="狀態", default="draft")
    tag = fields.Many2one('todo.tags', string="標籤")

    @api.model
    def create(self, vals):
        if not vals.get('description'):  #如果沒有說明，就預設加入'無說明XD'
            vals['description'] = '無說明XD'

        if vals.get('isCompleted'):
            raise UserError('你不能建立已經完成的待辦事項！')

        return super(Todos, self).create(vals)

    def complete_todo(self):
        """已完成"""
        for todo in self:
            todo.isCompleted = True

    def uncomplete_todo(self):
        """未完成"""
        for todo in self:
            todo.isCompleted = False

