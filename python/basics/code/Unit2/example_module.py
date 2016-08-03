"""
This module is used to create a method later called by the
hello_fundamentals_with_modules script. It has a single function
hello_fundamentals.
"""

import logging


def hello_fundamentals():
    """
    Function used to print to console "Hello Fundamentals with Modules!".
    """
    print("Hello Fundamentals with Modules!")


def hello_fundamentals_with_recipient(recipient):
    """
    Function used to print to console "Hello {recipient}!".
    :param recipient: The person to say hello to
    """
    print("Hello {}".format(recipient))


class HelloFundamentals(object):
    """
    Class used for Hello Fundamentals with Classes script. Implements a
    hello_fundamentals function that will be called to print out to console.
    """

    def __init__(self, recipient,
                 logger=logging.getLogger("example_module.HelloFundamentals")):
        """
        Default Initializer
        :param recipient: The recipient to say Hello to
        :param logger: The logger.
                       Defaults to getLogger(example_module.HelloFundamentals)
        """
        self.__recipient = recipient
        self.__logger = logger

    def hello_fundamentals(self):
        """
        Function used to print to console "Hello {self.__recipient}"
        """
        self.__logger.debug("Saying Hello to {}".format(self.__recipient))
        print("Hello {}".format(self.__recipient))
