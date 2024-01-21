FROM fedora:39

RUN dnf groupinstall -y "Development Tools" "Development Libraries"
RUN dnf -y install rpmdevtools rpm-build
RUN dnf -y install libX11-devel libuuid-devel
COPY . /home/rpm
RUN chown -R 1000 /home
USER 1000
WORKDIR /home/rpm/chez-scheme
ENV HOME=/home
RUN make -f ../.copr/Makefile rpm spec=chez-scheme.spec outdir=../out
