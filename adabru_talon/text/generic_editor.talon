find:
    edit.find()

next one:
    edit.find_next()

go left:
    edit.left()

go right:
    edit.right()

go up:
    edit.up()

go down:
    edit.down()

go bottom:
    edit.file_end()

go top:
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
clear left:
    key(backspace)

clear right:
    key(delete)

clear up:
    edit.extend_line_up()
    edit.delete()

clear down:
    edit.extend_line_down()
    edit.delete()

clear all:
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
line clear: edit.delete_line()
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
word clear left:
    edit.extend_word_left()
    edit.delete()
word clear right:
    edit.extend_word_right()
    edit.delete()
word clear:
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

