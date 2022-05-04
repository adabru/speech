app: alacritty
not title: Todo
-
point slash: "./\t\t"
list: "ls\n"
list verbose: "ls -ahl\n"
move: "mv "
link: "ln -s "
make dear: "mkdir "
div: "diff "
touch: "touch "
remove: "rm "
remove recurse: "rm -r "
paste: key(ctrl-shift-v)
cancel: key(ctrl-c)
clear: key(ctrl-l)
search$: key(ctrl-r)
search <phrase>:
  key(ctrl-r)
  "{phrase}"
quit: key(q)
less: "less "
pipe less: " | less\n"
pipe grep$: " | grep "
pipe grep <phrase>: " | grep {phrase}\n"
change: "cd "
change home: "cd ~\n"
change downloads: "cd ~/downloads\n"
change setup: "cd ~/setup\n"
change speech: "cd ~/repo/speech\n"
change eyeput: "cd ~/repo/eyeput\n"
change temp: "cd /tmp\n"
change talon: "cd ~/.talon/user\n"
change mount: "cd /mnt\n"
change up: "cd ..\n"
pe grep: "pgrep "
top: "top\n"
cat: "cat "
allow exec: "chmod +x "
copy: "copy "
man <phrase>: "man {phrase}\n"

disk usage: "df -h\n"
services reload: "systemctl --user daemon-reload\n"
generate password: "openssl rand -base64 16\n"

# talon
logscroll$: "journalctl --user -u speech.talon -e\n"
log$: "journalctl --user -u speech.talon -ef\n"
status$: "systemctl --user status speech.talon.service\n"
restart$: "systemctl --user restart speech.talon.service"
# launcher
logscroll launcher$: "journalctl --user -u speech.launcher -e\n"
log launcher$: "journalctl --user -u speech.launcher -ef\n"
status launcher$: "systemctl --user status speech.launcher.service\n"
stop launcher$: "systemctl --user stop speech.launcher.service\n"
restart launcher$: "systemctl --user restart speech.launcher.service\n"
# keys
logscroll keys$: "sudo journalctl -u eyeput.keys -e\n"
log keys$: "sudo journalctl -u eyeput.keys -ef\n"
status keys$: "sudo systemctl status eyeput.keys.service\n"
stop keys$: "sudo systemctl stop eyeput.keys.service\n"
restart keys$: "sudo systemctl restart eyeput.keys.service\n"


git status: "git status\n"
git diff: "git diff --ws-error-highlight=all\n"
git all: "git add -A\n"
git commit:
  "git commit -m \"\""
  key(left)
git amend: "git commit --amend --no-edit"
git set origin: "git remote set-url origin "
git add origin: "git remote add origin "
git push: "git push\n"
git clone: "git clone "

pacman search: "pacman -Ss "
pacman install: "pacman -S "
update: "update\n"

pip list: "pip list\n"
pip install$: "pip install "
pip install <phrase>: "pip install {phrase}\n"
pip uninstall$: "pip uninstall "
pip uninstall <phrase>: "pip uninstall {phrase}\n"
pip update$: "pip install -U "
pip update <phrase>: "pip install -U {phrase}\n"

in wheel: "imwheel -b 45\n"

# tmux
tew: key(alt-v)
tose: key(alt-y)
teft: key(alt-s)
tight: key(alt-f)

wifi list: "nmcli device wifi\n"
wifi connect: "nmcli device wifi connect -a "
wifi connection: "nmcli connection show\n"

unmount: "sudo umount /mnt\n"
mount squash: "sudo mount -o loop /mnt"

sink: "sync.py\n"
