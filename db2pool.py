#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import threading
import ibm_db
import time
import Queue


class db2pool(object):
    def __init__(self, host, port, user, password, db, conn_num):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.conn_num = conn_num

        self.conn_queue = Queue.Queue(0)

        for i in range(0, self.conn_num):
            try:
                conn = (ibm_db.connect("DATABASE=" + self.db + ";HOSTNAME=" + self.host + ";PORT=" +
                                           self.port + ";PROTOCOL=TCPIP;UID=" + self.user + ";PWD=" + self.password + ";", "", ""))
                self.conn_queue.put(conn)
            except Exception as e:
                    print e

    def getconnect(self):
        for i in range(0, 5):

            if self.conn_queue.qsize() > 0:
                conn = self.conn_queue.get()

                try:
                    stmt = ibm_db.prepare(
                        conn, "select 1 from sysibm.sysdummy1")
                    ibm_db.execute(stmt)
                    return conn
                 except Exception as e:
                        print e
                        try:
                            conn = (ibm_db.connect("DATABASE=" + self.db + ";HOSTNAME=" + self.host + ";PORT=" +
                                                   self.port + ";PROTOCOL=TCPIP;UID=" + self.user + ";PWD=" + self.password + ";", "", ""))
                            self.conn_queue.put(conn)
                        except Exception as e:
                            print e

                time.sleep(0.5)

            print "get connection error"

        def getclose(self, conn):
            self.conn_queue.put(conn)

    # example
    def work(pool, i):
        # while True:
        conn = pool.getconnect()
        if conn:
            try:
                pass
                stmt = ibm_db.prepare(
                    conn, "select " + str(i) + " from sysibm.sysdummy1")
                ibm_db.execute(stmt)
                result = ibm_db.fetch_both(stmt)
                while (result):
                    print "\nresult[0]=" + str(result[0]) + "++++" + str(conn)
                    result = ibm_db.fetch_both(stmt)
            except Exception as e:
                print e
            finally:
                pass
                pool.getclose(conn)
        time.sleep(5)

if __name__ == "__main__":
        pool = db2pool("172.16.2.9", "60000",
                       "db2inst1", "db2inst1", "secs", 5)
        for i in range(0, 50):
            t = threading.Thread(target=work, args=(pool, i,))
            t.start()
