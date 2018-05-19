rpmbuild_src = $(shell rpmbuild --eval '%{_sourcedir}')

prepare:
	dnf -y install rpmdevtools rpm-build gcc make ncurses-devel libX11-devel
	cp *.patch $(rpmbuild_src)
	spectool -g -R $(spec)

srpm: prepare
	rpmbuild -bs --define "_rpmdir $(outdir)" $(spec)

rpm: prepare
	rpmbuild -bb --define "_rpmdir $(outdir)" $(spec)
