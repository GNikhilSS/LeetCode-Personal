class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #num1, num2 = int(num1), int(num2)
        #return str(num1 * num2)

        l1 = len(num1)
        l2 = len(num2)
        number1 = 0
        number2 = 0

        for i in range(l1):
            number1 += (ord(num1[i]) - 48) * 10**(l1 - i - 1)

        for j in range(l2):
            number2 += (ord(num2[i]) - 48) * 10**(l1 - i - 1)

        result = number1 * number2
        Text = ""
        while result > 10:
            X = result // 10
            Text += chr(X + 48)
            result %= 10
        Text += chr(result + 48)
        return Text
