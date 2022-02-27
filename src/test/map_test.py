map = {
    "小明": 123,
    "小张": 456
}
print(map)

tuple = ("小明", 2)
map[tuple] = "123"

print(map)

print("小明" in map)
print(len(map))

del map["小明"]
print(map)

print("\n=== for1: ===")
for m in map:
    print(m)

print("\n=== for2: ===")
for k, v in map.items():
    print(k)
    print(v)


print("\n=== for3: ===")
for entry in map.items():
    print(entry[0])
    print(entry[1])



