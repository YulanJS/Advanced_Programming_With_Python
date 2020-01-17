# ----------------------------------------------------------------------
# Name:        HW7
# Purpose:     Practice unit testing
#
# Date:       Spring 2019
# ----------------------------------------------------------------------
"""
Unit test functions for hw4.

Test all five functions in hw4.
"""
import unittest
import homework4 as hw4


class TestTopStudents(unittest.TestCase):
    """
    This class contains test cases for top_students function.
    """
    def setUp(self):
        """Create dictionaries for testing."""
        self.empty_class = {}
        self.cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}

    def test_top_students_default_args(self):
        """Test if top_students() works with default argument."""
        self.assertEqual(hw4.top_students(self.cs122), ['Anna', 'Alex', 'Zoe'])

    def test_top_students(self):
        """Continues to test several test cases for top_students()."""
        self.assertEqual(hw4.top_students(self.cs122, 2), ['Anna', 'Alex'])
        self.assertEqual(hw4.top_students(self.cs122, 10),
                         ['Anna', 'Alex', 'Zoe', 'Dan'])
        self.assertEqual(hw4.top_students(self.empty_class, 6), [])

    def test_top_students_org_dict_unmodified(self):
        """
        Test the original dictionaries are unmodified after
        top_students()
        """
        # this funciton is implemented after setUp
        # need to call top_students inside this function
        # to check if dict is unmodified after function call
        hw4.top_students(self.empty_class)
        self.assertEqual(self.empty_class, {})
        hw4.top_students(self.cs122)
        self.assertEqual(self.cs122,
                         {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100})


class TestExtraCredit(unittest.TestCase):
    """
    This class contains test cases for extra_credit function.
    """
    def setUp(self):
        """Create dictionaries for testing."""
        self.empty_class = {}
        self.cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}

    def test_extra_credit_default_args(self):
        """Test if extra_credit() works with default argument."""
        self.assertEqual(hw4.extra_credit(self.cs122),
                         {'Zoe': 91, 'Alex': 94, 'Dan': 80, 'Anna': 101})

    def test_extra_credit(self):
        """Continues to test several test cases for extra_credit()."""
        self.assertEqual(hw4.extra_credit(self.cs122, 2),
                         {'Zoe': 92, 'Alex': 95, 'Dan': 81, 'Anna': 102})
        self.assertEqual(hw4.extra_credit(self.empty_class, 5), {})

    def test_extra_credit_org_dict_unmodified(self):
        """
        Test the original dictionaries are unmodified after
        extra_credit().
        """
        hw4.extra_credit(self.empty_class, 5)
        self.assertEqual(self.empty_class, {})
        hw4.extra_credit(self.cs122, 2)
        self.assertEqual(self.cs122,
                         {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100})


class TestAdjustedGrade(unittest.TestCase):
    """
    This class contains test cases for adjusted_grade function.
    """
    def setUp(self):
        """Create dictionaries for testing."""
        self.iclicker = {'Zoe': 46, 'Alex': 121, 'Ryan': 100, 'Anna': 110,
                         'Bryan': 2, 'Andrea': 110}
        self.exam = {'Dan': 89, 'Ryan': 89, 'Alex': 95, 'Anna': 64,
                     'Bryan': 95, 'Andrea': 86}

    def test_adjusted_grade(self):
        """Test several cases for adjusted_grade()."""
        self.assertEqual(hw4.adjusted_grade(self.iclicker, self.exam),
                         {'Bryan': 95, 'Zoe': 0, 'Anna': 65, 'Alex': 96,
                          'Ryan': 90, 'Andrea': 87, 'Dan': 89})
        self.assertEqual(hw4.adjusted_grade({}, self.exam),
                         {'Ryan': 89, 'Andrea': 86, 'Bryan': 95, 'Anna': 64,
                          'Dan': 89, 'Alex': 95})
        self.assertEqual(hw4.adjusted_grade(self.iclicker, {}),
                         {'Ryan': 1, 'Andrea': 1, 'Bryan': 0, 'Zoe': 0,
                          'Anna': 1, 'Alex': 1})
        self.assertEqual(hw4.adjusted_grade({}, {}), {})

    def test_adjusted_grade_org_dict_unmodified(self):
        """
        Test the original dictionaries are unmodified after
        adjusted_grade().
        """
        hw4.adjusted_grade(self.iclicker, self.exam)
        self.assertEqual(self.iclicker, {'Zoe': 46, 'Alex': 121, 'Ryan': 100,
                                         'Anna': 110, 'Bryan': 2,
                                         'Andrea': 110})
        self.assertEqual(self.exam, {'Dan': 89, 'Ryan': 89, 'Alex': 95,
                                     'Anna': 64, 'Bryan': 95, 'Andrea': 86})


class TestSumOfInverseOdd(unittest.TestCase):
    """
    This class contains test cases for sum_of_inverse_odd function.
    """
    def test_sum_of_inverse_odd(self):
        """Test several cases for sum_of_inverse_odd()."""
        # Better to split into different small functions
        self.assertEqual(hw4. sum_of_inverse_odd(0), 0)
        self.assertEqual(hw4.sum_of_inverse_odd(1), 1.0)
        self.assertEqual(hw4.sum_of_inverse_odd(2), 1.0)
        self.assertAlmostEqual(hw4.sum_of_inverse_odd(3), 1.3333333333333333)
        self.assertAlmostEqual(hw4.sum_of_inverse_odd(2000), 4.435632673335106)


class TestSameLength(unittest.TestCase):
    """
    This class contains test cases for same_length function.
    """
    def test_same_length(self):
        """Test several cases for same_length()."""
        self.assertTrue(hw4.same_length())
        self.assertFalse(hw4. same_length('hi', 'ha', 'it', 'quiet'))
        self.assertTrue(hw4.same_length('hi', 'ha', 'it'))
        self.assertFalse(hw4.same_length('hello', 'ha', 'it', 'ok'))
        self.assertTrue(hw4. same_length('Spartan'))
