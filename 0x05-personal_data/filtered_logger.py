#!/usr/bin/env python3
"""
    filtering and logging module
"""
from typing import List
import re
import logging
import os
import csv
import mysql.connector
from mysql.connector import Error

PII_FIELDS = ("name", "email", "phone", "ssn", "ip")


class RedactingFormatter(logging.Formatter):
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Use logging methods to format record """
        logging.basicConfig(format=self.FORMAT, level=record.levelname)
        log = logging.getLogger(record.name)
        log.info(filter_datum(self.fields, self.REDACTION, record.msg,
                              self.SEPARATOR))


def get_db():
    """ Use mysql connector python module to connect to MySQL database """
    return mysql.connector.connect(
        host=os.environ.get("PERSONAL_DATA_DB_HOST"),
        database=os.environ.get("PERSONAL_DATA_DB_NAME"),
        user=os.environ.get("PERSONAL_DATA_DB_USERNAME"),
        password=os.environ.get("PERSONAL_DATA_DB_PASSWORD"),
    )


def get_logger() -> logging.Logger:
    """ Return a logger object """
    log = logging.getLogger("user_data")
    log.setLevel(logging.INFO)
    log.propagate = False
    sh = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    sh.setFormatter(formatter)
    log.addHandler(sh)
    return log


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Redact occurrences of PII values using one regex piece and call """
    return re.sub("(\w+)=([a-zA-Z0-9@\.\-\(\)\ \:\^\<\>\~\$\%\@\?\!\/]+);",
                  lambda m: m.group(1) + "=" + redaction + separator
                  if m.group(1) in fields else m.group(0), message)


def main():
    """ Read and filter data """
    connection = get_db()
    sql_select_Query = "SELECT * FROM users"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    for row in records:
        message = "name={};email={};phone={};ssn={};password={};ip={};\
            last_login={};user_agent={};"\
            .format(row[0], row[1], row[2], row[3], row[4], row[5],
                    row[6], row[7])
        log_record = logging.LogRecord(
            "my_logger", logging.INFO, None, None, message, None, None)
        formatter = RedactingFormatter(PII_FIELDS)
        formatter.format(log_record)

if __name__ == '__main__':
    main()
