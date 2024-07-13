#/bin/sh

eval $(ssh-agent)

chmod 600 /root/.ssh/id_ed25519

ssh-add /root/.ssh/id_ed25519

git clone git@github.com:JuanJouglard/whatsapp-analyzer-frontend.git

cd whatsapp-analyzer-frontend

npm i

npm run dev
