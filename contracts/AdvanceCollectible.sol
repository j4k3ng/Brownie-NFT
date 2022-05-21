pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract AdvanceCollectible is ERC721{
    uint256 public tokenCounter;
     
    constructor() public ERC721 ("Moga", "OGA"){
        tokenCounter = 0;
        
    }

    function createCollectible() public returns(uint256){
        uint256 newTokenId = tokenCounter;  // define newTokenId equal to the current tokenCounter
        _safeMint(msg.sender, newTokenId);  // mint the nft from the address of the sender of the contract with the tokenid just defined
        tokenCounter = tokenCounter + 1;    // incremenat the token counter for the next mint
        return newTokenId;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC721: caller is not owner or not approved");
        _setTokenURI(tokenId, _tokenURI);
    }

}
