from screen import Screen, Message, Card, get_current_screen_size
from time import sleep


def main():
    try:
        rows, cols = get_current_screen_size()
    except:
        # We are probably running the code in IDLE, check this
        s = Screen(0, 0)
        if s.is_running_in_IDLE():
            print("You appear to be running this code in IDLE.")
            print("Please refer to the instructions in the PDF for how to run the file")
            input('Press ENTER to exit')

    # checks that the file is being run in fullscreen
    while rows < 50 or cols < 200:
        s = Screen(rows, cols)
        disp_string = "You don't appear to be running this file in fullscreen."
        disp_string += f"\nCurrent screen size: rows = {rows}, columns = {cols}"
        disp_string += "\nThe reccomended minimum screen size is 50 rows and 200 columns."
        disp_string += "\nPlease adjust the screen size to continue"
        message = Message(disp_string, s)
        message.display_centre()  # displays the message to the user
        s.display()
        sleep(2)
        rows, cols = get_current_screen_size()
    else:
        s.clear()


if __name__ == "__main__":
    main()
    input("...")
