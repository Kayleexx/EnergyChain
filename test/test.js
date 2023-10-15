const { expect } = require("chai");

describe("EnergyTrading Contract", function () {
  it("Should deploy EnergyTrading contract", async function () {
    const EnergyTrading = await ethers.getContractFactory("EnergyTrading");
    const energyTrading = await EnergyTrading.deploy();
    await energyTrading.deployed();

    expect(energyTrading.address).to.not.equal(0);
  });

  it("Should register renewable energy user", async function () {
    const EnergyTrading = await ethers.getContractFactory("EnergyTrading");
    const energyTrading = await EnergyTrading.deploy();
    await energyTrading.deployed();

    const [signer] = await ethers.getSigners();
    await energyTrading.connect(signer).registerRenewableEnergyUser();
    const isRenewableUser = await energyTrading.renewableEnergyUsers(signer.address);
    
    expect(isRenewableUser).to.equal(true);
});


});
