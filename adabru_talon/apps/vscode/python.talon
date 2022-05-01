#custom vscode commands go here
app: vscode
mode: user.python
mode: user.auto_lang
and code.language: python
-

zero: "0"
one: "1"
two: "2"
three: "3"
four: "4"
five: "5"
six: "6"
seven: "7"
eight: "8"
nine: "9"
point: "."
com: ","
col: ":"
dash: "-"
minus: "-"
downscore: "_"
plus: "+"
box: "["
round: "("
right round: ")"
brace: "{"
right brace: "}"
greater: ">"
less: "<"
dote: "\""
quote: "'"
assign: "="
equals: "=="
not equals: "!="
or: " or "
also: " and "

none: "None"
false: "False"
true: "True"
self: "self"
return: "return "
import: "import "
else: "else:\n"
print:
    "print()"
    key(left)
enumerate:
    "enumerate()"
    key(left)
len:
    "len()"
    key(left)

loop: user.snippet_insert("f")
while: user.snippet_insert("w")
if: user.snippet_insert("if")
function: user.snippet_insert("func")
class: user.snippet_insert("c")
constructor: user.snippet_insert("init")
