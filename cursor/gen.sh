#!/usr/bin/sh

for i in *.cursor; do xcursorgen $i "./AdabruCursors/cursors/${i%.*}"; done

# ls /usr/share/icons/Adwaita/cursors/
cd ./AdabruCursors/cursors
ln -s default arrow
ln -s default pointer
ln -s default right_ptr
ln -s default left_ptr
ln -s default crosshair
ln -s default cross
ln -s default draft_large
ln -s default draft_small
ln -s default plus
ln -s default top_left_arrow
ln -s default tcross
ln -s default hand
ln -s default hand1
ln -s default hand2
ln -s default left_tee
ln -s default left_side
ln -s default left_ptr_watch