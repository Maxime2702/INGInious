#!/usr/bin/python3
# -*- coding: utf-8 -*-


class SMSStore:

    def __init__(self):
        self.messages = []

    def __str__(self):
        s = ""
        for m in self.messages:
            s += s + str(m) + "\n"
        return s

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        has_been_viewed = False
        sms = (has_been_viewed, from_number, time_arrived, text_of_SMS)
        self.messages.append(sms)

    def message_count(self):
        return len(self.messages)

    def get_unread_indexes(self):
        l = []
        for i in range(0, len(self.messages)):
            viewed = self.messages[i][0]
            if not viewed: l.append(i + 1)
        return l

    def get_message(self, i):
        if i > self.message_count():
            return None
        else:
            m = self.messages[i - 1]
            self.messages[i - 1] = (True, m[1], m[2], m[3])
            return m[1], m[2], m[3]

    def delete(self, i):
        if i <= self.message_count():
            del self.messages[i - 1]

    def clear(self):
        self.messages = []
