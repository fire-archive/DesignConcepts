version=$(cat ../version)
hash=$(git rev-parse develop)
echo Revision: $version $hash "\n" > version.txt

