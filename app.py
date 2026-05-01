import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(
    page_title="ArcOS Testnet Hub",
    page_icon="🔵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS to force Desktop Layout and Hide Streamlit UI
# 'min-width' force karne se mobile browser ise desktop screen ki tarah treat karega
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    /* Forces the app to maintain a desktop width on all devices */
    .stApp {
        min-width: 1280px !important;
        overflow-x: auto !important;
    }
    iframe {
        width: 100% !important;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Fully Working HTML/JS with Arc Chain Integration
# Is mein Ethers.js use kiya gaya hai wallet connectivity ke liye
arc_hub_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1280, initial-scale=1">
    <script src="https://cdn.ethers.io/lib/ethers-5.2.umd.min.js" type="application/javascript"></script>
    <style>
        body {
            background-color: #0b0e11;
            color: #eaecef;
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
            margin: 0;
            padding: 40px;
            display: flex;
            justify-content: center;
        }
        .container {
            width: 1100px;
            background: #181a20;
            border: 1px solid #30363d;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.5);
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #30363d;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }
        .btn-connect {
            background-color: #f0b90b;
            color: #000;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            transition: 0.2s;
        }
        .btn-connect:hover { opacity: 0.9; }
        .grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
        }
        .card {
            background: #2b2f36;
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #30363d;
        }
        .card h3 { color: #848e9c; font-size: 14px; margin-top: 0; }
        .card p { font-size: 18px; font-weight: bold; margin-bottom: 0; word-break: break-all; }
        .footer-tag {
            margin-top: 40px;
            text-align: center;
            color: #848e9c;
            font-size: 12px;
            border-top: 1px solid #30363d;
            padding-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 style="margin:0;">ArcOS Testnet Hub</h1>
            <button class="btn-connect" id="connectBtn">Connect Wallet</button>
        </div>

        <div class="grid">
            <div class="card">
                <h3>Network Status</h3>
                <p id="networkStatus">Disconnected</p>
            </div>
            <div class="card">
                <h3>Current Address</h3>
                <p id="walletAddr">Not Connected</p>
            </div>
            <div class="card">
                <h3>Arc Chain ID</h3>
                <p>5042002</p>
            </div>
        </div>

        <div class="footer-tag">
            Full-Stack Infrastructure | Verifiable Work | Arc Testnet
        </div>
    </div>

    <script>
        const connectBtn = document.getElementById('connectBtn');
        const networkStatus = document.getElementById('networkStatus');
        const walletAddr = document.getElementById('walletAddr');

        const ARC_PARAMS = {
            chainId: '0x4CE9B6', // 5042002 in hex
            chainName: 'Arc Testnet',
            nativeCurrency: { name: 'USDC', symbol: 'USDC', decimals: 18 },
            rpcUrls: ['https://rpc.testnet.arc.network'],
            blockExplorerUrls: ['https://testnet.arcscan.app']
        };

        async function init() {
            if (window.ethereum) {
                try {
                    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                    const account = accounts[0];
                    
                    walletAddr.innerText = account.substring(0, 6) + '...' + account.substring(38);
                    
                    // Switch to Arc Testnet automatically
                    try {
                        await window.ethereum.request({
                            method: 'wallet_switchEthereumChain',
                            params: [{ chainId: ARC_PARAMS.chainId }],
                        });
                    } catch (err) {
                        if (err.code === 4902) {
                            await window.ethereum.request({
                                method: 'wallet_addEthereumChain',
                                params: [ARC_PARAMS],
                            });
                        }
                    }
                    
                    networkStatus.innerText = "Connected to Arc";
                    connectBtn.innerText = "Wallet Linked";
                    connectBtn.style.backgroundColor = "#2b2f36";
                    connectBtn.style.color = "#fff";
                    
                } catch (error) {
                    console.error("Connection failed", error);
                }
            } else {
                alert("Please install MetaMask!");
            }
        }

        connectBtn.addEventListener('click', init);
    </script>
</body>
</html>
"""

# 4. Execution
# Height ko bara rakha gaya hai taake vertical scroll smoothly chale
components.html(arc_hub_html, height=1500, scrolling=True)
