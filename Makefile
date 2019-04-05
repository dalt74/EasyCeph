install:
	cp bin/* /usr/local/bin
	cp ximera/bin/* /usr/local/bin
	cp ximera/systemd/* /usr/lib/systemd/system

post_install:
	systemctl daemon-reload
