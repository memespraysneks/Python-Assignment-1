import datetime
import random


def create_numbers(n, seed=None):
    random.seed(seed)
    ans = []
    for i in range(n):
        ans.append(random.randint(1, 100))
    return ans



def create_invoices(n, seed=None):
    ans = []
    for i in range(n):
        ans.append({
            "id": ans[-1]["id"] + random.randint(2, 50) if ans else 42,
            "product_code": random.randint(100, 999),
            "date":  datetime.date(2022, 1, 1) + datetime.timedelta(days=random.randint(1, 365)),
            "price": random.randint(99, 99 + 10**random.randint(2, 8)) / 100,
        })
    return ans



