"""These are known commands that require no input, and thus can be reused
The most popular ones are probably going to be `on` and `off`.
"""
commands = {
    'info':         '{"system":{"get_sysinfo":{}}}',
    'on':           '{"system":{"set_relay_state":{"state":1}}}',
    'off':          '{"system":{"set_relay_state":{"state":0}}}',
    'night':        '{"system":{"set_led_off":{"off":1}}}',
    'day':          '{"system":{"set_led_off":{"off":0}}}',
    'reboot':       '{"system":{"reboot":{"delay":1}}}',
    'reset':        '{"system":{"reset":{"delay":1}}}',
    'cloud-info':   '{"cnCloud":{"get_info":null}}',
    'scan':         '{"netif":{"get_scaninfo":{"refresh":1}}}',
    'time':         '{"time":{"get_time":{}}}',
    'timezone':     '{"time":{"get_timezone":null}}',
    'schedule':     '{"schedule":{"get_rules":{}}}',
    'timer':        '{"count_down":{"get_rules":{}}}',
    'away': '        {"anti_theft":{"get_rules":{}}}'
}

# delay of 1 seems to be the fastest, as 0 does not seem to run :P
