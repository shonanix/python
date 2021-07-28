import configparser
import os
import sys


def process_path():
    if hasattr(sys, '_MEIPASS'):
        ap = os.path.dirname(os.path.realpath(sys.executable))
    else:
        ap, filename = os.path.split(os.path.abspath(__file__))
    return ap


def readconfig():
    file_path = process_path()
    file_path = os.path.dirname(file_path)
    file_path = os.path.join(os.path.join(file_path, "config"), 'config.ini')
    config = configparser.ConfigParser()
    try:
        config.read(file_path, encoding="utf-8-sig")
    except:
        raise FileExistsError('没有config配置文件')
    return config
