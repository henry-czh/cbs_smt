
#!/bin/env python

import sys
import sqlite3

if __name__=='__main__':

    conn = sqlite3.connect('content-prefs.sqlite')

    c = conn.cursor()

    c.execute("DROP TABLE IF EXISTS prefs")
    c.execute("create table prefs (id INTEGER PRIMARY KEY,groupID INTEGER REFERENCES groups(id),settingID INTEGER NOT NULL REFERENCES settings(id),value BLOB,timestamp INTEGER NOT NULL DEFAULT 0)")
    c.execute("insert into prefs values(1,1,1,'%s','1644818160.331')" % (sys.argv[1]))

    c.execute("DROP TABLE IF EXISTS settings")
    c.execute("create table settings (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
    #c.execute("delete from settings")
    c.execute("insert into settings values(1,'browser.upload.lastDir')")

    c.execute("DROP TABLE IF EXISTS groups")
    c.execute("create table groups (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
    #c.execute("delete from groups")
    c.execute("insert into groups values(1,'127.0.0.1')")

    conn.commit()
    conn.close()
    

