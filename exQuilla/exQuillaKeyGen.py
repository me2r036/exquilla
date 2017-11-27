#!/usr/bin/env python
# encoding: utf-8
import sys
import hashlib

class CrackExQuilla(object):
    def __init__(self, email, expired_date):
        self.email = email
        self.expired_date = expired_date
        self.license = None

    def crack(self):
       str_tmp = "%s,%s,%s,%s" % ("EX1", self.email, self.expired_date, "356B4B5C")
       str_md5 = self._md5(str_tmp)
       self.license = "%s,%s,%s,%s" % ("EX1", self.email, self.expired_date, str_md5)
       return self.license

    def _md5(self, str_tmp):
        m = hashlib.md5()
        m.update(str_tmp)
        return m.hexdigest()

def usage(cmd):
    print '-' * 50
    print "%s email_address expired_date" % cmd
    print "usage: \n%s x@xsec.io 2016-12-30" % cmd
    print '-' * 50

if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage(sys.argv[0])
        sys.exit()
    email = sys.argv[1]
    expired_date = sys.argv[2]
    crack_exquilla = CrackExQuilla(email, expired_date)
    license = crack_exquilla.crack()
    print license
