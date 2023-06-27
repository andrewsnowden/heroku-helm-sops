export PATH="$PATH:$HOME/.heroku-helm-sops/"
export FOO=${FOO:bar}

echo "---> Start SOPS profile.d"

cat $HOME/values.yaml

echo "---> End SOPS profile.d"