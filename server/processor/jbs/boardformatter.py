from server.basic import BasicFormatter
from server.objects.spec import *

class BoardNamesListFormatter(BasicFormatter):
    """
    BoardNamesListFormatter, format jsbbs API get_all_boardnames api

    the jbsapi response in this format:
        ['boardname1', 'boardname2', ...]

    Returns:
        boardname_list: in this format:
        {'boards': ['boardname1', 'boardname2', ...]}
    """
    def format(self):
        return fill_board_name_list_object(self.raw_data)

class AllSectionBoardInfoListFormatter(BasicFormatter):
    """
    AllSectionBoardInfoListFormatter, format jsbbs API get_all_boards_info api

    the jsbbs response in this format:
        {'all': ['seccode': seccode, 'secname': secname, 'boards': [{boardinfo1}, {boardinfo2}, ...]],
        'good': [boardname]}

    Returns:
        boardinfo_list: in this format:
        {'boards': [{boardinfo}, ...]}
    """
    def format(self):
        boards = []
        for secs in self.raw_data['all']:
            for board in secs['boards']:
                boards.append(fill_board_object(boardname=board['boardname'],
                    description=board['title'], moderators=board['BM'].split(' '),
                    section_code=secs['seccode'], total_posts=board['total'], 
                    last_post_time=board['lastpost']))
        return fill_board_list_object(boards)

class BoardInfoFormatter(BasicFormatter):
    """
    BoardInfoFormatter, format jsbbs API get_board_info api

    the jsbbs response in this format:
    {boardinfo}

    Returns:
        boardinfo: in this format:
        {boardinfo}
    """

    def format(self):
        return fill_board_object(boardname=self.raw_data['filename'],
                description=self.raw_data['title'],
                moderators=self.raw_data['BM'],
                section_code=self.raw_data['seccode'],
                total_posts=self.raw_data['total'],
                last_post_time=self.raw_data['lastpost'])

class SpecificSectionBoardInfoListFormatter(BasicFormatter):
    """
    SpecificSectionBoardInfoListFormatter, format jsbbs API get_boards_info_by_seccode api

    the jsbbs response in this format:
    [{boardinfo}, {boardinfo}, ...]

    Returns:
        boards: in this format:
        {'boards': [{boardinfo}, {boardinfo}, ...]}
    """
    def format(self):
        boards = [
                fill_board_object(boardname=bobj['filename'],
                    description=bobj['title'],
                    moderators=bobj['BM'],
                    section_code=bobj['seccode'],
                    total_posts=bobj['total'],
                    last_post_time=bobj['lastpost'])     
                for bobj in self.raw_data
            ]
        return fill_board_list_object(boards)
