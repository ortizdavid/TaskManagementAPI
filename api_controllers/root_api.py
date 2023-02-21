from flask import send_file
from config import app

class RootAPI:

    @app.route('/', methods=['GET'])
    @app.route('/api', methods=['GET'])
    def root():
        return  """
            <h1>REST API for Task Management</h1>

            <p>Basic End Points:</p>
            <ul>
                <li>Users: /api/tasks</li>
                <li>Tasks: /api/tasks</li>
                <li>Roles: /api/roles</li>
                <li>Login: /api/auth/login</li>
                <li>Logout: /api/auth/logout</li>
            </ul>

            <p>Postman Collections:</p>
            <ul>
                <li>Postman Collection <a href="/postman-collection">Download</a></li>
                <li>Postman Test Run <a href="/postman-test">Download</a></li>
            </ul>
        """


    @app.route('/postman-collection', methods=['GET'])
    def postman_collection():
        return send_file("__postman_collections__/postman_collection.json", as_attachment='postman-collection.json')


    @app.route('/postman-test', methods=['GET'])
    def postman_test():
        return send_file("__postman_collections__/postman_test_run.json", as_attachment='postman-test.json')
