import os
import os.path
import json


def load_values(filename: str, f):
    if os.path.exists(filename):
        print(f">>> Loading environment variables from {filename}")

        s = os.popen(f"yq eval '.defaults.env' {filename}")
        output = s.read()

        for line in output.split("\n"):
            if line:
                key, value = line.split(": ", 1)

                if key not in os.environ:
                    print(f"    Set environment variable '{key}' to {value}")
                    f.write(f'export "{key}"={value}\n')
                else:
                    print(f"    Skipping {key} since it is set in Heroku")
    else:
        print(f">>> Unable to load values from {filename} - file does not exist")


def load_secrets(filename: str, f):
    if os.path.exists(filename):
        print(f">>> Loading secrets from {filename}")
        os.system(
            f"AWS_SECRET_ACCESS_KEY=$SOPS_AWS_SECRET_ACCESS_KEY AWS_ACCESS_KEY_ID=$SOPS_AWS_ACCESS_KEY_ID "
            + f"sops --decrypt {filename} | yq eval .defaults.secrets -o=json >> decrypted.json"
        )

        with open("decrypted.json") as d:
            j = json.loads(d.read())

            for key, value in j.items():
                if key not in os.environ:
                    print(f"    Set secret environment variable '{key}' from SOPS")
                    f.write(f"export '{key}'='{value}'\n")
                else:
                    print(f"    Skipping secret {key} since it is set in Heroku")

        os.remove("decrypted.json")
    else:
        print(f">>> Unable to load secrets from {filename} - file does not exist")


def load():
    with open(".profile.d/values", "w") as f:
        filenames = os.environ.get("HELM_VALUES_FILES", "values.yaml secrets.yaml")
        print(f">>> Load environment values from {filenames}")

        for filename in filenames.split(" "):
            if "secrets" in filename:
                load_secrets(filename, f)
            else:
                load_values(filename, f)


if __name__ == "__main__":
    load()
