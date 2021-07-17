birds = ["crows", "pigeon", "eagles", "falcon", "falcon"]
my_bird = []

while birds:
    new_bird = birds.pop()
    if new_bird not in my_bird:
        my_bird.append(new_bird)
        my_bird.sort()

print(my_bird)
