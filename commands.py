commands = {
    'info':     '{"system":{"get_sysinfo":{}}}',
    'on':       '{"system":{"set_relay_state":{"state":1}}}',
    'off':      '{"system":{"set_relay_state":{"state":0}}}',
    'cloud':    '{"cnCloud":{"get_info":{}}}',
    'scan':     '{"netif":{"get_scaninfo":{"refresh":0}}}',
    'time':     '{"time":{"get_time":{}}}',
    'schedule': '{"schedule":{"get_rules":{}}}',
    'timer':    '{"count_down":{"get_rules":{}}}',
    'away': '    {"anti_theft":{"get_rules":{}}}',
    'reboot':   '{"system":{"reboot":{"delay":1}}}',
    'reset':    '{"system":{"reset":{"delay":1}}}'
}

# delay of 1 seems to be the fastest, as 0 does not seem to run :P
