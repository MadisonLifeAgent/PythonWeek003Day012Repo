#region - alarm clock class

#alarm clock class
class Alarm_clock:
    # alarm clock properties
    def __init__(self):
        self.current_time = ""
        self.alarm_toggle = ""
        self.alarm_time = ""

    # set or change current time of alarm clock
    def what_time_is_it(self):
        # prompt user for current time
        self.current_time = input("What time is it?  ")

        # display the current time user entered
        print("The time is:  " + self.current_time)

    # toggle the alarm to on or off
    def alarm_toggle_switch(self):
        # prompt user to toggle the alarm
        self.alarm_toggle = input("Enter 1 to turn alarm ON, or 2 to turn alarm OFF.  ")

        print(self.alarm_toggle)

        # display whether alarm is on or off
        if (self.alarm_toggle == '1'):
            toggle_status = "Your alarm is turned ON"
            print(toggle_status)
        elif (self.alarm_toggle == '2'):
            toggle_status = "Your alarm is turned OFF"
            print(toggle_status)

        else:
            toggle_status = "Not a valid response. Try again."
            print(toggle_status)

        return toggle_status

    # set alarm time
    def set_wake_up_time(self):
        # prompt user to set alarm time
        self.alarm_time = input("Please set time for alarm:  ")

        print("Your alarm is set to:  " + self.alarm_time)

#endregion