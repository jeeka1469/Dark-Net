const { ethers } = require("hardhat");

async function main() {
    const Bounty = await ethers.getContractFactory("Bounty");
    const bounty = await Bounty.deploy();
    await bounty.deployed();
    
    console.log(`Bounty contract deployed at: ${bounty.address}`);
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});