import os
import socket
import paramiko


class SFTP():
    def __init__(self, host, port, username, password):
        self.sftp = None
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.__create_client()

    def close_transport(self):
        self.transport.close()

    def __get_transport(self):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.password)
        return transport

    def __create_client(self):
        self.transport = self.__get_transport()
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    def __connect(self, method, args, **kwargs):
        return self.sftp.__getattribute__(method)(*args, **kwargs)

    def client(self, method, args, **kwargs):
        try:
            if self.transport is None or self.sftp is None:
                self.__create_client()
            return self.__connect(method, args, **kwargs)
        except paramiko.SSHException as e:
            raise ValueError(
                'Error making connection or during {m}:\{e}'.format(
                    m=method, e=e))

    def get_file(self, remote_file, local_path):
        return self.client('get', [remote_file, local_path])

    def upload_file(self, local_file, remote_path):
        return self.client('put', [local_file, remote_path])

    def get_latest_file(self, remote_path):
        latest = 0
        latest_file = None

        for fileattr in self.sftp.listdir_attr(remote_path):

            if fileattr.st_mtime > latest:
                latest = fileattr.st_mtime
                latest_file = fileattr.filename

        if latest_file is not None:
            return os.path.join(remote_path, latest_file)
        else:
            return None
