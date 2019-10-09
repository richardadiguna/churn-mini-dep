import os
from sftp.sftp import SFTP


class InferenceSFTP(SFTP):
    def __init__(self, config):
        super(InferenceSFTP, self).__init__(
            config.sftp_host,
            config.sftp_port,
            config.sftp_username,
            config.sftp_password)

    def download_inference_dataset(self, remote_path, local_path):
        latest_file = self.get_latest_file(remote_path)
        download_path = os.path.join(
            local_path, latest_file.split('/')[-1])
        self.get_file(latest_file, download_path)

        return download_path

    def download_inference_model(self, remote_path, local_path):
        print("Downloading dataset...")
        latest_file = self.get_latest_file(remote_path)
        download_path = os.path.join(
            local_path, latest_file.split('/')[-1])

        if os.path.exists(download_path) is False:
            self.get_file(latest_file, download_path)

        return download_path
