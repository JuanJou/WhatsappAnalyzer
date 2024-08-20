echo "Starting setup..."
eval $(ssh-agent)

chmod 600 /root/.ssh/id_ed25519

ssh-add /root/.ssh/id_ed25519

echo "Cloning repo..."
git clone git@github.com:JuanJouglard/whatsapp-analyzer-backend.git

cd whatsapp-analyzer-backend

echo "Installing dependencies..."
pip install -r requirements.txt

uvicorn main:app --host 0.0.0.0 --port 8000 --reload
