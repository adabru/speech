find$:
    edit.find()

next one:
    edit.find_next()

left:
    edit.left()

right:
    edit.right()

up:
    edit.up()

down:
    edit.down()

bottom:
    edit.file_end()

top:
    edit.file_start()

# selecting
select all:
    edit.select_all()

select left:
    edit.extend_left()

select right:
    edit.extend_right()

select up:
    edit.extend_line_up()

select down:
    edit.extend_line_down()

# deleting
wipe up:
    edit.extend_line_up()
    edit.delete()

wipe down:
    edit.extend_line_down()
    edit.delete()

wipe all:
    edit.select_all()
    edit.delete()

#copy commands
copy all:
    edit.select_all()
    edit.copy()

#cut commands
cut all:
    edit.select_all()
    edit.cut()

# line commands
line select: edit.select_line()
line wipe: edit.delete_line()
line copy:
    edit.select_line()
    edit.copy()
line cut:
    edit.select_line()
    edit.cut()

# word commands
word cut:
    edit.select_word()
    edit.cut()
word left: edit.word_left()
word right: edit.word_right()
word select: edit.select_word()
word select left: edit.extend_word_left()
word select right: edit.extend_word_right()
word wipe left:
    edit.extend_word_left()
    edit.delete()
word wipe right:
    edit.extend_word_right()
    edit.delete()
word wipe:
    edit.delete_word()
word copy:
    edit.select_word()
    edit.copy()
word copy left:
    edit.extend_word_left()
    edit.copy()
word copy right:
    edit.extend_word_right()
    edit.copy()
word cut left:
    edit.extend_word_left()
    edit.cut()
word cut right:
    edit.extend_word_right()
    edit.cut()

