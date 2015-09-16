{
    "targets": [
        {
            "target_name": "rijndael",
            "defines": [
                'HAVE_CONFIG_H',
                'LIBDIR="lib/libmcrypt/modules/algorithms/:lib/libmcrypt/modules/modes/"'
            ],
            "cflags" : [
                "-Wno-unused-variable",
                "-Wno-unused-value",
                "-Wno-unused-but-set-variable",
                "-Wno-maybe-uninitialized",
                "-Wno-pointer-sign",
                "-Wno-sign-compare"
            ],
            "include_dirs": [
                ".",
                "lib/libmcrypt",
                "lib/libmcrypt/include",
                "lib/libmcrypt/lib",
                "lib/libmcrypt/modules/algorithms"
                "lib/libmcrypt/modules/lib",
                "<!(node -e \"require('nan')\")"
            ],
            "sources": [
                "src/rijndael.cc",
                "src/mcrypt_symb.cc",
                "lib/libmcrypt/modules/algorithms/3-way.c",
                "lib/libmcrypt/modules/algorithms/arcfour.c",
                "lib/libmcrypt/modules/algorithms/blowfish.c",
                "lib/libmcrypt/modules/algorithms/blowfish-compat.c",
                "lib/libmcrypt/modules/algorithms/cast-128.c",
                "lib/libmcrypt/modules/algorithms/cast-256.c",
                "lib/libmcrypt/modules/algorithms/des.c",
                "lib/libmcrypt/modules/algorithms/enigma.c",
                "lib/libmcrypt/modules/algorithms/gost.c",
                "lib/libmcrypt/modules/algorithms/loki97.c",
                "lib/libmcrypt/modules/algorithms/panama.c",
                "lib/libmcrypt/modules/algorithms/rc2.c",
                "lib/libmcrypt/modules/algorithms/rijndael-128.c",
                "lib/libmcrypt/modules/algorithms/rijndael-192.c",
                "lib/libmcrypt/modules/algorithms/rijndael-256.c",
                "lib/libmcrypt/modules/algorithms/safer64.c",
                "lib/libmcrypt/modules/algorithms/safer128.c",
                "lib/libmcrypt/modules/algorithms/saferplus.c",
                "lib/libmcrypt/modules/algorithms/serpent.c",
                "lib/libmcrypt/modules/algorithms/tripledes.c",
                "lib/libmcrypt/modules/algorithms/twofish.c",
                "lib/libmcrypt/modules/algorithms/wake.c",
                "lib/libmcrypt/modules/algorithms/xtea.c",
                "lib/libmcrypt/modules/modes/cbc.c",
                "lib/libmcrypt/modules/modes/cfb.c",
                "lib/libmcrypt/modules/modes/ctr.c",
                "lib/libmcrypt/modules/modes/ecb.c",
                "lib/libmcrypt/modules/modes/ncfb.c",
                "lib/libmcrypt/modules/modes/nofb.c",
                "lib/libmcrypt/modules/modes/ofb.c",
                "lib/libmcrypt/modules/modes/stream.c",
                "lib/libmcrypt/lib/bzero.c",
                "lib/libmcrypt/lib/mcrypt.c",
                "lib/libmcrypt/lib/mcrypt_extra.c",
                "lib/libmcrypt/lib/mcrypt_modules.c",
                "lib/libmcrypt/lib/xmemory.c"
            ],
            'conditions': [
                ['OS=="win"', {
                        'defines': [
                            'WIN32'
                        ]
                    }, { # OS != "win",
                        'defines': [
                            'HAVE_STRINGS_H',
                            'HAVE_UNISTD_H',
                            'HAVE_ENDIAN_H',
                            'HAVE_BYTESWAP_H',
                            'HAVE_DIRENT_H',
                            'HAVE_SYS_MMAN_H',
                            'HAVE_MLOCK'
                        ]
                    }
                ]
            ]
        }
    ]
}
