import subprocess, time, datetime, calendar, shlex

# monitor_cmd = 'xprop -id $(xprop -root -f _NET_ACTIVE_WINDOW 0x " \$0\\n" _NET_ACTIVE_WINDOW | awk "{print \$2}") | grep "_NET_WM_NAME(UTF8_STRING)" | awk "{print \$3, \$4}"'
monitor_cmd = 'xprop -id $(xprop -root -f _NET_ACTIVE_WINDOW 0x " \$0\\n" _NET_ACTIVE_WINDOW | awk "{print \$2}") | grep "_NET_WM_NAME(UTF8_STRING)"'



def unix_timestamp():
    present_time = datetime.datetime.now()
    return calendar.timegm(present_time.utctimetuple())


while True:
    title_subprocess = subprocess.Popen(monitor_cmd, stdout=subprocess.PIPE, shell=True)
    title_sp_comm = title_subprocess.communicate()
    output = title_sp_comm[0]
    print output
    print unix_timestamp()
    print "------------"
    time.sleep(5)
