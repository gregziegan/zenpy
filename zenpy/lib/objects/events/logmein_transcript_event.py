from zenpy.lib.objects.base_object import BaseObject


class LogmeinTranscriptEvent(BaseObject):
    def __init__(self, api=None, **kwargs):
        self.api = api
        self._body = None
        self._type = None
        self.id = None

        for key, value in kwargs.iteritems():
            setattr(self, key, value)
