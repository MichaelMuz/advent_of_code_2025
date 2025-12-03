# each ans is made up of an even number of digits
# so when you see a start number with an odd number of digits starting the real number is the nearest next num digit number
# when you see a end number that has an add amount of digits we round down to num with correct num digits
# now we split the starting and end range in half for example
# 1188511880-1188511890 becomes 11885-11885 and now you see that each digit of a number that conforms to this must be between the corresponding upper and lower digit for example
# first digit must be 1 <= x <= 1 because lower range has one there and so does upper range
# so all possible digits: 1 1 8 8 5 we see there is only one possibility here, 11885 and we of course just write that twice for the answer


import itertools


def get_invalid_ids(lower: int, upper: int):
    lower_digs = len(str(lower))
    if lower_digs % 2 == 1:
        lower = 10**lower_digs

    upper_digs = len(str(upper))
    if upper_digs % 2 == 1:
        upper = 10 ** (upper_digs - 1) - 1

    lower_str = str(lower)
    upper_str = str(upper)

    if lower > upper:
        return []

    first_half_lower = lower_str[: len(lower_str) // 2]
    first_half_upper = upper_str[: len(upper_str) // 2]

    # print("lower: ", lower, "upper: ", upper)

    all_nums = []

    def rec(acc: list, at_lower: bool, at_upper: bool):
        if len(acc) == len(first_half_lower):
            num = int("".join(acc) * 2)
            if lower <= num <= upper:
                all_nums.append(num)
            return

        low = 0
        if at_lower:
            low = int(first_half_lower[len(acc)])
            # print("actual low", low)

        up = 9
        if at_upper:
            up = int(first_half_upper[len(acc)])
            # print("actual up", up)

        for i in range(low, up + 1):
            acc.append(str(i))
            rec(
                acc,
                at_lower and i == low,
                at_upper and i == up,
            )
            acc.pop()

    rec([], True, True)

    return all_nums


def invalid_ids_dumb(lower: int, upper: int):
    acc = []
    for i in range(lower, upper + 1):
        s = str(i)
        if len(s) % 2 == 0 and s[: len(s) // 2] == s[len(s) // 2 :]:
            acc.append(int(s))
    return acc


if __name__ == "__main__":
    exps = [
        [11, 22, [11, 22]],
        [95, 115, [99]],
        [998, 1012, [1010]],
        [1188511880, 1188511890, [1188511885]],
        [222220, 222224, [222222]],
        [1698522, 1698528, []],
        [446443, 446449, [446446]],
        [38593856, 38593862, [38593859]],
    ]
    for lower, upper, exp in exps:
        invs = get_invalid_ids(lower, upper)
        dumb_invs = invalid_ids_dumb(lower, upper)
        # print("invalid ids found:", invs, "invalid ids expected:", exp)
        assert invs == exp == dumb_invs

    assert (
        sum(sum(get_invalid_ids(lower, upper)) for lower, upper, _ in exps)
        == sum(sum(invalid_ids_dumb(lower, upper)) for lower, upper, _ in exps)
        == 1227775554
    )

    # could buffered read but this is just a puzzle
    with open("input.txt") as f:
        line = f.read()

    ans = []
    for chunk in line.split(","):
        lower, _, upper = chunk.partition("-")
        invs = get_invalid_ids(int(lower), int(upper))
        invs_dumb = invalid_ids_dumb(int(lower), int(upper))
        assert invs == invs_dumb
        # if invs != invs_dumb:
        #     print(chunk)
        #     print("lower    : ", [int(lower)] * len(invs))
        #     print("upper    : ", [int(upper)] * len(invs))
        #     print("invs     : ", invs)
        #     print("invs dumb: ", invs_dumb)
        #     break
        ans.extend(invs)
    print(sum(ans))
