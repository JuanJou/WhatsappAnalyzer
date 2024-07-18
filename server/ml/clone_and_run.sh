#/bin/sh

eval $(ssh-agent)

chmod 600 /root/.ssh/id_ed25519

ssh-add /root/.ssh/id_ed25519

git clone git@github.com:JuanJouglard/whatsapp-ml-service.git

cd whatsapp-ml-service

npm i

npm run dev
