#! /bin/bash
# -*- coding: utf-8 -*-
#
# pyxbgen
# Agenzia delle Entrate pyxb generator
#
# This free software is released under GNU Affero GPL3
# author: Antonio M. Vigliotti - antoniomaria.vigliotti@gmail.com
# (C) 2017-2017 by SHS-AV s.r.l. - http://www.shs-av.com - info@shs-av.com
#
THIS=$(basename $0)
TDIR=$(readlink -f $(dirname $0))
for x in $TDIR $TDIR/.. $TDIR/../z0lib $TDIR/../../z0lib . .. /etc; do
  if [ -e $x/z0librc ]; then
    . $x/z0librc
    Z0LIBDIR=$x
    Z0LIBDIR=$(readlink -e $Z0LIBDIR)
    break
  fi
done
if [ -z "$Z0LIBDIR" ]; then
  echo "Library file z0librc not found!"
  exit 2
fi

__version__=0.1.3.1


OPTOPTS=(h        k        n           p          q            u       V           v           x)
OPTDEST=(opt_help opt_keep opt_dry_run opt_nopep8 opt_verbose  opt_uri opt_version opt_verbose opt_exclude)
OPTACTI=(1        1        1           1          0            "1>"    "*"         1           "=>")
OPTDEFL=(1        0        0           0          -1            0       ""         -1           "DatiFatturaMessaggi")
OPTMETA=("help"   ""       ""          ""         "silent"     ""      "version"   "verbose"   "module")
OPTHELP=("this help"\
 "keep temporary files"\
 "do nothing (dry-run)"\
 "do not apply pep8"\
 "silent mode"\
 "execute uri Agenzia delle Entrate"\
 "show version"\
 "verbose mode"\
 "commma separated module exclusion list; i.e. fornituraIvp,FatturaPA,DatiFattura,DatiFatturaMessaggi")
OPTARGS=()

DISTO=$(xuname "-d")
if [ "$DISTO" == "CentOS" ]; then
  parseoptargs "$@"
else
  echo "Waring! This tool run just under CentOS, version 6 o 7"
  opt_version=0
  opt_help=1
fi
if [ "$opt_version" ]; then
  echo "$__version__"
  exit 0
fi
if [ $opt_help -gt 0 ]; then
  print_help "Agenzia delle Entrate pyxb generator"\
  "(C) 2017 by zeroincombenze(R)\nhttp://wiki.zeroincombenze.org/en/Linux/dev\nAuthor: antoniomaria.vigliotti@gmail.com"
  exit 0
fi
bin_path=${PATH//:/ }
for x in $TDIR $TDIR/.. $bin_path; do
  if [ -e $x/pyxbgen ]; then
    # [ $opt_verbose -ne 0 ] && echo "PYXBGEN=$x/pyxbgen"
    PYXBGEN=$x/pyxbgen
    break
  fi
done
cmd=
mdl=
BINDINGS=$TDIR/bindings
SCHEMAS=../data
rm -fR $BINDINGS
mkdir -p $BINDINGS
pushd $BINDINGS ?>/dev/null
[ $opt_verbose -ne 0 ] && echo "\$ cd $PWD"
exclude="(${opt_exclude//,/|})"
for d in $SCHEMAS/*; do
  if [ -d $d ]; then
    p=$d
    for x in main liquidazione; do 
      if [ -d $d/$x ]; then
        p=$d/$x
        break
      fi
    done
    [ $opt_verbose -ne 0 ] && echo ".. reading directory $p"
    for f in $p/*.xsd; do
      fn=$(basename $f)
      m=
      if [ "$fn" == "fornituraIvp_2017_v1.xsd" ]; then
        m=vat_settlement_v_1_0
      elif [ "$fn" == "FatturaPA_versione_1.2.xsd" ]; then
        m=fatturapa_v_1_2
      elif [ "$fn" == "DatiFatturav2.0.xsd" ]; then
        m=dati_fattura_2_0
      elif [ "$fn" == "DatiFatturaMessaggiv2.0.xsd" ]; then
        m=messaggi_fattura_2_0
      fi
      if [ -n "$m" ] && [[ $fn =~ $exclude ]]; then
        m=
        continue
      fi
      if [ -n "$m" ]; then
        mdl="$mdl $m"
        cmd="-u $f -m $m $cmd"
      fi
    done
  fi
done
# cmd="$cmd --module-prefix=$BINDINGS --archive-to-file=$BINDINGS/ade.wxs"
cmd="$PYXBGEN $cmd --archive-to-file=./ade.wxs"
[ $opt_verbose -ne 0 ] && echo "\$ $cmd"
[ $opt_dry_run -ne 0 ] || eval "$cmd"
i=./__init__.py
if [ $opt_dry_run -eq 0 ]; then
  echo "# -*- coding: utf-8 -*-" >$i
  echo "# Copyright 2017 - Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>">>$i
  echo "#                  Associazione Odoo Italia <http://www.odoo-italia.org>">>$i
  echo "# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).">>$i
  echo "#">>$i
  echo "# Generated $(date '+%a %Y-%m-%d %H:%M:%S')">>$i
  echo "#">>$i
  for m in $mdl; do
    echo "from . import $m">>$i
  done
fi
for f in _cm _ds $mdl; do
  fn=$f.py
  [ $opt_verbose -ne 0 ] && echo "\$ $TDIR/pyxbgen.py $fn $SCHEMAS"
  [ $opt_dry_run -ne 0 ] || eval $TDIR/pyxbgen.py $fn $SCHEMAS
  if [ $opt_nopep8 -eq 0 ]; then
    [ $opt_verbose -ne 0 ] && echo "\$ autopep8 $fn -i"
    [ $opt_dry_run -ne 0 ] || autopep8 $fn -i
  fi
done
popd ?>/dev/null
if [ $opt_keep -eq 0 ]; then
  find . -name "*.bak" -delete
  find . -name "*.pyc" -delete
fi
