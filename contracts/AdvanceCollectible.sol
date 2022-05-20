pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SimpleCollectible is ERC721{
    uint256 public tokenCounter;
     
    constructor() public ERC721 ("Moga", "OGA"){
        tokenCounter = 0;
    }
