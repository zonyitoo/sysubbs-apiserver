
"""
data object specification
"""
section_object = """
                 {'sectionCode': sectionCode, 'sectionName': sectionName}
                 """
friend_ojbect = """
        {'username': username, remark: 'remark'}
        """ # in most cases, the remark may be null string
board_object = """
        {'boardname': boardname, 'boardTitle': title, 'BM': [BM1, BM2, ...], lastPostTime: timestamp,
        'lastPostFile': filename, 'lastPostTitle': posttitle, 'sectionCode': sectionCode, 'totalPost': postnum}
        """ # lastPostFile, lastPost may be null in board api
user_info_object = """
                   """

"""
fill object methods
"""
def fill_friend_obj(username, remark):
    _dict = {}
    _dict['username'] = username
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

"""
errCode and errMsg specification
"""
