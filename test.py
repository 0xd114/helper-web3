from web3ctf import util

print(util.str_conv("abcde"))

for i in range(0,256):
    if util.sha3(['uint8'], [i])['hex'] == '0xdb81b4d58595fbbbb592d3661a34cdca14d7ab379441400cbfa1b78bc447c365':
        print(i)

print(util.get_storage('0x7580DECF0b54F9DfBFcf927a2298f04C8bFB53Df', 0))
print(util.describe_tx('0xa8c17c5ac1b1ec07683814e6daee062cc78a7394fcc91848b484f73e01bb485a'))
print(util.describe_block(12973093))

print(util.hex_conv(util.sha3(['bytes32', 'uint256'], ['0xaa790a0e56c3d1dcceb22ec33e725624ba465d30b83e78538845c572226ceb3d', 1653079824])['hex']))
