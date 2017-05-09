cp dependencies/* $VIRTUAL_ENV/lib/
ln -s $VIRTUAL_ENV/lib/cv2.so $VIRTUAL_ENV/lib/python2.7/site-packages/cv2.so
echo 'export OLD_LD_LIBRARY_PATH="$LD_LIBRARY_PATH"' >> $VIRTUAL_ENV/bin/postactivate
echo 'export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$VIRTUAL_ENV/lib:$VIRTUAL_ENV/lib/python2.7/site-packages"' >> $VIRTUAL_ENV/bin/postactivate
echo 'export PATH="$VIRTUAL_ENV/lib:$PATH"' >> $VIRTUAL_ENV/bin/postactivate
echo 'export LD_LIBRARY_PATH=$OLD_LD_LIBRARY_PATH' >> $VIRTUAL_ENV/bin/postdeactivate
echo 'unset OLD_LD_LIBRARY_PATH' >> $VIRTUAL_ENV/bin/postdeactivate
