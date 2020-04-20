import binascii as askey # ascii library // didnt actually use this 

message = 'type message here' # type message (must be string for the thing to encode correctly )


print(bin(int.from_bytes(message.encode(), 'big'))) # makes it into a 
