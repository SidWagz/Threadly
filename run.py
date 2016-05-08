
from threadly import app

if __name__ == "__main__":

    import os

    HOST = os.environ.get('SERVER_HOST', 'localhost')
    PORT = os.environ.get('SERVER_PORT', 8081)

    app.run(HOST, PORT)