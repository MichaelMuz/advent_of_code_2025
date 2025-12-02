from collections.abc import Iterable


def run(f: Iterable):
    ans = 0
    count = 50
    for l in f:
        let, *num = l
        number = int("".join(num))
        if let == "L":
            number *= -1
        count += number
        count %= 100
        if count == 0:
            ans += 1
    return ans


if __name__ == "__main__":
    assert (
        run(
            [
                "50",
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
        == 3
    )

    with open("input.txt") as f:
        res = run(f)
    print(res)
