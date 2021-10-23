# Created by Marcin "Cozoob" Kozub 23.10.2021
import logging

if __name__ == "__main__":
    logging.basicConfig(filename="log.txt", filemode="w", level=0)
    logging.warning("Old Numpy version detected")
    logging.debug("Library check finished")
    logging.warning("No config file detected, using defaults")
    logging.critical("Could not connect to the main database (db: Northwind)")
    logging.critical("Could not connect to the secondary database (db: ClientsMongoDB)")
