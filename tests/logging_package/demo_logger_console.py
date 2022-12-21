import logging


class DemoLogger:
    def demo_logger_console(self):
        # logger create
        logger = logging.getLogger('sample_log')
        logger.setLevel(logging.INFO)

        # console handler and set the level to info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        # formatter create
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                                      datefmt='%d/%m/%Y %H:%M:%S %p')

        # add formatter to console handler
        chandler.setFormatter(formatter)

        #  add cosole handler
        logger.addHandler(chandler)

        #  mogging messagnes
        logger.debug('message debug')
        logger.info('message info')
        logger.warning('message warning')
        logger.error('message error')
        logger.critical('message critical')


run_demo = DemoLogger()
run_demo.demo_logger_console()

