import logging

logging.basicConfig(filename='test_run.txt', 
                    filemode='a+', format='%(created)f - %(levelname)s - %(message)s',
                    level=logging.INFO
                    )


def logger(msg="", error=False):
    if error:
        logging.error(msg)
    else:
        logging.info(msg)
