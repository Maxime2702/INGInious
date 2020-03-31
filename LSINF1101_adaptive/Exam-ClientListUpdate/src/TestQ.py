#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q


class TestQ(unittest.TestCase):
    def test_exist_files(self):
        self.assertTrue(hasattr(q, 'files'), "@1@: " + _("You did not name the method as expected."))

    def test_exist_directories(self):
        self.assertTrue(hasattr(q, 'directories'), "@2@: " + _("You did not name the method as expected."))

    def test_exist_subfiles(self):
        self.assertTrue(hasattr(q, 'subfiles'), "@3@: " + _("You did not name the method as expected."))

    def test_files(self):
        ans = "@1@: " + ("Les fichiers contenus ne sont pas tous affichés.")
        corr_ans = corr.files('.')
        stu_ans = q.files('.')
        if len(stu_ans) != len(corr_ans):
            self.fail("@1@: Vous affichez {} noms de fichiers au lieu des 4 attendus.".format(len(stu_ans)))
        self.assertEqual(corr_ans, stu_ans, ans)
        if 'test.txt' not in q.files('.'):
            self.fail("@1@: Affichez-vous les noms des fichiers avec les extensions dans votre liste?")
        stu_ans = q.files('sub2')
        if len(stu_ans) != 0:
            self.fail("@1@: Dans un dossier sans fichiers vous renvoyez {}. Utilisez-vous path correctement?".format(str(stu_ans)))

    def test_dir(self):
        ans = "@2@: " + ("Les dossiers contenus ne sont pas tous affichés.")
        res = ['sub0', 'sub1', 'sub2', 'sub3']
        self.assertEqual(corr.directories('.'), q.directories('.'), ans)
        stu_ans = q.files('sub2')
        if len(stu_ans) != 0:
            self.fail("@2@: Dans un dossier sans dossiers vous renvoyez {}. Utilisez-vous path correctement?".format(str(stu_ans)))

    def test_subfiles(self):
        ans = "@3@: " + ("Les fichiers contenus ne sont pas tous affichés.")
        corr_ans = corr.subfiles('.')
        stu_ans = q.subfiles('.')
        if len(stu_ans) != len(corr_ans):
            self.fail("@3@: Vous affichez {} noms de fichiers au lieu des {} attendus.".format(len(stu_ans), len(corr_ans)))
        self.assertEqual(corr_ans, stu_ans, ans)
        if './sub1/test.txt' not in q.subfiles('.'):
            self.fail("@3@: Affichez-vous les noms des fichiers avec les extensions dans votre liste?")
        stu_ans = q.files('sub2')
        if len(stu_ans) != 0:
            self.fail("@3@: Dans un dossier sans fichiers vous renvoyez {}. Utilisez-vous path correctement?".format(str(stu_ans)))


if __name__ == '__main__':
    unittest.main()
