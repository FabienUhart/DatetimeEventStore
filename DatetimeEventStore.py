#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3


class DatetimeEventStore:
    def __init__(self):
        """ Create Table if not exist, open the connection """
        try:
            self.conn = sqlite3.connect('EventsTable.db')
            c = self.conn.cursor()
            c.execute(
                '''CREATE TABLE IF NOT EXISTS EVENTS ([generated_id] INTEGER PRIMARY KEY,[Name] text, [Date] date)''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def __del__(self):
        """ close connection"""
        self.conn.close()

    def store_event(self, at, data):
        """ Insert a Event """
        try:
            c = self.conn.cursor()
            sqlite_insert_with_param = """INSERT INTO EVENTS(Name, Date) VALUES (?, ?);"""
            data_tuple = (data, at)
            c.execute(sqlite_insert_with_param, data_tuple)
            self.conn.commit()
        except sqlite3.Error as error:
            print("Failed to insert", error)

    def get_events(self, start, end):
        """ get events """
        strStart = start.strftime("%Y-%m-%d")
        strEnd = end.strftime("%Y-%m-%d")
        c = self.conn.cursor()
        sqlite_events_between = """SELECT NAME, DATE from EVENTS WHERE Date BETWEEN ? and ?;"""
        data_tuple = (strStart, strEnd)
        c.execute(sqlite_events_between, data_tuple)
        rows = c.fetchall()
        self.conn.commit()
        return rows

    def truncate(self):
        """ truncate the table"""
        c = self.conn.cursor()
        sqlite_truncate = '''DELETE FROM EVENTS;'''
        c.execute(sqlite_truncate)
        self.conn.commit()
