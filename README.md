# CS6303-Project

Python 3 source files to hack the [TP-Link HS100][hs100]

## Requirements

The only requirement is `python3`. You can install it from [Python's website][python].

## How to Runs

    python3 main.py <ip address> <command>

That's it! So, if your HS100's IP was `192.168.1.123` and you wanted to turn power off; run:

    python3 main.py 192.168.1.123 off

And it should switch power off!

That's it. You can find the list of commands in `commands.py`.

## How it Works

This is a simple client that basically acts like the [Kasa app][kasa] TP-Link uses to control its devices. I decompiled the Kasa Android apk and after rooting around for port 9999 (the port the HS100 uses to send/receive commands), I found the encryption function. It turns out TP-Link uses a simple [Autokey Cipher][autokey] which was easy to decrypt.

This client just does that. Once you can encrypt/decrypt traffic I could figure out exactly what the Kasa app was sending (simple JSON structured commands), and then I too could do these things.

## Usage

Ideally you would use this power to incorporate your HS100 into your own IoT network, expanding beyond the capabilities of the Kasa app. However because I've broken the security (which let's be honest was lacking), this could be used for nefarious purposed. I'm pretty sure I accidentally turned off someone else's Smart Plug while trying to get this working on my school's network.

*PLEASE*: Don't use this as a tool for attacks. I made this more to expose the security issues, not to try to take them down. The HS100 is a neat device, and I just like to hack things :P

## Other Notes

This was made as a component of my course project for MST's FS2016 CS6303 - Pervasive Computing.

Contact me at jacob.t.fischer@gmail.com if you have any questions.

[hs100]: http://www.tp-link.com/us/products/details/HS100.html
[python]: https://www.python.org/downloads/
[kasa]: https://play.google.com/store/apps/details?id=com.tplink.kasa_android
