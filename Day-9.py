import copy

def generate_data():
    users = [
        {
            "id": 1,
            "data": {"files": ["a.txt", "b.txt"], "usage": 500}
        },
        {
            "id": 2,
            "data": {"files": ["c.txt"], "usage": 300}
        }
    ]
    return users


def replicate_data(original):
    assignment = original
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)
    return assignment, shallow, deep


def modify_data(data, roll):
    for user in data:
        if roll % 2 == 0:
            user["data"]["files"].append("new.txt")
        else:
            if user["data"]["files"]:
                user["data"]["files"].pop()
        user["data"]["usage"] += 100


def check_integrity(original, shallow, deep):
    leakage = 0
    safe = 0
    overlap = 0

    for i in range(len(original)):
        if original[i]["data"]["files"] == shallow[i]["data"]["files"]:
            leakage += 1

        if original[i]["data"]["files"] != deep[i]["data"]["files"]:
            safe += 1

        set1 = set(original[i]["data"]["files"])
        set2 = set(shallow[i]["data"]["files"])
        overlap += len(set1.intersection(set2))

    return (leakage, safe, overlap)
roll = int(input("Enter Roll Number: "))

original = generate_data()

print("\nBefore Modification")
print(original)

assignment, shallow, deep = replicate_data(original)

modify_data(shallow, roll)

print("\nAfter Shallow Modification")
print("Original:", original)
print("Shallow :", shallow)
print("Deep :", deep)

result = check_integrity(original, shallow, deep)

print("\nIntegrity Report Tuple:")
print(result)