git commit -a -m .
git push origin main
cd ../test-sops
echo "1" >> v.md
git commit -a -m .
git push heroku main