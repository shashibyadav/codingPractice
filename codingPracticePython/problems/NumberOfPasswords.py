class NumberOfPasswords:
    def run(self):
        # password = "abc"
        # password = "aaaa"
        password = "abaa"
        dictionary = dict()
        for i in range(2, len(password) + 1):
            counter = 0
            for j in range(0, len(password) - i + 1):
                # key = str(i) + "-" + str(j)
                temp_pass = password[j : j + i]
                reverse_pass = temp_pass[::-1]
                if temp_pass in dictionary:
                    counter
                    continue
                if temp_pass != reverse_pass:
                    counter += 1

        print(total_counter)
