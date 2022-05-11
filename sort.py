populations = [
    ("DE", 83_000_000),
    ("FR", 67_000_000),
    ("IT", 59_000_000),
    ("LU", 630_000),
    ("BE", 11_000_000),
    ("NL", 17_000_000),
    ("DK", 6_000_000),
    ("CH", 9_000_000),
    ("AT", 9_000_000),
    ("PL", 38_000_000),
    ("CZ", 11_000_000),
]

populations.sort(key = lambda inner:inner[1])

print("Sorted by populations:", populations)
