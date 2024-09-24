import getpass
import hashlib
import os

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS


def Get_User_Credentials():
   username = input("Enter your username: ")
   password = getpass.getpass("Enter your password: ")

   salt = os.urandom(32)
   hashed_password = hashlib.pbkdf2_hmac('md5', password.encode('utf-8'), salt,
                                         100000)

   return username, hashed_password


def pass_user_data():
   aes_key = os.urandom(32)
   key = ECC.generate(curve='P-256')
   signer = DSS.new(key, 'fips-186-3')
   cipher = AES.new(aes_key, AES.MODE_OFB)

   encrypted_data = cipher.encrypt(str(user_passwords).encode())
   hash_obj = SHA256.new(encrypted_data)
   signature = signer.sign(hash_obj)

   with open('user.txt', 'wb') as file:
      file.write(encrypted_data)
      file.write(signature)


if __name__ == "__main__":

   user_passwords = {}

   while True:
      username, password = Get_User_Credentials()

      user_passwords[username] = password

      pass_user_data()

      choice = input("Do you want to continue? (Y/N)")

      if choice.lower() == "n":
         break
      elif choice.lower() == "y":
         continue
      else:
         raise TypeError("Invalid choice")
