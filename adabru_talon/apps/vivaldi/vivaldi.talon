app: vivaldi-stable
-
address: key(ctrl-l)
search: key(ctrl-k)
search <phrase>:
    key(ctrl-k)
    sleep(50ms)
    insert(phrase)
    key(enter)
copy address:
    key(ctrl-l)
    sleep(50ms)
    edit.copy()
go forward: key(alt-shift-right)
go back: key(alt-shift-left)
go to {user.website}:
    key(ctrl-l)
    sleep(50ms)
    insert(website)
    key(enter)
go cookie less: key(ctrl-shift-n)
(refresh | reload): key(ctrl-r)
(refresh | reload) hard: key(ctrl-shift-r)
dev tools [show]: key(f12)

tew: key(ctrl-t)
tabut: key(alt-left)
tabit: key(alt-right)
tose: key(ctrl-w )
tab (reopen|restore): key(ctrl-shift-t)
tab <number>: key("alt-{number}")
tab final: key(alt-9)
tab clone: key(ctrl-d)
tab mute:
    key(ctrl-m)
    key(ctrl-`)
