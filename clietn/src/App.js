import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import './App.css';
import EnergyTrade from './EnergyTrade.json';

function App() {
  const [account, setAccount] = useState('');
  const [balance, setBalance] = useState(0);
  const [energyType, setEnergyType] = useState('');
  const [amount, setAmount] = useState(0);
  const [isRenewable, setIsRenewable] = useState(false);
  const [recipientAddress, setRecipientAddress] = useState('');
  const [transferAmount, setTransferAmount] = useState(0);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const contractAddress = '0x36a38514b27F0CEf2fc407f91251Cbb2Ee4CE1f8';
  const contractABI = EnergyTrade.abi;

  

  useEffect(() => {
    async function initWeb3() {
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum);
        try {
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          const accounts = await web3.eth.getAccounts();
          setAccount(accounts[0]);
          const balanceInWei = await web3.eth.getBalance(accounts[0]);
          const balanceInEth = web3.utils.fromWei(balanceInWei, 'ether');
          setBalance(balanceInEth);
        } catch (error) {
          console.error('Error connecting to MetaMask:', error);
        }
      }
    }
    initWeb3();
  }, []);

  const handleTransaction = async (action, callback, transactionConfig) => {
    try {
      setLoading(true);
      setError('');
      const web3 = new Web3(window.ethereum);
      const contract = new web3.eth.Contract(contractABI, contractAddress);
      await callback(contract, web3, transactionConfig);
      alert(`${action} successful`);
    } catch (error) {
      console.error(`Error ${action}:`, error);
      setError(`Error ${action}: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };


  const registerAsRenewableEnergyUser = async () => {
    await handleTransaction('Registering as a Renewable User', async (contract, web3, transactionConfig) => {
      await contract.methods.registerRenewableEnergyUser().send({ from: account, ...transactionConfig });
    });
  };

  const addEnergy = async () => {
    await handleTransaction('Adding Energy', async (contract, web3, transactionConfig) => {
      await contract.methods.addEnergy(energyType, amount, isRenewable).send({ from: account, ...transactionConfig });
    });
  };

  const transferEnergy = async () => {
    await handleTransaction('Transferring Energy', async (contract, web3, transactionConfig) => {
      await contract.methods.transferEnergy(recipientAddress, transferAmount).send({ from: account, ...transactionConfig });
    });
  };

  const claimIncentive = async () => {
    await handleTransaction('Claiming Incentive', async (contract, web3, transactionConfig) => {
      await contract.methods.claimRenewableEnergyIncentive().send({ from: account, ...transactionConfig });
    });
  };

  return (
    <div className="App">
      <h1 className='title hoverable'>EnergyChain</h1>
      <div>
        <h2>Connected Account: {account}</h2>
        <p>Balance: {balance} MATIC</p>
      </div>
      <div>
        <button onClick={() => registerAsRenewableEnergyUser()} disabled={loading}>
          Register as Renewable User
        </button>
        <input
          type="text"
          placeholder="Energy Type"
          value={energyType}
          onChange={(e) => setEnergyType(e.target.value)}
        />
        <input
          type="number"
          placeholder="Amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />
        <label>Renewable: </label>
        <input
          type="checkbox"
          checked={isRenewable}
          onChange={(e) => setIsRenewable(e.target.checked)}
        />
        <button onClick={() => addEnergy()} disabled={loading}>
          Add Energy
        </button>
      </div>
      <div>
        <input
          type="text"
          placeholder="Recipient Address"
          value={recipientAddress}
          onChange={(e) => setRecipientAddress(e.target.value)}
        />
        <input
          type="number"
          placeholder="Amount"
          value={transferAmount}
          onChange={(e) => setTransferAmount(e.target.value)}
        />
        <button onClick={() => transferEnergy()} disabled={loading}>
          Transfer Energy
        </button>
      </div>
      <div>
        <button onClick={() => claimIncentive()} disabled={loading}>
          Claim Incentive
        </button>
      </div>
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}

export default App;
