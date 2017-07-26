# coding=utf-8
from flask import Flask, render_template,  request, abort
from flask.ext.restful import Resource, Api
import logging
import random

app = Flask(__name__)
api = Api(app)


@app.route("/")
def index():
    return render_template('index.html')


TODOS = []


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


class TodoList(Resource):

    def get(self):
        # curl -i http://127.0.0.1:5000/todos?page=3&pageSize=10
        # 当前页
        page = request.args.get('page', 1)
        # 页面大小
        page_size = request.args.get('pageSize', 10)
        return get_page_data(int(page), int(page_size)), 201, {'total': len(TODOS), 'page': page}

    def post(self):
        pass


class Todo(Resource):

    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def put(self, todo_id):
        pass

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

# 模拟数据


def mock_data():
    for x in xrange(1, 100):
        todo = {'name': 'build an API %d' % x, 'ranking': random.randint(1, 5)}
        TODOS.append(todo)

# 模拟分页


def get_page_data(page, page_size=10):
    start = (page-1)*page_size
    end = page*page_size
    return TODOS[start:end]


if __name__ == '__main__':
    handler = logging.FileHandler('flask.log', encoding='UTF-8')
    handler.setLevel(logging.DEBUG)
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.config['DEBUG'] = True
    # 设置jinja模板信息,防止和vue模板冲突
    app.jinja_env.variable_start_string = '{{ '
    app.jinja_env.variable_end_string = ' }}'
    mock_data()
    app.run()
