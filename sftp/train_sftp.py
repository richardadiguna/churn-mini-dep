import os
from sftp.sftp import SFTP


class TrainSFTP(SFTP):
    def __init__(self, config):
        super(TrainSFTP, self).__init__(
            config.sftp_host,
            config.sftp_port,
            config.sftp_username,
            config.sftp_password)

    def download_train_dataset(self, remote_path, local_path):
        print("Downloading train dataset...")
        latest_file = self.get_latest_file(remote_path)

        download_path = os.path.join(
            local_path, latest_file.split('/')[-1])
        self.get_file(latest_file, download_path)

        return download_path
