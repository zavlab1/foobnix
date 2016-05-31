import chardet
import logging


def any2unicode(data, code=None):
    if isinstance(data, str):
        if not code:
            code = code_detecter(data)
        try:
            data = unicode(data, code)
        except:
            if code is not 'utf-8':
                logging.info("Can't differ coding correctly. Try use utf-8")
                data = any2unicode(data, 'utf-8')
            else:
                logging.error("There is some problems while converting in unicode")
    return data

def any2utf(data, code=None):
    if not data:
        return ""
    data = any2unicode(data, code)
    return data.encode('utf-8')

def code_detecter(data):
    try:
        return chardet.detect(data)['encoding']
    except:
        return 'cp866'