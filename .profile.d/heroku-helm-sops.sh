export PATH="$PATH:$HOME/.heroku-helm-sops/"

#yaml_file="$HOME/values.yaml"
yaml_file='/Users/andrew/dev/test-sops/values.yaml'

variables=$(yq eval '.defaults.env' "$yaml_file")

# No idea what IFS is originally - but set it to something it will never match
IFS="&&&&&&&&"
original_ifs=$IFS

while read -r line
do
  echo "LINE: $line"
  IFS=": "
  set -- $line
  echo "WHAT??? '$1'='$2'"
  IFS=original_ifs
  export FOO="in loop"
done <<< $(yq eval '.defaults.env' "$yaml_file")

echo "quux is $FOO"

# Example line to split
line="key1: value1: key2: multi word: key3: value3"

# Save the original IFS value
original_ifs=$IFS

# Set the IFS to ": "
IFS=": "

# Split the line into fields
set -- $line

# Access the individual fields
echo "Field 1: $1"
echo "Field 2: $2"
echo "Field 3: $3"
echo "Field 4: $4"
echo "Field 5: $5"
echo "Field 6: $6"

# Reset the IFS to its original value
IFS=$original_ifs

#while read -r key value; do
#  # Set the environment variable
#  v=${value# }
#  v=${v#\"}
#  v=${v%\"}
#
#  echo "-----"
#  echo "key=${key} value=${v}"
#  declare "$key"="$v"
#  export "$key"
#  echo $key
##  export "$key"="$v"
#  export LAST='$v'
#  export LOOP='loop'
#
##  export $key=$value
#  #export "$key"="$value"
#done

#export QUUX="manual"
#
#echo $FOO
#echo $BAR
#echo $QUUX
#echo $LAST
#echo $LOOP

#ITEMS=$(yq ".defaults.env" "$HOME/values.yaml")
#VALUES=$(yq ".defaults.env[]" "$HOME/values.yaml")
#KEYS=$(yq ".defaults.env | keys" "$HOME/values.yaml")
#
#
#echo "Values";
#echo $VALUES;
#echo "Keys";
#echo $KEYS;