import os

print(f"cwd: ${os.cwd()}")
s = os.popen(f"yq eval '.defaults.env' ../values.yaml")
output = s.read()

print("-" * 80)
print(output)