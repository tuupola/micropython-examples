.DEFAULT_GOAL := help

help:
	@echo ""
	@echo "Available tasks:"
	@echo "    watch  Upload changed *.py files to /flash automatically"
	@echo "    shell  Start an remote shell session"
	@echo "    sync   Copy all *.py files to /flash"
	@echo "    reset  Soft reboot the board"
	@echo "    repl   Start a repl session"
	@echo "    deps   Install dependencies with upip"
	@echo ""

watch:
	find . -name "*.py" | entr -c sh -c 'make sync && make reset'

sync:
	#rshell --port /dev/tty.usbmodem* --timing --buffer-size=32 cp --recursive *.py /pyboard
	rshell --port /dev/tty.usbmodem* --timing --buffer-size=32 rsync --mirror --verbose ./firmware /flash

shell:
	rshell --port /dev/tty.usbmodem* --timing --buffer-size=32

repl:
	screen /dev/tty.usbmodem* 115200

reset:
	rshell --port /dev/tty.usbmodem* --timing --buffer-size=32 repl "~ import machine ~ machine.reset()~"

deps:
	micropython -m upip install -p firmware/lib/ micropython-gnssl76l
	curl https://raw.githubusercontent.com/inmcm/micropyGPS/master/micropyGPS.py -o firmware/lib/micropyGPS.py

.PHONY: help watch shell repl reset sync deps
