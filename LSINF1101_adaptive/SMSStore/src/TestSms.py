#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import string
import random
import unicodedata

import CorrSms as corr
import smsStore


def equal_string(uni_string):
    return unicodedata.normalize('NFKD', uni_string)


class TestSms(unittest.TestCase):
    def test_exist(self):
        self.assertTrue((hasattr(smsStore.SMSStore, '__init__') and hasattr(smsStore.SMSStore, '__str__'))
                        and hasattr(smsStore.SMSStore, 'add_new_arrival')
                        and hasattr(smsStore.SMSStore, 'message_count')
                        and hasattr(smsStore.SMSStore, 'get_unread_indexes')
                        and hasattr(smsStore.SMSStore, 'get_message') and hasattr(smsStore.SMSStore, 'delete')
                        and hasattr(smsStore.SMSStore, 'clear'), _("You did not provide the requested methods."))

    def test_addition(self):
        my_inbox = smsStore.SMSStore()
        my_inbox.add_new_arrival("0478123456", "10:43", "I'm leaving from work")
        self.assertEquals(1, my_inbox.message_count(), "You're inbox doesn't contain a message after the addition of"
                                                       " only one.")

    def test_access(self):
        my_inbox = smsStore.SMSStore()
        my_inbox.add_new_arrival("0478123456", "10:43", "I'm leaving from work")
        my_inbox.add_new_arrival("0478123456", "10:45", "What are we eating tonight?")
        my_inbox.add_new_arrival("0478123456", "10:50", "Almost there")
        self.assertEquals(("0478123456", "10:50", "Almost there"), my_inbox.get_message(3), "You're inbox doesn't "
                                                                                            "return the right third sms "
                                                                                            "after addition of 3 sms.")

    def test_deletion(self):
        my_inbox = smsStore.SMSStore()
        my_inbox.add_new_arrival("0478123456", "10:45", "What are we eating tonight?")
        my_inbox.add_new_arrival("0478123456", "10:50", "Almost there")
        my_inbox.add_new_arrival("0478123456", "10:43", "I'm leaving from work")
        my_inbox.delete(1)
        self.assertEquals(("0478123456", "10:50", "Almost there"), my_inbox.get_message(1), "You're inbox doesn't "
                                                                                            "return the right sms "
                                                                                            "after addition of 3 sms "
                                                                                            "and deletion of 1.")

    def test_clear(self):
        my_inbox = smsStore.SMSStore()
        my_inbox.add_new_arrival("0478123456", "10:45", "What are we eating tonight?")
        my_inbox.add_new_arrival("0478123456", "10:50", "Almost there")
        my_inbox.add_new_arrival("0478123456", "10:43", "I'm leaving from work")
        my_inbox.clear()
        self.assertEquals(0, my_inbox.message_count(), "You're inbox doesn't clear all sms properly, it still indicate"
                                                       " to possess at least one sms.")


if __name__ == '__main__':
    unittest.main()
