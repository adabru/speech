## kaldi

```
cd ./run/kaldi
./get_files.sh
sudo -E docker-compose up
```

Not working good enough yet, pushing to later.

## talon

```sh
#git clone https://github.com/knausj85/knausj_talon.git
#pacman -S ttf-dejavu
#mkdir -p ~/.talon/user
wget -o ~/.talon/user/dictionary/german.dic https://github.com/mqnc/talon_german/raw/master/dictionary/german.dic
cd ~/.talon/user
git clone https://github.com/cursorless-dev/cursorless-talon.git cursorless-talon

#pacman -S python-pyqt5 python-scipy python-sounddevice python-wheel swig
#t -S python-keyboard
# t -S python-pocketsphinx-git
#pip install pocketsphinx

ln -s ~/repo/speech/parrot_patterns.json ~/.talon/parrot/patterns.json

#sudo cp ~/repo/speech/service/speech.keys.service /etc/systemd/system/
#sudo cp ~/repo/speech/service/speech.speechwindow.service /etc/systemd/user/
#sudo cp ~/repo/speech/service/speech.sphinx.service /etc/systemd/user/
sudo cp ~/repo/speech/service/speech.talon.service /etc/systemd/user/
sudo cp ~/repo/speech/service/speech.launcher.service /etc/systemd/user/

#sudo systemctl enable --now speech.keys
#systemctl --user start speech.speechwindow
#systemctl --user enable --now speech.sphinx
systemctl --user enable --now speech.talon
systemctl --user enable --now speech.launcher

# https://github.com/talonvoice/talon/issues/330
# https://superuser.com/a/1270812/966225
pacman -S imwheel
imwheel -b 45
```
