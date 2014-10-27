import os
import pytz
import config
import fitbit
import datetime

# authenticated client
authd_client = fitbit.Fitbit(config.C_KEY, config.C_SECRET, system="en-GB",
                     resource_owner_key=config.resource_owner_key,
                     resource_owner_secret=config.resource_owner_secret)

device = authd_client.get_devices()[0]
device_id = device['id']

# first, delete the previous alarm id that was saved to a file
with open('alarms', 'r') as f:
    alarm_id_str = f.read()

# now delete the previous alarm using API
if alarm_id_str:
    alarm_id = int(alarm_id_str)
    try:
        authd_client.delete_alarm(device_id, alarm_id)
    except Exception as e:
        print "couldn't delete the alarm", e

# set a new alarm in 25 minutes
time_now = datetime.datetime.now(pytz.utc)
time_next = time_now + datetime.timedelta(minutes=25)

try:
    alarm = authd_client.add_alarm(device_id=device_id, alarm_time=time_next, week_days=[], recurring=False, enabled=True)
except Exception as e:
    print "couldn't add the alarm", e

# save the id of just created alarm
alarm_id = alarm['trackerAlarm']['alarmId']

# save this to the file, by replacing the previous
with open("alarms", 'w') as f:
    if alarm_id:
        f.write(str(alarm_id))

