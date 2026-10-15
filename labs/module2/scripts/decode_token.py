import base64

api = "3PDW8NHx1/rS+96IpYyB/IeOu7PSm5G6g/G9jqjkkr+ig4imrYWGs57kgYuniA=="
decoded = base64.b64decode(api)
xor = b""
for x in decoded:
        xor += (x ^ 168).to_bytes(1, 'big')
xor2 = b""
for i in range(len(xor)):
        if i%2 == 0:
                xor2 += (xor[i] ^ 76).to_bytes(1, 'big')
        else:
                xor2 += (xor[i] ^ 97).to_bytes(1, 'big')
print(xor2)

