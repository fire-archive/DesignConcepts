version=$(cat ../version)
hash=$(git rev-parse develop)
echo -e Revision: $version Closest Commit: $hash "\n" > version.txt

