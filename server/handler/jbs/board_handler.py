from jbs_handler import jbsHandler
from server.logger import log_server, log_request
from server.processor.jbs.boardprocessor import BoardProcessor
from server.basic.util import get_json_post_data, is_process_success, post_data_format_error
from server.basic.formatter import fill_fail_format, fill_success_format
from flask import make_response

class BoardHandler(jbsHandler):
    __handler_name__ = 'jbsboard'
    __processor__ = BoardProcessor()

    def get_all_boardname(self):
        '''
        Get all boards' name
        methods: GET
        response: a list of names
        '''
        response_value = self.__processor__.get_all_boardname()
        log_request(api_addr="get_all_boardname", response=response_value)
        if is_process_success(response_value):
            return make_response(fill_success_format(response_value))
        else:
            return make_response(fill_fail_format(err_code=response_value))

    def get_all_boards_info(self):
        '''
        Get all boards' detail information
        methods: GET
        response: a list of boards' object
        '''
        ret = self.__processor__.get_all_boards_info()
        log_request(api_addr="get_all_boards_info", response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    def get_board_info(self, boardname):
        '''
        Get a specific board's detail information
        methods: GET
        response: a board info object
        '''
        ret = self.__processor__.get_board_info(boardname)
        log_request(api_addr="get_board_info", request={'boardname': boardname}, response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    def get_all_boards_info_by_section_code(self, section_code):
        '''
        Get all boards' information in a specific section
        param: section_code
        methods: GET
        response: a list of boards' object
        '''
        ret = self.__processor__.get_all_boards_info_by_section_code(section_code)
        log_request(api_addr="get_all_boards_info_by_section_code", request={'section_code': section_code}, response=ret)

        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    def clear_board_unread(self, boardname):
        '''
        Clear unread status of a specific board.
        param: boardname
        methods: GET
        response: success or fail
        '''
        ret = self.__processor__.clear_board_unread(boardname)
        log_request(api_addr="clear_board_unread", request={'boardname': boardname}, response=ret)

        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))
