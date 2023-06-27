import os

s = os.popen(f"yq eval '.defaults.env' values.yaml")
output = s.read()

with open(".profile.d/values", "w") as f:
    for line in output.split("\n"):
        key, value = line.split(": ", 1)

        if key not in os.environ:
            print(f"Set environment variable '${key}' to ${value}")
            f.write(f'export "{key}"={value}\n')
        else:
            print(f"Skipping {key} since it is set in Heroku")
