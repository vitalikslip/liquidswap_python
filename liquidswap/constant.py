MODULES_ACCOUNT = "0x0163df34fccbf003ce219d3f1d9e70d140b60622cb9dd47599c25fb2f797ba6e"
RESOURCES_ACCOUNT = "0x61d2c22a6cb7831bee0f48363b0eec92369357aece0d1142062f7d5d85c7bef8"
COINS_ACCOUNT = "0x43417434fd869edee76cca2a4d2301e528a1551b1d719b75c350c3c97d15b8b9"

CURVE_UNCORRELATED = f"{MODULES_ACCOUNT}::curves::Uncorrelated"
CURVE_STABLE = f"{MODULES_ACCOUNT}::curves::Stable"
COIN_INFO = "0x1::coin::CoinInfo"
COIN_STORE = "0x1::coin::CoinStore"

NETWORKS_MODULES = {
    "Scripts": f"{MODULES_ACCOUNT}::scripts",
    "Faucet": f"{COINS_ACCOUNT}::faucet",
    "LiquidityPool": f"{MODULES_ACCOUNT}::liquidity_pool",
    "CoinInfo": f"{COIN_INFO}",
    "CoinStore": f"{COIN_STORE}",
}

FEE_PCT = 3
FEE_SCALE = 1000
CURVES = f"{MODULES_ACCOUNT}::curves::Uncorrelated"
