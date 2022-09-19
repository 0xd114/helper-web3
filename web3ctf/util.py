from web3 import Web3, HTTPProvider
from hexbytes import HexBytes
import typing
import binascii
import os

INFURA_API_KEY = os.getenv('INFURA_API_KEY')

providers = dict()
providers['ropsten'] = Web3(HTTPProvider(f'https://ropsten.infura.io/v3/{INFURA_API_KEY}'))


'''return string representations'''
def str_conv(st: str) -> str:

    assert len(st) < 32, "too long :("

    ret = Web3.toHex(st.encode())
    ret = ret + '0' * (66-len(ret))
    return {
        'hex': HexBytes(ret).hex(),
    }


def hex_conv(hx: str) -> typing.Dict[str, typing.Any]:

    return {
        'uint256': Web3.toInt(hexstr=hx),
        'uint8': Web3.toInt(hexstr=hx) % 256
    }


'''return sha3 / keccak of abi.encodePacked values
see: https://web3py.readthedocs.io/en/stable/web3.main.html?highlight=keccak#web3.Web3.solidityKeccak'''
def sha3(types: list[str], values: list[typing.Any]) -> typing.Dict[str, typing.Any]:
    
    types2 = []
    for _type in types:
        val = _type
        if val == 'uint':
            val = 'uint256'
        types2.append(val)
    types = types2
    
    # types_chk = ['uint256', 'uint8', 'bool', 'address', 'bytes32']

    # for _type in types:
    #     assert _type in types_chk, "Unsupported types"

    ret = Web3.solidityKeccak(types, values)
    
    return {
        'hex': ret.hex(),
    }


'''return storage at slot_no of a smart contract address representation'''
def get_storage(addr: str, 
                slot_no: int, 
                provider: str = 'ropsten') -> typing.Dict[str, typing.Any]:

    res = providers[provider].eth.get_storage_at(addr, slot_no)
    return {
        'int': Web3.toInt(res),
        'hex': res.hex()
    }


'''describe important transaction properties'''
def describe_tx(tx_id: str, provider: str = 'ropsten') -> typing.Dict[str, typing.Any]:

    res = providers[provider].eth.getTransaction(tx_id)
    return {
        'from': res['from'],
        'to': res['to'],
        'block_number': res['blockNumber'],
    }


'''describe important block properties'''
def describe_block(blk_id: str, provider: str = 'ropsten') -> typing.Dict[str, typing.Any]:

    res = providers[provider].eth.get_block(blk_id)
    return {
        'hash': res['hash'].hex(),
        'timestamp': res['timestamp']
    }

