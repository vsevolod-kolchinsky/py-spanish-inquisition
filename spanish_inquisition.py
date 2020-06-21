""" Spanish Inquisition Exception """

import abc


class SpanishInquisition(BaseException):
    """ Spanish Inquisition Exception """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = ("Nobody expected!",)

    @abc.abstractmethod
    def fear(self):
        """ a weapon """

    @abc.abstractmethod
    def surprise(self):
        """ a weapon """

    @abc.abstractmethod
    def ruthless_efficiency(self):
        """ a weapon """


if __name__ == "__main__":

    try:
        raise SpanishInquisition()
    except Exception:  # pylint: disable=W0703
        pass
