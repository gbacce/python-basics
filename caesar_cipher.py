message = "lbh zhfg hayrnea jung lbh unir yrnearq"

decrypted = "abcdefghijklmnopqrstuvwxyz "
encrypted = "nopqrstuvwxyzabcdefghijklm "

decrypted_list = list(decrypted)
encrypted_list = list(encrypted)
message_list = list(message)

decrypted_message = []


def decryption_function(encrypted_letter):

	number = encrypted_list.index(encrypted_letter)
	decrypted_message.append(decrypted_list[number])

	
for i in range(0, len(message_list)):
	decryption_function(message_list[i])


decryyyyypted_message = "".join(decrypted_message)

print decryyyyypted_message





	# if message_list[i] == encrypted_list.index(message_list[i])
	# 	decrypt = decrypted_list.index()




# for i in range(0, len(decrypted_list))
# 	encrypted_list[i]