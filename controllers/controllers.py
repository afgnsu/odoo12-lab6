from odoo import http

# `todo` is name of folder and NOT module

class Todos(http.Controller):

    # Welcome page
    @http.route('/todo/welcome', auth='public', website=True)
    def welcome(self, **kw):
        context = {
            'message': 'Hello, world'
        }
        return http.request.render('todo.welcome', context)
    
    # Todo tags
    @http.route('/todo/tags', auth="public", website=True)
    def todo_tags(self, **kw):
        Todotags = http.request.env['todo.tags']
        context = {
            'tags': Tags.search([])
        }
        return http.request.render('todo.tags', context)

     # Todo tag individual
    @http.route('/todo/tag/<int:tag_id>', auth="public", website=True)
    def todo_tag(self, tag_id=None, **kw):
        Todotags = http.request.env['todo.tags']
        context = {
            'tag_id': tag_id,
            'tag': Tags.search([('id', '=', tag_id)])
        }
        return http.request.render('todo.tag', context)
    
    # Todos list
    @http.route('/todo/todos', auth="public", website=True)
    def todos(self, **kw):
        Todos = http.request.env['todo.todos']
        context = {
            'todos': Todos.search([])
        }
        return http.request.render('todo.todos', context)
        
    # Individual todo
    @http.route('/todo/todo/<int:todo_id>', auth="public", website=True)
    def todo(self, todo_id=None, **kw):
        Todos = http.request.env['todo.todos']

        context = {
            'todo_id': todo_id,
            'todo': Todos.search([('id', '=', todo_id)])
        }
        return http.request.render('todo.todo', context)

    # Todo create page
    @http.route('/todo/todo/createpage', auth="public", website=True)
    def todo_create_page(self, **kw):
        todo_tags = http.request.env['todo.tags'].search([])
        context = {
            'todo_tags': todo_tags
        }
        return http.request.render('todo.createpage', context)
    
    # Todo edit page
    @http.route('/todo/todo/edit/<int:todo_id>', auth="public", website=True)
    def todo_edit_page(self, todo_id=None, **kw):
        todo = http.request.env['todo.todos'].search([('id', '=', todo_id)])
        tags = http.request.env['todo.tags'].search([])
        context = {
            'todo_id': todo_id,
            'todo': todo,
            'tags': tags
        }
        return http.request.render('todo.editpage', context)
    
    # Todo edit route
    @http.route('/todo/todo/edit', auth="public", website=True)
    def todo_edit(self, **kw):
        todo_id = kw['todo_id']
        todo = http.request.env['todo.todos'].search([('id', '=', todo_id)])

        del kw['todo_id'] # removing `todo_id` element
        todo.sudo().write(kw)
        context = {
            'message': todo.todo
        }
        return http.request.render('todo.message', context)

    # Todo create route
    @http.route('/todo/todo/create', auth="public", website=True)
    def todo_create(self, **kw):
        # `kw` is data from form
        http.request.env['todo.todos'].sudo().create(kw)
        context = {
            'message': '待辦事項建立完成！'
        }
        # Created successfully page
        return http.request.render('todo.message', context)