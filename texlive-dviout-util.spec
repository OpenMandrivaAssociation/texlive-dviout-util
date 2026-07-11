%global tl_name dviout-util
%global tl_revision 66186

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	TeX Live package dviout-util
Group:		Publishing
URL:		https://www.ctan.org/pkg/dviout-util
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dviout-util.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dviout-util.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(dviout-util.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
TeX Live package dviout-util.

