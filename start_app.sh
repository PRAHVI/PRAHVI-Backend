export WORKON_HOME=~/Envs
source /usr/local/bin/virtualenvwrapper.sh

cd /home/abe/Production/PRAHVI-Backend

workon prahvi_backend

gunicorn --workers 3 --bind unix:prahvi_backend.sock -m 007 prahvi.app:create_app\(\)
