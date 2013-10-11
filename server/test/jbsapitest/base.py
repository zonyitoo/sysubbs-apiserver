"""
The jsbbs api url
"""

host = "http://bbs.sysu.edu.cn"

"""
~~~
session
~~~
"""
get_session_site = host + "/ajax/section/"

"""
~~~
user
~~~
"""
register_site = host + "/ajax/register/"
login_site = host + "/ajax/login/"
logout_site = host + "/ajax/logout/"
get_friends_site = host + "/ajax/friend/"
add_friend_site = host + "/ajax/addfriend/"
del_friend_site = host + "/ajax/delfriend/"
get_fav_boards_site = host + "/ajax/user/fav/"
add_fav_board_site = host + "/ajax/user/addfav/"
del_fav_board_site = host + "/ajax/user/delfav/"
query_other_user_site = host + "/ajax/user/query/"
update_user_info_site = host + "/ajax/user/update/"
get_user_self_info_site = host + "/ajax/user/info/"
get_user_avatar_site = "http://argo.sysu.edu.cn/avatar/%s/"

"""
~~~
board
~~~
"""
get_all_boardnames_site = host + "/ajax/board/all/"
get_all_boards_info_site = host + "/ajax/board/alls/"
get_board_info_site = host + "/ajax/board/get/"
get_sec_info_site = host + "/ajax/board/getbysec/"
clear_unread_site = host + "/ajax/board/clear/"
get_readed_site = host + "/ajax/board/readmark/"

"""
~~~
post
~~~
"""
get_board_topics_site = host + "/ajax/post/list"
get_post_content_site = host + "/ajax/post/get"
get_near_post_site = host + "/ajax/post/nearname/"
get_same_topic_posts_site = host + "/ajax/post/topiclist/"
add_post_site = host + "/ajax/post/add/"
del_post_site = host + "/ajax/post/del/"

"""
~~~
mail
~~~
"""
get_mailbox_info_site = host + "/ajax/mail/mailbox/"
get_maillist_info_site = host + "/ajax/mail/list/"
get_mail_content_site = host + "/ajax/mail/get/"
send_mail_site = host + "/ajax/mail/send/"
del_mail_site = host + "/ajax/mail/del/"

"""
~~~
misc
~~~
"""
get_errcode_site = host + "/ajax/misc/errorcode"
