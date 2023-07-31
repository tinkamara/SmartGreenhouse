import logging


class Log:

    logging.basicConfig(
        filename='log.log',
        format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%d.%m.%y %H:%M:%S',
        level=logging.DEBUG,
        filemode = 'w'
        )

    @staticmethod
    def write_to_log(message, level):
        if level == 2:
            logging.warning(message)
        elif level == 3:
            logging.error(message)
        elif level == 4:
            logging.critical(message)
        elif level == 5:
            logging.debug(message)
        else:
            logging.info(message)
