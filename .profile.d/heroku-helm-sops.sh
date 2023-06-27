export PATH="$PATH:$HOME/.heroku-helm-sops/"

echo "Decrypting secrets using SOPS"
AWS_SECRET_ACCESS_KEY=$SOPS_AWS_SECRET_ACCESS_KEY AWS_ACCESS_KEY_ID=$SOPS_AWS_ACCESS_KEY_ID sops --decrypt secrets.yaml | yq eval .defaults.secrets -o=json >> decrypted.json

echo "Loading environment variables from values.yaml and secrets.yaml"
python .profile.d/load-env.py

rm decrypted.json

source .profile.d/values