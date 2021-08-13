import tictactoe as t

test_cases = [
    {
        "board": [
            [t.EMPTY, t.EMPTY, t.EMPTY],
            [t.EMPTY, t.EMPTY, t.EMPTY],
            [t.EMPTY, t.EMPTY, t.EMPTY],
        ],
        "player": t.X
    },
    {
        "board": [
            [t.EMPTY, t.EMPTY, t.EMPTY],
            [t.EMPTY, t.EMPTY, t.EMPTY],
            [t.EMPTY, t.EMPTY, t.X],
        ],
        "player": t.O
    },
    {
        "board": [
            [t.X, t.EMPTY, t.EMPTY],
            [t.EMPTY, t.EMPTY, t.EMPTY],
            [t.EMPTY, t.EMPTY, t.EMPTY],
        ],
        "player": t.O
    },
    {
        "board": [
            [t.EMPTY, t.EMPTY, t.EMPTY],
            [t.X, t.EMPTY, t.EMPTY],
            [t.EMPTY, t.EMPTY, t.EMPTY],
        ],
        "player": t.O
    },
    {
        "board": [
            [t.EMPTY, t.EMPTY, t.EMPTY],
            [t.EMPTY, t.X, t.EMPTY],
            [t.EMPTY, t.EMPTY, t.EMPTY],
        ],
        "player": t.O
    },
    {
        "board": [
            [t.EMPTY, t.EMPTY, t.O],
            [t.EMPTY, t.X, t.EMPTY],
            [t.EMPTY, t.EMPTY, t.EMPTY],
        ],
        "player": t.X
    },
]
