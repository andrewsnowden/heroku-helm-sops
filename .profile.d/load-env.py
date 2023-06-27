import os
import json

with open(".profile.d/values", "w") as f:
    s = os.popen(f"yq eval '.defaults.env' values.yaml")
    output = s.read()

    for line in output.split("\n"):
        if line:
            key, value = line.split(": ", 1)

            if key not in os.environ:
                print(f"Set environment variable '${key}' to ${value}")
                f.write(f'export "{key}"={value}\n')
            else:
                print(f"Skipping {key} since it is set in Heroku")

    with open('decrypted.json') as d:
        j = json.loads(d.read())

        for key, value in j.items():
            if key not in os.environ:
                print(f"Set secret environment variable '${key}' to ${value}")
                f.write(f'export "{key}"={value}\n')
            else:
                print(f"Skipping secret {key} since it is set in Heroku")
