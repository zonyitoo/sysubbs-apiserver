from jbsapitest.user import login, get_friends, get_fav_boards, query_other_user
from server.processor.jbs.userformatter import FriendsListFormatter,\
    UserFavBoardListFormatter, UserInfoFormatter


if __name__ == '__main__':
    login_data = login('okone', '8612001')
    cookie = login_data['cookie']

    get_friends_data = get_friends(cookie)['data']
    print get_friends_data
    friends_list_formater = FriendsListFormatter(get_friends_data)
    print friends_list_formater.format()

    get_fav_boards_data = get_fav_boards(cookie)['data']
    fav_board_list_formatter = UserFavBoardListFormatter(get_fav_boards_data)
    print fav_board_list_formatter.format()

    query_other_user_data = query_other_user('zhongyut')['data']
    user_info_formatter = UserInfoFormatter(query_other_user_data)
    print user_info_formatter.format()
