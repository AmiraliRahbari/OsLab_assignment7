import random

def married_random():
    boys = ["ali", "reza", "yasin", "benyamin", "mehrdad", "sjjad", "aidin", "shahin"]
    girls = ["sara", "zari", "neda", "homa", "eli", "goli", "mari", "mina"]

    size1 = len(boys)
    size2 = len(girls)
    random_boys = list()
    random_girls = list()

    while len(random_girls) != size1 or len(random_girls) != size2:
        choose_girl = random.randint(0, size1 - 1)
        if girls[choose_girl] not in random_girls:
            random_girls.append(girls[choose_girl])

        choose_boy = random.randint(0, size1 - 1)
        if boys[choose_boy] not in random_boys:
            random_boys.append(boys[choose_boy])

    for i in range(0, size1 - 1):
        print(f"{random_boys[i]} with {random_girls[i]}")


if __name__ == '__main__':
    married_random()



