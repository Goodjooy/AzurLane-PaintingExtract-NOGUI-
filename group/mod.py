
import restore_hand.support
import restore_hand.scr_class
import restore_hand

scr = restore_hand.scr_class.Screen()

restore_hand.support.prepare()

scr.create_screen()

restore_hand.support.load_sub_pic()
restore_hand.support.load_bg()
restore_hand.support.print_pic()

while True:
    restore_hand.support.event_catch()
    restore_hand.support.show_prepare()
    scr.load_scr_bg()
    restore_hand.support.print_bg(scr)
    scr.load_bar()
    restore_hand.support.show(scr)
    restore_hand.support.press(scr)
    scr.update_scr()
    restore_hand.support.change_print()