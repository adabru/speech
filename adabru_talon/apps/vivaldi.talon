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
[go] forward: key(alt-shift-left)
go (back | backward): key(alt-shift-right)
go to {user.website}:
    key(ctrl-l)
    sleep(50ms)
    insert(website)
    key(enter)
go private: key(ctrl-shift-n)
(refresh | reload) it: key(ctrl-r)
(refresh | reload) it hard: key(ctrl-shift-rc)
dev tools [show]: key(f12)

tab (open | new): key(ctrl-t)
tab left: key(alt-left)
tab right: key(alt-right)
tab close: key(ctrl-w )
tab (reopen|restore): key(ctrl-shift-t)
go tab <number>: key(alt-number)
go tab final: key(alt-9)
tab duplicate: key(ctrl-d)
