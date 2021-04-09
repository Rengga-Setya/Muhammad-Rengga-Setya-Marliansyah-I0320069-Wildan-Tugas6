for bil in range(10,25):
    if bil > 1:
        for i in range(2, bil):
            if (bil % i) == 0:
                print(bil,"bukan prima")
                break
        else:
            print(bil,"adalah bilangan prima")