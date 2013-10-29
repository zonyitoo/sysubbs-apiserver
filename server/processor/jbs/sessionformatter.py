from server.basic import BasicFormatter
from server.objects import fill_session_list_object, fill_session_object

class SessionFormatter(BasicFormatter):
    """
    SessionFormatter, format jsbbs raw session object into
    session_object
    """
    def format(self):
        section_code = self.raw_data['seccode']
        section_name = self.raw_data['secname']
        return fill_session_object(section_code, section_name)

class SessionListFormatter(BasicFormatter):
    """
    SessionListFormat, format jsbbs raw session list into
    session_list_object
    """
    def format(self):
        sessions = [fill_session_object(session['seccode'], session['secname'])
                for session in self.raw_data]
        return fill_session_list_object(sessions)
