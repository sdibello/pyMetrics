"""
Read the metrics from the database.
"""
from prometheus_client import Gauge, start_http_server
import config
import logging
import MySQLdb
import sys
import sched, time
import threading

'''labels here is metadata on how to filter the result data
so here, queue name ( which data is in what queue) and
region are used to allow prometheus to write more rich queries.'''

queue_count = Gauge('open_text_queue', 'current queue count', {'queue_name','region'})

''' add the metric to the list'''
def add_metric(name, reg, value):
    queue_count.labels(region=reg, queue_name=name).set(value)
    return

''' pull the data from MySQL'''
def get_data():
    db = MySQLdb.connect(config.MYSQL_SERVER, config.MYSQL_USER, config.MYSQL_PASSWORD, config.MYSQL_DATABASE)
    cursor = db.cursor()
    cursor.execute('SELECT FORM_TYPE, region, count(1) FROM teddb.RM_TASK where created = 0 and STATUS_ID NOT IN (0,6,7)  group by FORM_TYPE, region order by region')
    return cursor

'''pull the metric every so often'''
def do_periodically():
    cursor = None
    cursor = get_data()
    for row in cursor:
        #print('{0}, {1}, {2}'.format(row[0], row[1], row[2]))
        add_metric(row[0], row[1], int(row[2]))
    print('data')
    cursor = None
    return

if __name__ == '__main__':
    print("starting process")
    cursor = None
    start_http_server(int(config.METRIC_ENDPOINT_PORT))

    while True:
        do_periodically()
        time.sleep(config.SECONDS_TO_PULL_DATA)
