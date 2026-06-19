import os
import sys

CONFIG_FILE = os.path.expanduser("~/.hertzflow_config")

# -------------------------
# CONFIG
# -------------------------
def save_api_key(key):
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        f.write(key)

def load_api_key():
    if not os.path.exists(CONFIG_FILE):
        return None
    return open(CONFIG_FILE).read().strip()


# -------------------------
# MOCK SURF CALL (REAL PLACEHOLDER)
# -------------------------
def analyze_contract(api_key, contract):
    print("\n[Surf] analyzing contract:", contract)

    # simulate success/failure
    if contract.endswith("0"):
        return None  # fail case

    return {
        "contract": contract,
        "score": 42,
        "status": "WATCH"
    }


# -------------------------
# MAIN LOOP ENGINE
# -------------------------
def main():
    print("\n========================")
    print(" HERTZFLOW CLI SYSTEM")
    print("========================")

    # API KEY CHECK
    api_key = load_api_key()

    if not api_key:
        api_key = input("\nEnter Surf API Key: ")
        save_api_key(api_key)

    print("\nAPI loaded ✔")

    while True:
        contract = input("\nEnter contract (or 'exit'): ")

        if contract.lower() == "exit":
            break

        result = analyze_contract(api_key, contract)

        if result is None:
            print("\n❌ Analysis failed — try another contract")
            continue

        print("\n================ RESULT ================")
        print("Contract:", result["contract"])
        print("Score:", result["score"])
        print("Status:", result["status"])
        print("========================================")


if __name__ == "__main__":
    main()
