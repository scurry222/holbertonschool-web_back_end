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

PII_FIELDS = ("name", "email", "phone", "ssn", "ip")


class RedactingFormatter(logging.Formatter):
    """ Format and initialize log class """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ initalization """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Use logging methods to format record """
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Use mysql connector python module to connect to MySQL database """
    return mysql.connector.connect(
        host=os.getenv("PERSONAL_DATA_DB_HOST", "root"),
        database=os.getenv("PERSONAL_DATA_DB_NAME"),
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "localhost"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
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
    return re.sub(r"(\w+)=([a-zA-Z0-9@\.\-\(\)\ \:\^\<\>\~\$\%\@\?\!\/]*)",
                  lambda m: m.group(1) + "=" + redaction
                  if m.group(1) in fields else m.group(0), message)


def main() -> None:
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
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
