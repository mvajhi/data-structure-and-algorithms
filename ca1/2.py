def main():
    output = str()
    count1 = int(input())
    for i in range(count1):
        clock = clock_to_min(input())
        count2 = int(input())
        for j in range(count2):
            input_clock = input()
            clock1 = clock_to_min(input_clock[:8])
            clock2 = clock_to_min(input_clock[9:])

            if is_ok(clock, clock1, clock2):
                output += "1"
            else:
                output += "0"
        output += "\n"

    print(output)

def is_ok(c, c1, c2):
    return c1 <= c and c <= c2


m_to_min = {"AM": 0, "PM": 12 * 60}


def clock_to_min(clock: str) -> int:
    s_clock = separate_clock(clock)
    if int(s_clock["hour"]) == 12:
        return int(s_clock["min"]) + m_to_min[s_clock["m"]]
    return int(s_clock["min"]) + int(s_clock["hour"]) * 60 + m_to_min[s_clock["m"]]


def separate_clock(clock: str) -> dict:
    return {
        "m": clock.split(" ")[1],
        "hour": clock.split(" ")[0].split(":")[0],
        "min": clock.split(" ")[0].split(":")[1]
    }


if __name__ == "__main__":
    main()
