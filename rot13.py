small_letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

cipher = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}"
message = ""
for letter in cipher:
	if letter in small_letters:
		message += small_letters[small_letters.index(letter)+13]    
	elif letter in capital_letters:        
		message += capital_letters[capital_letters.index(letter)+13]    
	else:
		message += letter
print(message)
