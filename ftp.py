import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import settings
from transform import process_file


class CustomHandler(FTPHandler):

    def on_connect(self):
        print (f"{self.remote_ip}:{self.remote_port} connected")

    def on_disconnect(self):
        # do something when client disconnects
        pass

    def on_login(self, username):
        # do something when user login
        pass

    def on_logout(self, username):
        # do something when user logs out
        pass

    def on_file_received(self, file):
        if (process_file(file)):
            os.remove(file)

    def on_incomplete_file_received(self, file):
        # remove partially uploaded files
        os.remove(file)


def start_ftp_server():
    authorizer = DummyAuthorizer()
    authorizer.add_user(os.getenv('ftp_user') or 'user', os.getenv('ftp_pwd') or '12345', settings.ftp_path, perm=settings.ftp_permissions)
    authorizer.add_anonymous(settings.ftp_path)
    handler = CustomHandler
    handler.authorizer = authorizer
    handler.banner = settings.ftp_welcome_message
    address = (settings.ftp_ip, settings.ftp_port)
    server = FTPServer(address, handler)

    server.max_cons = settings.ftp_max_cons
    server.max_cons_per_ip = settings.ftp_max_cons_per_ip

    server.serve_forever()


if __name__ == '__main__':
    start_ftp_server()