echo "path of local folder $1"
echo "username $2"
echo "reponame $3"

cd $1
echo "https://github.com/$2/$3.git"
git init
git remote add origin https://github.com/$2/$3.git
git pull  https://github.com/$2/$3.git

sleep 30s