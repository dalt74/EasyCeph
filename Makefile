install:
	cp scripts/* /usr/local/bin
	cp systemd/* /usr/lib/systemd/system

post_install:
	systemctl daemon-reload
