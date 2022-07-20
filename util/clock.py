from datetime import datetime
import os


def now():
    return datetime.strptime('18/09/19 01:55:19', '%d/%m/%y %H:%M:%S')  if 'TEST' in  os.environ else datetime.utcnow()

