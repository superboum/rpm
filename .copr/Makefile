scm_root = $(dir $(realpath $(firstword $(MAKEFILE_LIST))))../
spec_root = $(dir $(realpath $(scm_root)$(spec)))
rpmbuild_src = $(shell rpmbuild --eval '%{_sourcedir}')

prepare:
	dnf -y install rpmdevtools rpm-build gcc make ncurses-devel libX11-devel
	cp $(spec_root)/*.patch $(rpmbuild_src)
	spectool -g -R ${scm_root}chez-scheme/chez-scheme.spec

srpm: prepare
	rpmbuild -bs --define "_rpmdir $(outdir)" $(scm_root)$(spec)

rpm: prepare
	rpmbuild -bb --define "_rpmdir $(outdir)" $(scm_root)$(spec)
