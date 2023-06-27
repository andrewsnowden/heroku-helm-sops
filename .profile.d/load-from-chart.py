import os
import os.path
import json

with open(".profile.d/values", "w") as f:
    if os.path.exists("values.yaml"):
        print("Loading environment variables from values.yaml")

        s = os.popen(f"yq eval '.defaults.env' values.yaml")
        output = s.read()

        for line in output.split("\n"):
            if line:
                key, value = line.split(": ", 1)

                if key not in os.environ:
                    print(f"Set environment variable '{key}' to {value}")
                    f.write(f'export "{key}"={value}\n')
                else:
                    print(f"Skipping {key} since it is set in Heroku")

    if os.path.exists("secrets.yaml"):
        print("Loading secrets from secrets.yaml")
        os.system("AWS_SECRET_ACCESS_KEY=$SOPS_AWS_SECRET_ACCESS_KEY AWS_ACCESS_KEY_ID=$SOPS_AWS_ACCESS_KEY_ID sops --decrypt secrets.yaml | yq eval .defaults.secrets -o=json >> decrypted.json")

        with open('decrypted.json') as d:
            j = json.loads(d.read())

            for key, value in j.items():
                if key not in os.environ:
                    print(f"Set secret environment variable '{key}' from SOPS")
                    f.write(f"export '{key}'='{value}'\n")
                else:
                    print(f"Skipping secret {key} since it is set in Heroku")

        os.remove("decrypted.json")