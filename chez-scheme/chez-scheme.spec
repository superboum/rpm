%global debug_package %{nil}
%define is_mageia %(test -e /etc/mageia-release && echo 1 || echo 0)

Name:           chez-scheme
Summary:        Chez Scheme is an efficient and reliable implementation of Scheme based on an incremental optimizing compiler that produces efficient code and does so quickly. 
Version:        9.5.2
Release:        2%{?dist}
URL:            http://cisco.github.io/ChezScheme
License:        Apache-2.0
Source0:        https://github.com/cisco/ChezScheme/archive/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  curl
BuildRequires:  ca-certificates
BuildRequires:  libuuid-devel

%if %is_mageia
BuildRequires: lib64x11-devel
%else
BuildRequires:  libX11-devel
%endif

Requires: libuuid

Patch0: install-permissions-strip.patch

%description
Chez Scheme is both a programming language and an implementation of that language, with supporting tools and documentation.

As a superset of the language described in the Revised6 Report on the Algorithmic Language Scheme (R6RS), Chez Scheme supports all standard features of Scheme, including first-class procedures, proper treatment of tail calls, continuations, user-defined records, libraries, exceptions, and hygienic macro expansion.

Chez Scheme also includes extensive support for interfacing with C and other languages, support for multiple threads possibly running on multiple cores, non-blocking I/O, and many other features.

The Chez Scheme implementation consists of a compiler, run-time system, and programming environment. Although an interpreter is available, all code is compiled by default. Source code is compiled on-the-fly when loaded from a source file or entered via the shell. A source file can also be precompiled into a stored binary form and automatically recompiled when its dependencies change. Whether compiling on the fly or precompiling, the compiler produces optimized machine code, with some optimization across separately compiled library boundaries. The compiler can also be directed to perform whole-program compilation, which does full cross-library optimization and also reduces a program and the libraries upon which it depends to a single binary.

The run-time system interfaces with the operating system and supports, among other things, binary and textual (Unicode) I/O, automatic storage management (dynamic memory allocation and generational garbage collection), library management, and exception handling. By default, the compiler is included in the run-time system, allowing programs to be generated and compiled at run time, and storage for dynamically compiled code, just like any other dynamically allocated storage, is automatically reclaimed by the garbage collector.

The programming environment includes a source-level debugger, a mechanism for producing HTML displays of profile counts and program "hot spots" when profiling is enabled during compilation, tools for inspecting memory usage, and an interactive shell interface (the expression editor, or "expeditor" for short) that supports multi-line expression editing. 

%prep
%autosetup -n ChezScheme-%{version} -p 1

%build
./configure --installbin=%{_bindir} --installlib=%{_libdir} --installman=%{_mandir} --temproot=%{buildroot} --threads
make CFLAGS=-Wno-unknown-warning

%install
%make_install

%files
%{_bindir}/petite
%{_bindir}/scheme
%{_bindir}/scheme-script
%{_libdir}/csv%{version}/*
%{_mandir}/man1/*.1.*

%changelog
* Wed Jul 01 2020 Quentin Dufour <quentin@dufour.io> - 9.5.2-2
- Compile with thread support (appending --thread to ./configure), thanks Jens-Ulrik Peterson for the notification.

* Mon Jun 15 2020 Quentin Dufour <quentin@dufour.io> - 9.5.2-1
- Upgrade sources from 9.5 to 9.5.2. Changelog is avalaible here: https://github.com/cisco/ChezScheme/blob/v9.5.2/LOG
- Patch makefile to fix binary stripping on fedora rawhide that causes a fatal error

* Mon Jun 11 2018 Quentin Dufour <quentin@dufour.io> - 9.5-2
- Update symlink patch to use a hard link instead as recommended in https://github.com/cisco/ChezScheme/pull/307

* Sat May 19 2018 Quentin Dufour <quentin@dufour.io> - 9.5-1
- Initial packaging of Chez Scheme
