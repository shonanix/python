import logging
import os.path
from logging.handlers import RotatingFileHandler


class Logger(object):
    instance = {}
    def __init__(self, logger, name='logger.log'):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        """
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        # rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # log_path = os.path.dirname(os.getcwd()) + '/Logs/'  # 项目根目录下/Logs 保存日志
        log_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs'))
        log_name = os.path.abspath(os.path.join(log_path, name))
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        # fh = logging.FileHandler(log_name, encoding='utf-8')
        fh = RotatingFileHandler(log_name, maxBytes=1024 * 1024 * 50, backupCount=0, encoding='utf-8')  # 按照文件大小分割
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = logging.Formatter('%(levelname)s %(asctime)s [%(filename)s:%(lineno)d] %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        if name != 'insert.log':
            self.logger.addHandler(ch)

    def get_log(self):
        return self.logger

    def __new__(cls, *args, **kwargs):  # 保证Logger实例为单例模式
        if cls in cls.instance:
            return cls.instance[cls]
        else:
            cls.instance[cls] = super().__new__(cls)
            return cls.instance[cls]


if __name__ == '__main__':
    logger = Logger(__file__, 1,2).get_log()
    logger.error('按照文件大小分割')
    logger.info('成功完成')
