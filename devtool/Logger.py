class Logger:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

    def write_log(self, message):
        with open(self.log_file_path, 'a') as log_file:
            log_file.write(message + '\n')

