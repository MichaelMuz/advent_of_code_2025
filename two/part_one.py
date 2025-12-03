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

    if lower > upper:
        return []

    print("lower: ", lower, "upper: ", upper)

    lower_str = str(lower)
    first_half_lower = lower_str[: len(lower_str) // 2]

    upper_str = str(upper)
    first_half_upper = upper_str[: len(upper_str) // 2]

    # print(
    #     "first_half_lower: ", first_half_lower, "first_half_upper: ", first_half_upper
    # )

    pos_per_spot = []
    for f_dig_l, f_dig_u in zip(first_half_lower, first_half_upper, strict=True):
        pos_per_spot.append([i for i in range(int(f_dig_l), int(f_dig_u) + 1)])
    print("pos per spot", pos_per_spot)

    return list(
        filter(
            lambda x: lower <= x <= upper,
            (int("".join(map(str, s)) * 2) for s in itertools.product(*pos_per_spot)),
        )
    )


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
        print("invalid ids found:", invs, "invalid ids expected:", exp)
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
        # assert invs == invs_dumb
        if invs != invs_dumb:
            print(chunk)
            print("invs: ", invs, "invs dumb: ", invs_dumb)
            break
        ans.extend(invs)
    print(sum(ans))
