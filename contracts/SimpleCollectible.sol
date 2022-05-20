// SPDX-License-Identifier: MIT
pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";


contract SimpleCollectible is ERC721{   //by saying "is" means inheriting from ERC721 contract on openzeppelin so I can use all the functions associated with 
    uint256 public tokenCounter;
     
    constructor() public ERC721 ("Moga", "OGA"){    // I only need to pass 2 arguments to the constructor of the ERC721 which are (name, shortname). I dont need to provide any argument to the constructor of this contract instead.
        tokenCounter = 0;
    }

    function createCollectible(string memory tokenURI) public returns(uint256){
        uint256 newTokenId = tokenCounter;  // define newTokenId equal to the current tokenCounter
        _safeMint(msg.sender, newTokenId);  // mint the nft from the address of the sender of the contract with the tokenid just defined
        _setTokenURI(newTokenId, tokenURI); // set the token URI
        tokenCounter = tokenCounter + 1;    // incremenat the token counter for the next mint
        return newTokenId;
    }
}   