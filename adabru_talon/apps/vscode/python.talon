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
hash: "#"
downscore: "_"
plus: "+"
star: "*"
slash: "/"
modulo: "%"
percent: "%"
box: "["
right box: "]"
round: "("
right round: ")"
brace: "{"
right brace: "}"
greater: ">"
less: "<"
dote: "\""
quote: "'"
sign: "="
equals: "=="
not equals: "!="
not: "not "
other: " or "
also: " and "

none: "None"
false: "False"
true: "True"
self: "self"
int: "int"
float: "float"
return: "return "
import: "import "
assert: "assert "
global: "global "
otherwise: "else:\n"
try: "try:\n"
except: "except Exception as e:\n"
print:
    "print()"
    key(left)
range:
    "range()"
    key(left)
enumerate:
    "enumerate()"
    key(left)
len:
    "len()"
    key(left)
stringy:
    "str()"
    key(left)

loop: user.snippet_insert("f")
while: user.snippet_insert("w")
if: user.snippet_insert("if")
elif: user.snippet_insert("elif")
function: user.snippet_insert("func")
class: user.snippet_insert("c")
constructor: user.snippet_insert("init")
store: user.snippet_insert("store")

file play: user.vscode("python.execInTerminal")
