export WORKON_HOME=~/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

cd /home/abemillan/Developer/PRAHVI/PRAHVI-Backend

workon prahvi_backend

gunicorn --workers 3 prahvi.app:create_app\(\)
