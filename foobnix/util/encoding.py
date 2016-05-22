import chardet
import logging


def any2unicode(data, code=None):
    if isinstance(data, str):
        if not code:
            code = code_detecter(data)
        try:
            data = unicode(data, code)
        except:
            logging.error("There is some problems while converting in unicode")
            if code is not 'utf-8':
                logging.info("Try use utf-8")
                data = any2unicode(data, 'utf-8')
    return data

def any2utf(data, code=None):
    data = any2unicode(data, code)
    return data.encode('utf-8')

def code_detecter(data):
    try:
        return chardet.detect(data)['encoding']
    except:
        return 'cp866'