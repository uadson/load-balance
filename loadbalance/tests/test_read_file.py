def test_read_file():
    file = open('data/input.txt', 'r')
    file.close()
    assert file == file


def test_get_ttask():
    file = open('data/input.txt', 'r')
    ttask = 0
    for f in file.readlines():
        if f == 4:
            ttask = 4
            continue
    assert ttask == ttask


def test_get_umax():
    file = open('data/input.txt', 'r')
    umax = 0
    for f in file.readlines():
        if f == 2:
            umax = 2
    assert umax == umax


def test_get_users():
    file = open('data/input.txt', 'r')
    users = []
    for f in file.readlines():
        num = int(f)
        if num < 4 and num < 2:
            users.append(num)
    assert users == users


def test_balance():

    ttask = 4
    umax = 2
    tick = 0
    cost = 0

    users = [1, 3, 0, 1, 0, 1]

    servers = []

    start = 0
    end = ttask
    diff = 0

    first = users[0]
    tick = sum(users[start: end])
    cost = tick

    if first < umax:
        servers.append(1)

    if first == umax:
        servers.append(umax)

    if first > umax:
        servers.append(umax)
        diff = (first - umax)

    if diff > umax:
        servers.append(umax)
        diff = (diff - umax)

    if diff == umax:
        servers.append(umax)

    start += 1
    for user in users[start: end]:
        if (user + first) > umax:
            servers.append(umax)
            diff = (user + first) - umax

        if diff > umax:
            servers.append(umax)
            diff = diff - umax

        if diff == umax:
            servers.append(umax)

        if diff < umax:
            servers.append(1)

            first = user + first

        end += 1
        tick = tick + sum(users[start: end])
        cost = tick

        for _ in range(1):
            user = sum(users[start: end])
            servers.append(1)
            if (user - 1) > umax:
                servers.append(umax)
                diff = (user - 1) - umax

            if diff > umax:
                servers.append(umax)
                diff = diff - umax

            if diff == umax:
                servers.append(umax)

            if diff < umax:
                servers.append(1)

        start += 1
        tick = tick + sum(users[start:])
        cost = tick

        for _ in range(1):
            user = sum(users[start:])
            if user == umax:
                servers.append(umax)

            if user < umax:
                servers.append(1)

            if user > umax:
                servers.append(umax)
                diff = user - umax

            if diff > umax:
                servers.append(umax)
                diff = diff - umax

            if diff == umax:
                servers.append(umax)

        start += 1
        tick = tick + sum(users[start:])
        cost = tick

        for _ in range(1):
            user = sum(users[start:])
            if user == umax:
                servers.append(umax)

            if user < umax:
                servers.append(1)

            if user > umax:
                servers.append(umax)
                diff = user - umax

            if diff > umax:
                servers.append(umax)
                diff = diff - umax

            if diff == umax:
                servers.append(umax)

        start += 1
        tick = tick + sum(users[start:])
        cost = tick

        for _ in range(1):
            user = sum(users[start:])
            if user == umax:
                servers.append(umax)

            if user < umax:
                servers.append(1)

            if user > umax:
                servers.append(umax)
                diff = user - umax

            if diff > umax:
                servers.append(umax)
                diff = diff - umax

            if diff == umax:
                servers.append(umax)

        start += 1
        tick = tick + sum(users[start:])
        cost = tick

        for _ in range(1):
            user = sum(users[start:])
            if user == umax:
                servers.append(umax)

            if user < umax:
                servers.append(1)

            if user > umax:
                servers.append(umax)
                diff = user - umax

            if diff > umax:
                servers.append(umax)
                diff = diff - umax

            if diff == umax:
                servers.append(umax)

        start += 1
        tick = tick + sum(users[start:])
        cost = tick

        for _ in range(1):
            user = sum(users[start:])
            if user == umax:
                servers.append(umax)

            if user < umax and user > 0:
                servers.append(1)

            if user == 0:
                servers.append(0)

            if user > umax:
                servers.append(umax)
                diff = user - umax

            if diff > umax:
                servers.append(umax)
                diff = diff - umax

            if diff == umax:
                servers.append(umax)

        servers.append(cost)

    test = [
        1,
        2, 2,
        2, 2,
        2, 2, 1,
        1, 2, 1,
        2,
        2,
        1,
        1,
        0,
        15]

    assert test == servers
