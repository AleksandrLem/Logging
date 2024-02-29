import logging
logging.basicConfig(level=logging.DEBUG) # уровень логирования

logging.debug('Это лог уровня DEBUG')
logging.info('Это лог уровня INFO')
logging.warning('Это лог уровня WARNING')
logging.error('Это лог уровня ERROR')
logging.critical('Это лог уровня CRITICAL')

print()
print(logging.DEBUG)
print(logging.INFO)
print(logging.WARNING)
print(logging.ERROR)
print(logging.CRITICAL)



print()
logging.debug('Это лог уровня DEBUG')
logging.info('Это лог уровня INFO')
logging.warning('Это лог уровня WARNING')
logging.error('Это лог уровня ERROR')
logging.critical('Это лог уровня CRITICAL')

print()
logger = logging.getLogger(__name__) # так можно создать логгер
print(logger)
print(dir(logger))

logger = logging.getLogger()
print(logger.parent)
logger = logging.getLogger(__name__)
print(logger.parent)

logger_1 = logging.getLogger('one.two')
print(logger_1.parent)
logger_2 = logging.getLogger('one.two.three')
print(logger_2.parent)

logger = logging.getLogger(__name__)
logger.warning('Предупреждение!')
logger.debug('Отладочная информация')