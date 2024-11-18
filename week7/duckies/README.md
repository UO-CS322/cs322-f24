# Rubber duckies

This is a complete example of a simple Flask application with a MongoDB backend

* MongoDB notes: [Mongodb.md](./Mongodb.md)
* Docker compose notes: [DockerCompose.md](./DockerCompose.md)

Contents summary:
├── DockerCompose.md : composes the `web` and `db` services in this example
├── Dockerfile : Container for the Flask application
├── app.ini : Configuration used in mulitple components (e.g., port)
├── app.py : Flask application for adding and finding duckies in the databse
├── requirements.txt : required python packages (install in a venv)
├── selenium_test.py : two test cases for the buttons in the application
└── templates
    └── index.html : the single web page in this application; contains Ajax scriptss
