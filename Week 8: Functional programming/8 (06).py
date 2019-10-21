print(
    *list(
        map(
            lambda a, b: int(a) ^ int(b),
            input().split(), input().split()
        )
    )
)
