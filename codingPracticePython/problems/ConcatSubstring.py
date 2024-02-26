class ConcatSubstring:

    def run(self):
        words = ["word","good","best","good"]
        s = "wordgoodgoodgoodbestword"
        word_set = set()
        no_words = 0
        for word in words:
            word_set.add(word)
            no_words += 1
        word_length = len(words[0])
        window_length = word_length * no_words
        result = []
        for i in range(len(s) - window_length + 1):
            temp_set = set()
            for j in range(0, no_words):
                start = i + (j * word_length)
                item = s[start: start + word_length]
                if item in word_set:
                    temp_set.add(item)
                else:
                    break
            if len(temp_set) == len(word_set):
                result.append(i)

        print(result)