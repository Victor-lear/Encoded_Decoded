import base64


def encoded(string,password):
    new_string=""
    for i in range(len(string)):
        data=ord(string[i])
        shift=ord(password[i%len(password)])
        shift_data=data+shift
        if(data>=48 and data<=57):
            new_data=(shift_data-48)%10+48
        elif(data>=65 and data<=90):
            new_data=(shift_data-65)%26+65
        elif(data>=97 and data<=122):
            new_data=(shift_data-97)%26+97
        else:
            new_data=data
        new_string+=chr(new_data)
    return new_string

def decoding(string,password):
    new_string=""
    for j in range(len(string)):
        data=ord(string[j])
        shift=ord(password[j%len(password)])
        if(data>=48 and data<=57):
                ori_data = next(i for i in range(48, 58) if (i+shift - 48) % 10 + 48 == data)
        elif(data>=65 and data<=90):
                ori_data=next(i for i in range(65, 91) if (i + shift - 65) % 26 + 65 == data)
        elif(data>=97 and data<=122):
                ori_data=next(i for i in range(97, 123) if (i + shift - 97) % 26 + 97 == data)
        else:
            ori_data=data
        new_string+=chr(ori_data)
    return new_string



