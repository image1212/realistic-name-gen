import httpx

while True:
    name = httpx.get("https://story-shack-cdn-v2.glitch.me/generators/username-generator?").json().get("data").get("name")
    print(name)
    with open("name.txt", "a") as f:
        f.write(f"{name}\n")
