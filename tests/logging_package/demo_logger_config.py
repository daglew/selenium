
import logging
import logging.config


class DemoLoggerConfig:

    def demo_logger_conf(self):
        # create logger
        logging.config.fileConfig("logging")
        logger = logging.getLogger(DemoLoggerConfig.__name__)

        #  logging messagnes
        logger.debug('message debug')
        logger.info('message info')
        logger.warning('message warning')
        logger.error('message error')
        logger.critical('message critical')


run_demo_conf = DemoLoggerConfig()
run_demo_conf.demo_logger_conf()

