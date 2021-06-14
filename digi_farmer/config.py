print ("Content-type:text/html\r\n\r\n")
#import MySQLdb
import pymysql
import sys
try:
    db=pymysql.connect(host="127.0.0.1", user='root',passwd="", db='digi')
except Exception as e:
    sys.exit(e)
    #print e