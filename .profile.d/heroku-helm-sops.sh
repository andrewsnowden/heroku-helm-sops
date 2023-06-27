export PATH="$PATH:$HOME/.heroku-helm-sops/"

echo "SOURCING heroku-helm-sops.sh"
python .profile.d/load-env.py

echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>"
cat .profile.d/values

source .profile.d/values