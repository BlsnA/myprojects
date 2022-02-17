from cryptography.fernet import Fernet 
# install with 'pip install cryptography'
import random

#Execute once then comment out
# def write_key():
# 	key = Fernet.generate_key()
# 	with open('key.key', 'wb') as key_file:
# 		key_file.write(key)
# write_key()

def load_key():
	key_file = open('key.key', 'rb')
	key = key_file.read()
	key_file.close()
	return key


key = load_key()
fer = Fernet(key)

def view():
	with open('passwords.txt', 'r') as file:
		for line in file.readlines():
			line = line.rstrip()
			username, password = line.split("|")
			print('User:', username, '|', 'Password:', fer.decrypt(password.encode()).decode())


def generator():
	chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!§$%&/()=?€0123456789'
	length = int(input('Input the length of your new password: '))
	password_generated = ''
	for c in range(length):
		password_generated += random.choice(chars)
	print('This is the generated password: ', password_generated)
	yes_no = input('Would you like to use this as your password?' "\n" \
		'Enter \'yes\' to add it to your file' "\n" \
		'Enter \'no\' to exit the program' "\n" )
	if yes_no.lower() == 'yes':
		return password_generated
	if yes_no.lower() == 'no':
		quit()

def add():
	username_new = input('Account Name: ')
	password_new = generator()
	with open('passwords.txt', 'a') as file:
		file.write(username_new + "|" + fer.encrypt(password_new.encode()).decode() + "\n")
	print('The new password has been added to your file.')


while True: 
	mode = input('Would you like to a new passwords or view existing ones?' + "\n" \
		'Enter \'view\' to view existing passwords' "\n" \
		'Enter \'add\' to add a new password to your list' "\n" \
		'Enter \'quit\' to exit the program' "\n")
	mode = mode.lower()
	if mode == 'quit':
		quit()
	elif mode == 'view':
		view()
	elif mode == 'add':
		add()
	else:
		print('Invalid input')
		continue
