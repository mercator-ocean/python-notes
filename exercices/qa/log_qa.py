import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='debug.log',
    format='%(asctime)s %(filename)s %(funcName)s L%(lineno)s: %(message)s'
)
log = logging.getLogger()


def xor(a, b):
    if type(a) is not bool or type(b) is not bool:
        raise TypeError()
    result = a != b
    log.debug('a: %s, b: %s, result: %s', a, b, result)
    return result


# print(xor(True, True))
# print(xor(True, False))
# print(xor(False, True))
# print(xor(False, False))
# print(xor('toto', 'titi'))
