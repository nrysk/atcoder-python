n, q = map(int, input().split())
queries = [tuple(input().split()) for _ in range(q)]

queries = reversed(queries)
string_buffer = []
cursor = "-1"  # -1: server, 0..n-1: client

for query in queries:
    if query[0] == "1":
        if cursor == query[1]:
            cursor = "-1"
    elif query[0] == "2":
        if cursor == query[1]:
            string_buffer.append(query[2])
    elif query[0] == "3":
        if cursor == "-1":
            cursor = query[1]

print("".join(reversed(string_buffer)))
