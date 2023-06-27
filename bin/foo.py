import os

s = os.popen(f"yq eval '.defaults.env ../values.yaml")
output = s.read()

print("-" * 80)
print(output)