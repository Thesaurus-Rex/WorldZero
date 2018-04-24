import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'snugglebugglewuggles'
    # note - this is hardcoded now an
    # the string literal will change
    # before it goes into production
