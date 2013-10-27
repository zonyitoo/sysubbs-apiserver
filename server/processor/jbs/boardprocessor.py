
from jbsprocess import jbsProcessorMixin
from server.basic import BasicBoardProcessor
import requests
from boardformatter import *
from urls import *

class BoardProcessor(BasicBoardProcessor, jbsProcessorMixin):
    """
    BasciBoardProcessor, used to retrieve boards' information
    """
    def get_all_boardname(self):
        """
        retrieve all boards' name
        """
        r = requests.get(url=get_all_boardnames_site, cookies=self.cookie)
        resp = r.json()
        if resp['success']:
            fmt = BoardNamesListFormatter(resp['data'])
            return fmt.format()
        else:
            return resp['code']

    def get_all_boards_info(self):
        """
        get all boards' information
        """
        r = requests.get(url=get_all_boards_info_site)
        resp = r.json()
        if resp['success']:
            fmt = AllSectionBoardInfoListFormatter(resp['data'])
            return fmt.format()
        else:
            return resp['code']

    def get_board_info(self, boardname):
        """
        get a specfic board information
        """

        r = requests.get(url=get_board_info_site, params={'boardname': boardname})
        resp = r.json()
        if resp['success']:
            fmt = BoardInfoFormatter(resp['data'])
            return fmt.format()
        else:
            return resp['code']

    def get_all_boards_info_by_section_code(self, seccode):
        """
        get a specific section's boards
        """
        r = requests.get(get_sec_info_site, params={'sec_code': seccode})
        resp = r.json()
        if resp['success']:
            fmt = SpecificSectionBoardInfoListFormatter(resp['data'])
            return fmt.format()
        else:
            return resp['code']

    def clear_board_unread(self, boardname):
        """
        clear the unread marks for a specific board
        """
        r = requests.post(clear_unread_site, data={'boardname': boardname}, cookies=self.cookie)
        resp = r.json()
        if resp['success']:
            return True
        else:
            return resp['code']

