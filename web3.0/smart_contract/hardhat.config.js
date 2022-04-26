// https://eth-ropsten.alchemyapi.io/v2/GVov7rAoY75k1OSYR4StoAigJHpK7SOT
require('@nomiclabs/hardhat-waffle');

module.exports = {
  solidity: '0.8.0',
  networks: {
    ropsten: {
      url: 'https://eth-ropsten.alchemyapi.io/v2/GVov7rAoY75k1OSYR4StoAigJHpK7SOT',
      accounts: ['44bba596cd6bb7459c895dcce73d4d8613f8826dc0369bbb3c3055ed0b0b3ed3'],
    },
  },
};