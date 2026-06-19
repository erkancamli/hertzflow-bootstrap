#!/bin/bash

echo "================================="
echo " HERTZFLOW INSTALLER"
echo "================================="

# 1. Python check
if ! command -v python3 &> /dev/null
then
    echo "Python3 not found. Installing..."
    apt update && apt install -y python3 python3-pip
fi

# 2. create CLI folder

# 3. copy run engine
cat > /usr/local/bin/hertzflow/run.py << 'EOF'
import os
import sys

CONFIG = os.path.expanduser("~/.hertzflow_config")

def save(key):
    os.makedirs(os.path.dirname(CONFIG), exist_ok=True)
    open(CONFIG,"w").write(key)

def load():
    return open(CONFIG).read().strip() if os.path.exists(CONFIG) else None

def analyze(contract):
    # MOCK SURF PLACEHOLDER
    if contract.endswith("0"):
        return None

    return {
        "contract": contract,
        "score": 45,
        "status": "WATCH"
    }

def main():
    key = load()
    if not key:
        key = input("Enter Surf API Key: ")
        save(key)

    print("\nHERTZFLOW READY")

    while True:
        c = input("\nEnter contract (or exit): ")
        if c == "exit":
            break

        res = analyze(c)
        if not res:
            print("❌ failed, try again")
            continue

        print("\n--- RESULT ---")
        print(res)

if __name__ == "__main__":
    main()
EOF

# 4. CLI wrapper
cat > /usr/local/bin/hertzflow << 'EOF'
#!/bin/bash
python3 /usr/local/bin/hertzflow/run.py
EOF

chmod +x /usr/local/bin/hertzflow

echo "Installed ✔"
echo "Run: hertzflow"
