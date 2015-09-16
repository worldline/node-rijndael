#/bin/sh

declare -a EXTRA_ALGOS=("3-way" "arcfour" "blowfish" "blowfish-compat" "cast-128" "cast-256" "des" "enigma" "gost" "loki97" "panama" "rc2" "rijndael-128" "rijndael-192" "rijndael-256" "safer64" "safer128" "saferplus" "serpent" "tripledes" "twofish" "wake" "xtea" "cbc" "cfb" "ctr" "ecb" "ncfb" "nofb" "ofb" "stream")
echo "#include \"mcrypt_internal.h\"" > mcrypt_symb.c
echo "" >> mcrypt_symb.c
echo "/* This is automatically created. Don't touch... */" >> mcrypt_symb.c
echo "" >> mcrypt_symb.c
for i in "${EXTRA_ALGOS[@]}"; do \
  if test -f ../lib/libmcrypt/modules/algorithms/$i.c; then cat ../lib/libmcrypt/modules/algorithms/$i.c 2>/dev/null|grep define|grep LTX|awk '{printf "extern int "$3"();";}' >> mcrypt_symb.c 2>/dev/null; fi; \
  if test -f ../lib/libmcrypt/modules/modes/$i.c; then cat ../lib/libmcrypt/modules/modes/$i.c 2>/dev/null|grep define|grep LTX|awk '{printf "extern int "$3"();";}' >> mcrypt_symb.c 2>/dev/null; fi; \
done
echo "" >> mcrypt_symb.c
echo "const mcrypt_preloaded mps[] = {" >> mcrypt_symb.c
for i in "${EXTRA_ALGOS[@]}"; do \
  if test -f ../lib/libmcrypt/modules/modes/$i.c; then echo "  {\"$i\", NULL}, " >> mcrypt_symb.c 2>/dev/null; fi; \
  if test -f ../lib/libmcrypt/modules/algorithms/$i.c; then echo " {\"$i\", NULL}, " >> mcrypt_symb.c 2>/dev/null; fi; \
  if test -f ../lib/libmcrypt/modules/algorithms/$i.c; then cat ../lib/libmcrypt/modules/algorithms/$i.c 2>/dev/null|dos2unix|grep define|grep LTX|awk '{print "\t{\""$3"\", "$3"},";}' >> mcrypt_symb.c 2>/dev/null; fi; \
  if test -f ../lib/libmcrypt/modules/modes/$i.c; then cat ../lib/libmcrypt/modules/modes/$i.c 2>/dev/null|dos2unix|grep define|grep LTX|awk '{print "\t{\""$3"\", "$3"},";}' >> mcrypt_symb.c 2>/dev/null; fi; \
done
echo " {NULL, NULL}" >> mcrypt_symb.c
echo "};" >> mcrypt_symb.c