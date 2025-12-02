from collections.abc import Iterable


def run(f: Iterable):
    ans = 0
    count = 50
    for l in f:
        let, *num = l
        number = int("".join(num))
        if let == "L":
            number *= -1
        new_count = count + number
        past_0, new_count = divmod(new_count, 100)
        past_0 = abs(past_0)
        if number < 0:
            if count == 0:
                # starting at 0 and going left should be -1 to what mod said
                past_0 -= 1
            elif new_count == 0:
                # also ending at zero after left should be + 1 to what mod said
                past_0 += 1

        count = new_count
        ans += past_0
    return ans


if __name__ == "__main__":
    assert (
        run(
            [
                "L68",
                "L30",
                "R48",
                "L5",
                "R60",
                "L55",
                "L1",
                "L99",
                "R14",
                "L82",
            ]
        )
        == 6
    )

    assert run(["R200"]) == 2
    assert run(["L200", "R200"]) == 4

    with open("input.txt") as f:
        res = run(f)
    print(res)
