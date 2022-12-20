import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S %p', level=logging.DEBUG)
logging.warning("warning massage")
logging.info("info massage")
logging.error("error massage")




