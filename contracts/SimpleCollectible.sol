// SPDX-License-Identifier: MIT
pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";


contract SimpleCollectible is ERC721{   //by saying "is" means inheriting from ERC721 contract on openzeppelin so I can use all the functions associated with 
    uint256 public tokenCounter;
     
    constructor() public ERC721 ("Moga", "OGA"){    // 
        tokenCounter = 0;
    }

    function createCollectible(string memory tokenURI) public returns(uint256){
        uint256 newTokenId = tokenCounter;
        _safeMint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);
        tokenCounter = tokenCounter + 1;
        return newTokenId;
    }
}   