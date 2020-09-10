def main():
    data = {0: .1, 5: .08, 9: .07, 15: .05, 28: .015, 30: .01}
    sorted_key = dict(sorted(data.items(), key = lambda k:k[0], reverse = False))
    val_list = list(sorted_key.values())
    print(sorted_key)
    print(val_list)
    num = 27
    closest_key = min(sorted_key.keys(), key=lambda k: abs(k-num))
    print(closest_key)

    print('Closest key = ' ,closest_key)
    print('Closest value =  ',sorted_key[closest_key])
    while closest_key > num:
        sorted_key.pop(closest_key, None)
        closest_key = min(sorted_key.keys(), key=lambda k: abs(k - num))

    print('The correct key is: ', closest_key)

#######################
if __name__ == '__main__':
    main()

