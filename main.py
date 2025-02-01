import getpass
import hashlib
import os

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS


def Get_User_Credentials():
   """
   Prompt the user to enter a username and password.
   The password is hashed using MD5 with a randomly generated salt.
   """
   username = input("Enter your username: ")
   password = getpass.getpass("Enter your password: ")

   salt = os.urandom(32) # Generate a random 32-byte salt
   hashed_password = hashlib.pbkdf2_hmac('md5', password.encode('utf-8'), salt, 100000) # Hash the password

   return username, hashed_password


def pass_user_data():
   """
   Encrypt user credentials using AES encryption and sign the data with ECC (Elliptic Curve Cryptography).
   """
   aes_key = os.urandom(32) # Generate a random 32-byte AES key
   key = ECC.generate(curve='P-256') # Generate an ECC key pair
   signer = DSS.new(key, 'fips-186-3') # Create a digital signature scheme
   cipher = AES.new(aes_key, AES.MODE_OFB) # Create an AES cipher object in OFB mode

   encrypted_data = cipher.encrypt(str(user_passwords).encode()) # Encrypt user data
   hash_obj = SHA256.new(encrypted_data) # Generate a SHA-256 hash of encrypted data
   signature = signer.sign(hash_obj) # Sign the hash with ECC

   with open('user.txt', 'wb') as file: # Write encrypted data and signature to a file
      file.write(encrypted_data)
      file.write(signature)


if __name__ == "__main__":

   user_passwords = {} # Dictionary to store usernames and hashed passwords

   while True:
      username, password = Get_User_Credentials() # Get user credentials

      user_passwords[username] = password # Store them in the dictionary

      pass_user_data() # Encrypt and store user data

      choice = input("Do you want to continue? (y/n)")

      if choice.lower() == "n":
         break
      elif choice.lower() == "y":
         continue
      else:
         raise TypeError("Invalid choice")
