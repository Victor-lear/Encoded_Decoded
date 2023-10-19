import Encoded_Decoded
original_string = "M11115Q26@mail.ntust.edu.tw"

password=("")
data=Encoded_Decoded.encoded(original_string,password)
print(data)
print(Encoded_Decoded.decoding(data,password))