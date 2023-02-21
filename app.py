from config import *
from api_controllers import (
	user_api,
	auth_api,
	task_api,
	role_api,
	root_api
)


if __name__ == '__main__':
    app.run(port=APP_PORT, debug=True)