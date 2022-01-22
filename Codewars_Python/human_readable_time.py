# nlantau, 2020-11-07


def make_readable(seconds):
    sec = 0
    min = 0
    hrs = 0

    for s in range(seconds):
        sec += 1
        if sec == 60:
            min += 1
            sec = 0
        if min == 60:
            hrs += 1
            min = 0
    return (
        "hh:mm:ss".replace("hh", (str(hrs) if hrs > 9 else ("0" + (str(hrs)))))
        .replace("mm", (str(min) if min > 9 else ("0" + (str(min)))))
        .replace("ss", (str(sec) if sec > 9 else ("0" + (str(sec)))))
    )


print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))
