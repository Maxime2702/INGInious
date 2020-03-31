#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random
import string

import CorrGUI as corr
import GUI as stu


def callback():
    pass


class TestGUI(unittest.TestCase):
    def setUp(self):
        try:
            button = stu.Button((1, 1), "", callback)
        except (NameError, AttributeError):
            self.fail(_("Does the class `Button` exist?"))
        except Exception as e:
            self.fail(_("You wrongly raised an exception when creating a button: {}('{}')").format(e, type(e).__name__))
        self.assertTrue(hasattr(button, "size"), _("Your button does not have an attribute called 'size'."))
        self.assertTrue(hasattr(button, "label"), _("Your button does not have an attribute called 'label'."))
        self.assertTrue(hasattr(button, "callback"), _("Your button does not have an attribute called 'callback'."))

    def test_constructor_valid(self):
        valid_sizes = [(1, 3), (50, 200), (700, 1000)]
        valid_labels = ["label", "Click this", "I am a button"]
        for size in valid_sizes:
            try:
                button = stu.Button(size, valid_labels[0], callback)
            except AssertionError as e:
                raise e
            except Exception as e:
                self.fail(_("You wrongly raise an exception when creating a button with size {}, label '{}' and a valid"
                            " callback: {}('{}').").format(size, valid_labels[0], type(e).__name__, e))
        for label in valid_labels:
            try:
                button = stu.Button(valid_sizes[0], label, callback)
            except AssertionError as e:
                raise e
            except Exception as e:
                self.fail(_("You wrongly raise an exception when creating a button with size {}, label '{}' and a valid"
                            " callback: {}('{}').").format(valid_sizes[0], label, type(e).__name__, e))

        max_size = 2000
        random_size = (random.randint(0, max_size), random.randint(0, max_size))
        random_label = ''.join(random.choice(string.ascii_letters) for _ in range(5))
        try:
            button = stu.Button(random_size, random_label, callback)
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(_("You wrongly raise an exception when creating a button with size {}, label '{}' and a valid"
                        " callback: {}('{}').").format(random_size, random_label, type(e).__name__, e))

    def test_constructor_invalid(self):
        invalid_sizes = [5, "yo", ValueError(), (1, 5, 7), (1.5, 12.8), (-10, -100)]
        invalid_labels = [12, ("lab", "el"), ValueError()]
        invalid_callbacks = [0, "slt"]
        valid_size = (1, 1)
        valid_label = "Label"
        for size in invalid_sizes:
            try:
                self.assertRaises(ValueError, stu.Button, size, valid_label, callback)
            except AssertionError as e:
                raise AssertionError("{} while creating button with invalid size {}.").format(e, size)
            except Exception as e:
                self.fail(_("You raise an unexpected exception when creating a button with invalid size {} and valid"
                            " label and callback: {}('{}').").format(size, type(e).__name__, e))
        for label in invalid_labels:
            try:
                self.assertRaises(ValueError, stu.Button, valid_size, label, callback)
            except AssertionError as e:
                raise AssertionError("{} while creating button with invalid label {}.".format(e, label))
            except Exception as e:
                self.fail(_("You raise an unexpected exception when creating a button with invalid label '{}' and valid"
                            " size and callback: {}('{}').").format(label, type(e).__name__, e))
        for cb in invalid_callbacks:
            try:
                self.assertRaises(ValueError, stu.Button, valid_size, valid_label, cb)
            except AssertionError as e:
                raise AssertionError("{} while creating button with an invalid callback of type {}.")\
                    .format(e, type(cb).__name__)
            except Exception as e:
                self.fail(_("You raise an unexpected exception when creating a button with invalid callback {} and"
                            " valid size and label: {}('{}').").format(cb, type(e).__name__, e))

    def test_size_setter_valid(self):
        size = (100, 100)
        label = "label"
        max_size = 1000
        try:
            button = stu.Button(size, label, callback)
            random_size = None
            for i in range(15):
                random_size = (random.randint(0, max_size), random.randint(0, max_size))
                button.set_size(random_size)
                self.assertEqual(random_size, button.size, _("Changing the size of the button doesn't change the value"
                                                             " of `size` correctly: {} instead of {}.")
                                 .format(button.size, random_size))
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(_("You wrongly raised an exception while creating a button with valid size {}, label '{}' and a"
                        " valid callback, and changing the size to the valid size {}: {}('{}')")
                      .format(size, label, random_size, type(e).__name__, e))

    def test_size_setter_invalid(self):
        size = (100, 200)
        label = ""
        max_size = 2000
        invalid_sizes = [10, -1, ValueError(), (1.5, 10), (-1, 12)]
        try:
            button = stu.Button(size, label, callback)
            for invalid_size in invalid_sizes:
                self.assertRaises(ValueError, button.set_size, invalid_size)
            for i in range(2):
                invalid_size = (random.uniform(-5, 10), random.uniform(-5, 10))
                self.assertRaises(ValueError, button.set_size, invalid_size)
            for i in range(2):
                invalid_size = (random.randint(-max_size, 0), random.randint(-max_size, 0))
                self.assertRaises(ValueError, button.set_size, invalid_size)
        except AssertionError as e:
            raise AssertionError("{} while setting size to invalid size {}.").format(e, invalid_size)
        except Exception as e:
            self.fail(_("You wrongly raised an exception while creating a button with valid size {}, label {} and a"
                        " valid callback, and changing the size to the invalid size {} : {}('{}').")
                      .format(size, label, invalid_size, type(e).__name__, e))

    def test_label_setter_valid(self):
        size = (100, 100)
        label = "button"
        try:
            button = stu.Button(size, label, callback)
            random_label = None
            for i in range(15):
                random_label = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(0, 10)))
                button.set_label(random_label)
                self.assertEqual(random_label, button.label, _("Changing the label of the button doesn't change the"
                                                               " value of `label` correctly: {} instead of {}.")
                                 .format(button.label, random_label))
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(_("You wrongly raised an exception while creating a button with valid size {}, label '{}' and a"
                        " valid callback, and changing the label to the valid label {}: {}('{}')")
                      .format(size, label, random_label, type(e).__name__, e))

    def test_label_setter_invalid(self):
        size = (100, 200)
        label = "Label"
        invalid_labels = [10, -1, ValueError(), (1.5, 10), (-1, 12)]
        try:
            button = stu.Button(size, label, callback)
            for invalid_label in invalid_labels:
                self.assertRaises(ValueError, button.set_label, invalid_label)
        except AssertionError as e:
            raise AssertionError("{} while setting label to invalid label {}.").format(e, invalid_label)
        except Exception as e:
            self.fail(_("You wrongly raised an exception while creating a button with valid size {}, label {} and a"
                        " valid callback, and changing the label to the invalid label {} : {}('{}').")
                      .format(size, label, invalid_label, type(e).__name__, e))

    def test_callback_setter_valid(self):
        size = (100, 100)
        label = "Button here"

        def cb1():
            return 5

        def cb2():
            x=3

        cb_in_var = callback
        valid_callbacks = [callback, cb1, cb2, cb_in_var]
        try:
            button = stu.Button(size, label, callback)
            for valid_callback in valid_callbacks:
                button.on_click(valid_callback)
                self.assertEqual(valid_callback, button.callback, _("Changing the callback of the button doesn't change"
                                                                    " the value of `callback` correctly: {} instead of "
                                                                    "{}.")
                                 .format(button.callback.__name__, valid_callback.__name__))
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(_("You wrongly raised an exception while creating a button with valid size {}, label '{}' and a"
                        " valid callback, and changing the callback to a valid callback: {}('{}')")
                      .format(size, label, type(e).__name__, e))

    def test_callback_setter_invalid(self):
        size = (100, 200)
        label = "Ok"
        invalid_callbacks = [1, RuntimeError(), "test"]
        try:
            button = stu.Button(size, label, callback)
            for invalid_callback in invalid_callbacks:
                self.assertRaises(ValueError, button.on_click, invalid_callback)
        except AssertionError as e:
            raise AssertionError("{} while setting callback to invalid callback of type {}.")\
                .format(e, type(invalid_callback).__name__)
        except Exception as e:
            self.fail(_("You wrongly raised an exception while creating a button with valid size {}, label {} and a"
                        " valid callback, and changing the callback to an invalid callback: {}('{}').")
                      .format(size, label, type(e).__name__, e))

    def test_call_callback(self):
        size = (1, 100)
        label = "Go"
        return_val_cb = "Callback called"

        def cb():
            return return_val_cb

        try:
            button = stu.Button(size, label, cb)
            if button.clicked() != return_val_cb:
                self.fail(_("Calling the method `clicked()` on your button doesn't call the callback method."))
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(_("You wrongly raised an exception while creating a button with valid size {}, label {} and a "
                        "valid callback, and calling the callback: {}('{}').").format(size, label, type(e).__name__, e))


if __name__ == '__main__':
    unittest.main()
