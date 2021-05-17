echo "username is $1"
echo "useremail is $2"
echo "path is $3"

cd $3
git config user.name $1
git config user.email $2

sleep 100s
