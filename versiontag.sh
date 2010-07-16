version=$(cat ../version)
hash=$(git rev-parse develop)
echo Revision: $version Closest Commit: $hash "\n" > version.txt

