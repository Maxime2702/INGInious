#!/usr/bin/python3
# -*- coding: utf-8 -*-


from contextlib import redirect_stdout
import subprocess
import unittest
import random
import shlex
import sys
import io

import CorrM01 as corr


class TestM01(unittest.TestCase):
    def test_mission(self):
        ans = _("The expected output is:\n{}\nand you returned:\n{}")
        with open('err.txt', 'w+', encoding="utf-8") as f:
            py_cmd = "python3 mise_en_route.pyc"
            try:
                resproc = subprocess.Popen(shlex.split(py_cmd), universal_newlines=True, stderr=f, stdout=subprocess.PIPE)
                result, tanguy_et_francois = resproc.communicate()
                f.seek(0)
                error = f.read()
            except (IOError, BrokenPipeError):
                result = "Error"
        if error != "":
            raise Exception(error)
        with io.StringIO() as out, redirect_stdout(out):
            corr.squares2()
            corr_ans = out.getvalue()
        if corr_ans != result:
            self.fail(ans.format(corr_ans, result))


if __name__ == '__main__':
    unittest.main()
    sys.stdout = sys.__stdout__

