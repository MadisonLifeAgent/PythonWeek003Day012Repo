#region - #import Alarm_clock class for use

from alarmclock import Alarm_clock
#endregion

#region - # set the current time and display it

# call the alarm clock and set the current time
set_time = Alarm_clock()
set_time.what_time_is_it()

#endregion

#region - #toggle the alarm on or off and display toggle status

# call the alarm clock and toggle the alarm on or off
toggle_alarm = Alarm_clock()
toggle_alarm.alarm_toggle_switch()

#endregion

#region - #set the alarm time and display it

set_alarm_time = Alarm_clock()
set_alarm_time.set_wake_up_time()
# print alarm toggle status

#endregion