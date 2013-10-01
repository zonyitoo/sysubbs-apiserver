
"""
data object specification
"""
section_object = """
                 {'sectionCode': sectionCode, 'sectionName': sectionName}
                 """
friend_ojbect = """
        {'userid': userid, remark: 'remark'}
        """ # in most cases, the remark may be null string
board_object = """
        {'boardname': boardname, 'boardTitle': title, 'BM': [BM1, BM2, ...], lastPostTime: timestamp,
        'lastPostFile': filename, 'lastPostTitle': posttitle, 'sectionCode': sectionCode, 'totalPost': postnum}
        """ # lastPostFile, lastPost may be null in board api
user_info_object = """
                   {'userid': userid, 'useralias': userAlias, 'signature': signature,
                    'introduction': introduction, 'gender': gender, 'stayTime': stay,
                    'lastlogin': timestamp, 'postsNum': postNum}
                   """

"""
fill object methods
"""
def fill_friend_obj(userid, remark):
    _dict = {}
    _dict['userid'] = username
    if remark:
        _dict['remark'] = remark

    return _dict

def fill_board_obj(boardname, title, BM, last_post_time, section_code, totalpost, *args, **kwargs):
    """
    last_post_file and last_post is optional
    BM must be an array
    """
    _dict = {}
    _dict['boardname'] = boardname
    _dict['boardTitle'] = title
    _dict['BM'] = BM
    _dict['lastPostTime'] = last_post_time
    _dict['sectionCode'] = section_code
    _dict['totalPost'] = totalpost
    if kwargs.get(last_post_file):
        _dict['lastPostFile'] = last_post_file
    if kwargs.get(last_post):
        _dict['lastPostTitle'] = last_post

    return _dict

def fill_user_obj(userid, useralias, signature, introduction, gender,
        stay_time, lastlogin, posts_num):
    _dict = {}
    _dict['userid'] = userid
    _dict['userAlias'] = useralias
    _dict['signature'] = signature
    _dict['introduction'] = introduction
    _dict['gender'] = gender
    _dict['stayTime'] = stay_time
    _dict['lastlogin'] = lastlogin
    _dict['postsNum'] = posts_num

    return _dict

"""
errCode and errMsg specification
"""
