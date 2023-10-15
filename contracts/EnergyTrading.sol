// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EnergyTrading {
    address public owner;

    struct EnergyProvider {
        address providerAddress;
        string energyType;
        uint256 energyBalance; // In kilowatt-hours (kWh)
        bool isRenewable;
    }

    EnergyProvider[] public energyProviders;

    mapping(address => uint256) public energyBalances;
    mapping(address => bool) public renewableEnergyUsers;

    event EnergyTransferred(address indexed from, address indexed to, uint256 amount);
    event EnergyAdded(address indexed provider, uint256 amount);
    event RenewableEnergyRegistered(address indexed user);
    event RenewableEnergyIncentiveClaimed(address indexed user, uint256 incentiveAmount);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

function registerRenewableEnergyUser() public {
    require(!renewableEnergyUsers[msg.sender], "You are already a registered renewable energy user");
    renewableEnergyUsers[msg.sender] = true;
    emit RenewableEnergyRegistered(msg.sender);
}

    function addEnergy(string memory energyType, uint256 amount, bool isRenewable) public {
        require(amount > 0, "Amount must be greater than zero");
        require(bytes(energyType).length > 0, "Energy type must not be empty");
        energyProviders.push(EnergyProvider(msg.sender, energyType, amount, isRenewable));
        emit EnergyAdded(msg.sender, amount);
    }

    function transferEnergy(address to, uint256 amount) public {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(energyBalances[msg.sender] >= amount, "Insufficient energy balance");
        energyBalances[msg.sender] -= amount;
        energyBalances[to] += amount;
        emit EnergyTransferred(msg.sender, to, amount);
    }

    function claimRenewableEnergyIncentive() public {
        require(renewableEnergyUsers[msg.sender], "Only renewable energy users can claim incentives");
        uint256 incentiveAmount = calculateIncentive();
        require(incentiveAmount > 0, "No incentives available to claim");
        energyBalances[msg.sender] += incentiveAmount;
        emit RenewableEnergyIncentiveClaimed(msg.sender, incentiveAmount);
    }

    function calculateIncentive() private view returns (uint256) {
        uint256 incentive = 0;
        for (uint256 i = 0; i < energyProviders.length; i++) {
            if (energyProviders[i].isRenewable) {
                // Calculate the incentive based on renewable energy usage.
                incentive += (energyProviders[i].energyBalance / 10); // Placeholder calculation
            }
        }
        return incentive;
    }
}
