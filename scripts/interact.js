const { ethers } = require("hardhat");

async function interact() {
    const contractAddress = process.env.CONTRACT_ADDRESS;
    const contractABI = require("../blockchain/abi/Bounty.json"); 
    const provider = new ethers.JsonRpcProvider(process.env.ALCHEMY_RPC_URL);
    const signer = new ethers.Wallet(process.env.PRIVATE_KEY, provider);
    const contract = new ethers.Contract(contractAddress, contractABI, signer);

    // Example: Creating a bounty
    const tx = await contract.createBounty("Test Bounty", "Solve this challenge", ethers.utils.parseEther("0.1"));
    await tx.wait();
    console.log("Bounty created!");

    // Example: Getting bounty count
    const count = await contract.getBountyCount();
    console.log("Total bounties:", count.toString());
}

interact().catch(console.error);