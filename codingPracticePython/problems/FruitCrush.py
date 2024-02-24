class FruitCrush:
    def __init__(self):
        self.dictionary = None
        self.input = None

    def run(self):
        input = [2,2,2,5,1,2]
        dictionary = dict()
        for i in range(len(input)):
            if input[i] not in dictionary:
                dictionary[input[i]] = 1
            else:
                dictionary[input[i]] += 1

        key = None
        removed_keys = set()

        for item, count in dictionary.items():
            if key == None:
                key = item
            else:
                if count > dictionary[key]:
                    dictionary[item] = count - dictionary[key]
                    key = item
                    removed_keys.add(key)
                elif count < dictionary[key]:
                    dictionary[key] = dictionary[key] - count
                    removed_keys.add(item)
                else:
                    removed_keys.add(item)
                    removed_keys.add(key)
                    key = -1
        for key in removed_keys:
            del dictionary[key]
        final = 0
        for key, value in dictionary.items():
            final += value

        print(final)
        return final
