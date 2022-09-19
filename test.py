from web3ctf import util

print(util.str_32bytes("abcde"))

for i in range(0,256):
    if util.uint8_sha3(i)[0] == '0xdb81b4d58595fbbbb592d3661a34cdca14d7ab379441400cbfa1b78bc447c365':
        print(i)