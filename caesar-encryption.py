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

    def decrypt(self, key):
        self.key = key
        decryption_key = {}
        for letter in key:
            decryption_key[key[letter]] = letter
        return decryption_key

while True:
    obj = caesar()
    key = obj.generate_key(3)
    x = int(input("------------------------------------------- " +
            "\nEnter your choice:\n   1= encrypt\n   2= decrypt\n"))
    if x == 1:
        massage = input("Enter your massage:\n  ").upper()
        print("  cipher is: " + obj.encrypt(key, massage))

    if x == 2:
        cipher = input("Enter your cipher:\n  ").upper()
        decryption_key = obj.decrypt(key)
        print("  Your original text is: " + obj.encrypt(decryption_key, cipher))