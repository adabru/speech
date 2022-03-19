app: alacritty
-
list: "ls\n"
paste: key(ctrl-shift-v)
cancel: key(ctrl-c)
quit: key(q)
less: "less "
change: "cd "
change home: "cd ~\n"
change downloads: "cd ~/downloads\n"
change speech: "cd ~/repo/speech\n"
change temp: "cd /tmp\n"
pe grep: "pgrep "
flag <user.letter>+$:
  "-"
  user.insert_many(letter_list)


logscroll: "journalctl --user -u speech.talon -e\n"
log: "journalctl --user -u speech.talon -ef\n"
status: "systemctl --user status speech.talon.service\n"
restart: "systemctl --user restart speech.talon.service"

logscroll launcher: "journalctl --user -u speech.launcher -e\n"
log launcher: "journalctl --user -u speech.launcher -ef\n"
status launcher: "systemctl --user status speech.launcher.service\n"
stop launcher: "systemctl --user stop speech.launcher.service\n"
restart launcher: "systemctl --user restart speech.launcher.service\n"

git status: "git status\n"
git diff: "git diff --ws-error-highlight=all\n"
git all: "git add -A\n"
git commit:
  "git commit -m \"\""
  key(left)
git amend: "git commit --amend --no-edit"
