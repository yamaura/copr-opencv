.PHONY: srpm

srpm:
	dnf install -y rpmdevtools
	rpmbuild -bs coin-or-Clp-rpm-macros-bootstrap.spec --define "_sourcedir $(PWD)" --define "_srcrpmdir $(outdir)"
