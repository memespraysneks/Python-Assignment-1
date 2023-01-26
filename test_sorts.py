import unittest

from data_generators import create_numbers, create_invoices
from sorting_routines import (
    sort_alpha,
    sort_bravo,
    sort_charlie,
    sort_delta,
)


class AntiDiscoveryWrapper:
    class WrapperTestSorts(unittest.TestCase):
        def assertSorted(self, list, key=lambda _: _):
            if key is None:
                key = lambda _: _
            for i in range(len(list) - 1):
                self.assertLessEqual(
                    key(list[i]),
                    key(list[i + 1]),
                    f"{key(list[i])} is not <= {key(list[i + 1])}, so this part of the list is not sorted: list[{max(0, i-4)}:{i+4}] : {list[max(0, i-4):i+4]}",
                )

        def helper(self, generator, n, key=None, seed=None):
            data = generator(n, seed)
            result = self.sort(data, key=key) if key else self.sort(data)
            self.assertSorted(result, key)

        def test_fixed_A_11_numb(self):
            self.helper(create_numbers, 11, key=None, seed="A")

        def test_fixed_A_31_numb(self):
            self.helper(create_numbers, 31, key=None, seed="A")

        def test_fixed_A_101_numb(self):
            self.helper(create_numbers, 101, key=None, seed="A")

        def test_fixed_Z_12_numb(self):
            self.helper(create_numbers, 12, key=None, seed="Z")

        def test_fixed_Z_32_numb(self):
            self.helper(create_numbers, 32, key=None, seed="Z")

        def test_fixed_Z_102_numb(self):
            self.helper(create_numbers, 102, key=None, seed="Z")

        def test_random_5_5_numb(self):
            for i in range(5):
                self.helper(create_numbers, 5, key=None)

        def test_fixed_A_33_invoice(self):
            self.helper(
                create_invoices,
                33,
                key=lambda invoice: int(invoice["date"].strftime("%Y%m%d")),
                seed="A",
            )

        def test_fixed_Z_34_invoice(self):
            self.helper(
                create_invoices,
                34,
                key=lambda invoice: int(invoice["date"].strftime("%Y%m%d")),
                seed="Z",
            )

    class WrapperTestSortsMore(unittest.TestCase):
        def test_random_10_300_numb(self):
            for i in range(10):
                self.helper(create_numbers, 300, key=None)

        def test_random_3_3000_numb(self):
            for i in range(3):
                self.helper(create_numbers, 3000, key=None)

        def test_random_10_300_invoice(self):
            for i in range(10):
                self.helper(
                    create_invoices,
                    300,
                    key=lambda invoice: int(invoice["date"].strftime("%Y%m%d")),
                )


class TestSortAlpha(AntiDiscoveryWrapper.WrapperTestSorts):
    def setUp(self):
        self.sort = sort_alpha


class TestSortBravo(AntiDiscoveryWrapper.WrapperTestSorts):
    def setUp(self):
        self.sort = sort_bravo


class TestSortCharlie(AntiDiscoveryWrapper.WrapperTestSorts):
    def setUp(self):
        self.sort = sort_charlie


class TestSortDelta(AntiDiscoveryWrapper.WrapperTestSorts):
    def setUp(self):
        self.sort = sort_delta
