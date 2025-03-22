const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Bounty Contract", function () {
    it("Should create a bounty", async function () {
        const Bounty = await ethers.getContractFactory("Bounty");
        const bounty = await Bounty.deploy();
        await bounty.deployed();

        await bounty.createBounty("Test Bounty", "Solve this challenge", ethers.utils.parseEther("0.1"));
        const count = await bounty.getBountyCount();
        expect(count).to.equal(1);
    });
});