from commands import commands
from socket import socket

# All these "magic" variables come from reverse engineering the HS100 app, Kasa
# We decompiled it and found their encryption function, then wrote this to try
# to connect and manipulate a HS100, which it does! It appears they use no form
# of authentication or fancy crypto algorithms for encryption

# -85 in the Kasa app, but bytes are unsigned,
# so 256 - 85 = 171
STARTING_BYTE = 171

# 4 hard coded null characters pad each string sent and received.
STARTING_PAD = b"\0\0\0\0"


# Revealed via netcat
PORT = 9999


def encrypt(string):
    """Encrypts a string for transferring to an HS100, they use a simple
        autokey cipher padded by 4 null characters

    Args:
        string: a json string the HS100 should understand

    Returns:
        bytearray: a bytearray of encrypted bytes using the reversed engineered
            autokey cipher
    """
    byte = STARTING_BYTE
    encrypted = bytearray(STARTING_PAD)
    for char in string:
        byte = byte ^ ord(char)
        encrypted.append(byte)
    return encrypted


def decrypt(bytes):
    """Decrypts a bytes sent from an HS100 response

    Args:
        bytes: the raw bytes sent back from an HS100 to decrypt

    Returns:
        str: should be a JSON string if a valid command was sent prior to
            decyption, but could also be empty string if no response.
            Regardless it will now be decrypted
    """
    # chop off the beginning with with padded nulls
    bytes = bytes[len(STARTING_PAD):]

    key = STARTING_BYTE
    decrypted = ""
    for byte in bytes:
        decrypted += chr(key ^ byte)
        key = byte
    return decrypted


def query(host, command):
    """Simply given a host an a shorthand command alias, runs that command and
        returns the response from the HS100

    Args:
        host: string of the valid hostname that is the location of the HS100
        command: string that is a valid command to run, from commands.py

    Returns:
        str: the returned str from the HS100, empty string means an error
    """
    if command not in commands:
        raise Exception("Command {} not known".format(command))

    command_string = commands[command]
    tcp = socket()
    tcp.connect((host, PORT))

    send = encrypt(command_string)
    tcp.send(send)

    # 4KB of data should be enough for any response
    data = tcp.recv(4096)

    # we are done with the query, now we need to parse it
    tcp.close()

    response = decrypt(data)
    return response
