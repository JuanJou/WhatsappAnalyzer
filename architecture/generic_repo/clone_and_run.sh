echo "Starting setup..."
eval $(ssh-agent)

chmod 600 /root/.ssh/id_ed25519

ssh-add /root/.ssh/id_ed25519

echo "Cloning repo..."
git clone $GITHUB_REPO $FOLDER

cd $FOLDER

echo "Installing dependencies..."
pip install -r requirements.txt

#python manage.py runserver 8004
tail -f /dev/null
