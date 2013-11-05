"""
API objects specifications and helper methods
"""
"""
friends api
"""
def fill_friend_object(username, nickname):
    """
    Friend object:
        {'username': username, 'nickname': nickname}

    Returns:
        friend_object (dict)
    """
    return dict(username=username, nickname=nickname)

def fill_friends_list_object(friends_list):
    """
    in get_friends api
    Friends list object:
        {'friends': [friend_object, ...]}
    Returns:
        friends_list_object (dict)
    """
    return dict(friends=friends_list)

def fill_board_object(boardname="", description="", moderators=[], section_code="",
        total_posts=0, last_post_time=0):
    """
    Board object:
        {'boardname': boardname, 'description': description,
        'moderators': [m1username, m2....], 'section_code': code,
        'total_posts': total_posts_num, 'last_post_time': timestamp}
    """
    return dict(boardname=boardname, description=description, moderators=moderators, section_code=section_code,
            total_posts=total_posts, last_post_time=last_post_time)

def fill_board_list_object(board_list):
    """
    Board list object:
        {"boards": ['board object', ...]}
    """
    return dict(boards=board_list)

def fill_user_info_object(username="", nickname="", life_value=0, stay_time="",
        gender="M", signature="", description="", numposts=0):
    """
    User info object
    {'username': username, 'nickname': nickname, 'life_value': value, 'stay_time': time,
        'gender': M or F, 'signature': signature, 'description': description,
         'numposts': numposts}
    """
    return dict(username=username, nickname=nickname, life_value=life_value, stay_time=stay_time,
            gender=gender, signature=signature, description=description, numposts=numposts)

def fill_board_topic_object(offset=0, id='', ownerid='', title='', total_reply=0, unread=False, marked=''):
    return dict(
            offset=offset,
            id=id,
            ownerid=ownerid,
            title=title,
            total_reply=total_reply,
            unread=unread,
        )

def fill_board_topic_list_object(topic_list=[]):
    return dict(topics=topic_list)

def fill_board_name_list_object(namelist=[]):
    return dict(boards=namelist)

def fill_topic_content_object(offset=0, id='', ownerid='', ownername='', title='', 
        boardname='', post_time=0, content='', signature='', bbsname='', perm_del=False, attachments=[]):
    return dict(
            offset=offset,
            id=id,
            ownerid=ownerid,
            ownername=ownername,
            title=title,
            boardname=boardname,
            post_time=post_time,
            content=content,
            signature=signature,
            bbsname=bbsname,
            perm_del=perm_del,
            attachments=attachments
        )

def fill_topic_reply_list_object(reply_list=[]):
    return dict(replies=reply_list)

def fill_post_attachment_object(id='', origname='', mimetype='', filetype='', post_id='', url=''):
    return dict(
            id=id,
            origname=origname,
            mimetype=mimetype,
            filetype=filetype,
            post_id=post_id,
            url=url
        )

def fill_session_object(section_code, section_name):
    """
    Session Object:
    {'section_code': section_code,
     'section_name': section_name}
    """
    return dict(section_code=section_code, section_name=section_name)

def fill_session_list_object(section_list):
    """
    Session List Object:
    {'sessions':
      [section_object, ...]
    }
    """
    return dict(sessions=section_list)

def fill_mail_content_object(id, title, send_time, content, sender, is_reply, is_read):
    """
    Mail Content Object
    {'id': mail_id, 'title': title, 'send_time': timestamp,
     'content': mail_content, 'sender': sender, 'is_reply': is_reply,
     'is_read': is_read}
    """
    return dict(id=id, title=title, send_time=send_time, content=content,
            is_reply=is_reply)

def fill_mail_list_entry_object(id, title, send_time, sender, is_reply, is_read):
    """
    Mail List Entry Object
    {'id': mail_id, 'title': title, 'send_time': timestamp, 'is_reply': is_reply,
    'is_read': is_read}
    """
    return dict(id=id, title=title, send_time=send_time, sender=sender, is_reply=is_reply,
            is_read=is_read)

def fill_mail_list_object(mails):
    """
    Mail List Object
    {'mails': [mail_list_entry_object, ...]}
    """
    return dict(mails=mails)

def fill_mail_box_objects(mail_num):
    """
    Mail Box Object
    {'mail_num': mail_num}
    """
    return dict(mail_num=mail_num)
