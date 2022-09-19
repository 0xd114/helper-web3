pragma solidity ^0.4.21;

contract xxx {
    uint8 answer;

    function lol() public view returns(bytes32){
        bytes32 hash = 0xaa790a0e56c3d1dcceb22ec33e725624ba465d30b83e78538845c572226ceb3d;
        uint timestamp = 1653079824;
        return keccak256(hash, timestamp);
    }
}