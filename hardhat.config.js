require("@nomiclabs/hardhat-waffle");

module.exports = {
  solidity: {
    version: "0.8.1",
  },
  networks: {
    mumbai: {
      url: "https://rpc-mumbai.maticvigil.com/",
      accounts: ['YOUR_PRIVATE_KEY'],
    },
  },
};
