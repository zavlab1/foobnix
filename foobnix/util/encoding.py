import chardet
import logging


def any2unicode(data, code=None):
    if isinstance(data, str):
        if not code:
            code = code_detecter(data)
        data = unicode(data, code)
    return data

def any2utf(data, code=None):
    try:
        data = any2unicode(data, code)
    except:
        logging.error("There is some problems while converting in unicode")
    return data.encode('utf-8')

def code_detecter(data):
    try:
        return chardet.detect(data)['encoding']
    except:
        return 'cp866'