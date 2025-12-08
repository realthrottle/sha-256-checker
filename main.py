import hashlib

print("HashMatch by Throttle.")

file = input("Please enter the file path: ")
expectedsha256 = input("Please enter the expected SHA-256 hash: ")
expectedmd5 = input("Please enter the expected MD5 hash: ")

with open(file, "rb") as f:
    sha256hash = hashlib.sha256(f.read()).hexdigest()


with open(file, "rb") as f:
    md5hash = hashlib.md5(f.read()).hexdigest()

print(f"The SHA-256 hash is: {sha256hash}")
print(f"The expected SHA-256 was: {expectedsha256}")
print(f"The MD5 hash is: {md5hash}")
print(f"The expected MD5 was: {expectedmd5}")

if sha256hash == expectedsha256:
    print("The SHA-256 hash matches the expected SHA-256 hash.")
else:
    print("The SHA-256 hash does not match the expected SHA-256 hash.")

if md5hash == expectedmd5:
    print("The MD5 hash matches the expected MD5 hash.")
else:
    print("The MD5 hash does not match the expected MD5 hash.")


print("Thank you for using HashMatch.")
input("Press enter to exit.")
exit()