
class BasicFormatter(object):
    """
    Basic Formatter classes for the data retrieve from the server
    to format data into uniform data json object
    """
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def format(self):
        """
        format the raw_data into the specif json object
        """
        raise NotImplementedError()
