# heroku-helm-sops

A Heroku buildpack that installs Mozilla SOPS and will load environment variables
from them `values.yaml` and `secrets.yaml` in your Helm chart. 

You must specify the AWS account for SOPS to use with the following variables:
`SOPS_AWS_SECRET_ACCESS_KEY` and `SOPS_AWS_ACCESS_KEY_ID`.

This buildpack also requires the `heroku-community/awscli` buildpack.

To add this buildpack to your Heroku app run:

- `heroku buildpacks:add heroku-community/awscli`
- `heroku buildpacks:add https://github.com/yoco-tech/heroku-helm-sops.git`
