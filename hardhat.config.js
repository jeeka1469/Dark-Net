require("dotenv").config();
require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  networks: {
    sepolia: {
      url: "https://eth-sepolia.g.alchemy.com/v2/cZXSGH6YWJZOqoLN-0G7vp5R_Anz48OH", 
      accounts: [process.env.PRIVATE_KEY], 
    },
  },
  solidity: "0.8.18",
};