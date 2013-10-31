# -*- coding: utf-8 -*-
import locale
import datetime
import time

from server.basic import BasicFormatter
from server.objects.spec import fill_mail_content_object, fill_mail_list_entry_object, \
        fill_mail_list_object, fill_mail_box_objects

class MailBoxFormatter(BasicFormatter):
    def format(self):
        return fill_mail_box_objects(mail_num=self.raw_data['total'])

class MailListFormatter(BasicFormatter):
    def format(self):
        mails = [
                fill_mail_list_entry_object(
                    id=data['index'],
                    title=data['title'],
                    sender=data['owner'],
                    send_time=format_mail_time(data['filetime']),
                    is_reply=int(data['flag']) > 31 and True or False,
                    is_read=int(data['flag']) > 0 and True or False
                    )
                for data in self.raw_data
                ]
        return fill_mail_list_object(mails=mails)

class MailContentFormatter(BasicFormatter):
    def format(self):
        return fill_mail_content_object(
                id=self.raw_data['index'],
                title=self.raw_data['title'],
                send_time=format_mail_time(self.raw_data['filetime']),
                content=self.raw_data['content'],
                sender=self.raw_data['owner'],
                is_reply=int(self.raw_data['flag']) > 31 and True or False,
                is_read=int(self.raw_data['flag']) > 0 and True or False
                )

def format_mail_time(t):
    """
    format mail 'filetime' into timestamp
    """
    try:
        # first try to format eng_time:
        # 2012 Dec 07 21:51
        locale.setlocale(locale.LC_TIME, "en_US.UTF8")
        eng_datetime = datetime.datetime.strptime(t, "%Y %b %d %H:%M")
        return time.mktime(eng_datetime.timetuple())
    except:
        # then try to format chn_time
        # 02月09日 09:17
        chn_datetime = datetime.datetime.strptime(t.encode('gbk'), '%m\xd4\xc2%d\xc8\xd5 %H:%M')
        chn_datetime = chn_datetime.replace(year=datetime.datetime.today().year)
        return time.mktime(chn_datetime.timetuple())
