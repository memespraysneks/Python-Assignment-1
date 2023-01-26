def sort_alpha(arr, key=lambda _: _):
    arr = arr[:]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j > i and key(arr[i]) > key(arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def sort_bravo(arr, key=lambda _: _):
    if not arr:
        return []
    bot = float("inf")
    top = float("-inf")
    for elt in arr:
        bot = min(bot, key(elt))
        top = max(top, key(elt))
    counts = [0] * (top - bot + 1)
    for elt in arr:
        counts[key(elt) - bot] += 1
    sums = [0]
    for c in counts:
        sums.append(sums[-1] + c)
    counts = [0] * (top - bot + 1)
    ans = [None] * len(arr)
    for elt in arr:
        ans[sums[key(elt) - bot] + counts[key(elt) - bot]] = elt
        counts[key(elt) - bot] += 1
    return ans


def sort_charlie(arr, key=lambda _: _):
    def charlie_helper(arr, lo, hi, key):
        if hi - lo <= 1:
            return
        mid = (lo + hi) // 2
        charlie_helper(arr, lo, mid, key)
        charlie_helper(arr, mid, hi, key)
        if key(arr[mid - 1]) > key(arr[hi - 1]):
            arr[mid - 1], arr[hi - 1] = arr[hi - 1], arr[mid - 1]
        charlie_helper(arr, lo, hi - 1, key)

    arr = arr[:]
    charlie_helper(arr, 0, len(arr), key)
    return arr


def sort_delta(arr, key=lambda _: _):
    arr = arr[:]
    ans = []
    while len(arr) > 0:
        smallest = None
        for e1 in arr:
            for e2 in arr:
                if key(e2) < key(e1):
                    break
            else:
                smallest = e1
        ans.append(smallest)
        arr.remove(smallest)
    return ans
