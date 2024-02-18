class FruitCrush:
    def __init__(self):
        self.dictionary = None
        self.input = None

    def run(self):
        input = [3, 3, 1, 1, 2]
        dictionary = dict()

        for i in range(len(input)):
            if input[i] not in dictionary:
                dictionary[input[i]] = 1
            else:
                dictionary[input[i]] += 1

        key = -1
        removed_keys = []

        for item, count in dictionary.items():
            if key == -1:
                key = item
            else:
                if count > dictionary[key]:
                    dictionary[item] = count - dictionary[key]
                    key = item
                    removed_keys.append(key)
                elif count < dictionary[key]:
                    dictionary[key] = dictionary[key] - count
                    removed_keys.append(item)
                else:
                    removed_keys.append(item)
                    removed_keys.append(key)
                    key = -1

        final = len(dictionary) - len(removed_keys)

        print(final)
        return final
