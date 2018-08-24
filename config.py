import os
import logging

def get_logging_level():
    try:
        level = os.environ['LOGGING_LEVEL']
        return getattr(logging, level.upper(), logging.INFO)
    except KeyError:
        return logging.INFO

LOGGING_LEVEL = get_logging_level()
LOGGING_FORMAT = '%(asctime)-15s %(name)s %(filename)s %(levelname)s %(message)s'

try:
    OPENTEXT_MYSQL_PASSWORD = os.environ['OPENTEXT_MYSQL_PASSWORD']
except:
    OPENTEXT_MYSQL_PASSWORD = 'puRPLE69caRFLy3Pie'


MYSQL_SERVER = 'tul1mdpdrmy01.corporate.local'
MYSQL_USER = 'ted_ro'
MYSQL_PASSWORD = 'puRPLE69caRFLy3Pie'
MYSQL_DATABASE = 'teddb'
METRIC_ENDPOINT_PORT = '8051'
SECONDS_TO_PULL_DATA = 300