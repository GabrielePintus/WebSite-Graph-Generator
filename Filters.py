import re


class Filters:

    html = "[\w]+\.htm[l]?"
    php  = "[\w]+\.php"


    @staticmethod
    def extension( string ):
        return f'[\w]+\.{string}'

