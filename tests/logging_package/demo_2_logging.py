import logging
import tests.logging_package.custom_logger as cust_log


class Demo2Logging:

    log = cust_log.custom_logger(log_level=logging.DEBUG)

    def method_1(self):
        self.log.debug('message debug')
        self.log.info('message info')
        self.log.warning('message warning')
        self.log.error('message error')
        self.log.critical('message critical')

    def method_2(self):
        m2log = cust_log.custom_logger(log_level=logging.INFO)
        m2log.debug('message debug')
        m2log.info('message info')
        m2log.warning('message warning')
        m2log.error('message error')
        m2log.critical('message critical')

    def method_3(self):
        self.log.debug('message debug')
        self.log.info('message info')
        self.log.warning('message warning')
        self.log.error('message error')
        self.log.critical('message critical')


demo_logging = Demo2Logging()
demo_logging.method_1()
demo_logging.method_2()
demo_logging.method_3()
cust_log.delete_logs_after_execution()

