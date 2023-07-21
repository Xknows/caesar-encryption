class caesar:
    def generate_key(self, n):
        self.n = n
        key = {}
        Counter = 0
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for letter in letters:
            key[letter] = letters[(Counter + n) % len(letters)]
            Counter += 1
        return key

    def encrypt(self, key, massage):
        self.massage = massage
        cipher = ""
        for letter in massage:
            if letter in key:
                cipher += key[letter]
            else:
                cipher += letter
        return cipher




obj = caesar()
key = obj.generate_key(3)
massage = input("Enter your massage: \n  ").upper()
print("  cipher is: " + obj.encrypt(key, massage))
