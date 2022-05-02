# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.


INCLUDES = """
/* define our OpenSSL API compatibility level to 1.0.1. Any symbols older than
   that will raise an error during compilation. We can raise this number again
   after we drop 1.0.2 support in the distant future.  */
#define OPENSSL_API_COMPAT 0x10001000L

#include <openssl/opensslv.h>


#if defined(LIBRESSL_VERSION_NUMBER)
#define CRYPTOGRAPHY_IS_LIBRESSL 1
#else
#define CRYPTOGRAPHY_IS_LIBRESSL 0
#endif

#if defined(OPENSSL_IS_BORINGSSL)
#define CRYPTOGRAPHY_IS_BORINGSSL 1
#else
#define CRYPTOGRAPHY_IS_BORINGSSL 0
#endif

/*
    LibreSSL removed e_os2.h from the public headers so we'll only include it
    if we're using vanilla OpenSSL.
*/
#if !CRYPTOGRAPHY_IS_LIBRESSL
#include <openssl/e_os2.h>
#endif
#if defined(_WIN32)
#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <Wincrypt.h>
#include <Winsock2.h>
#endif

#if CRYPTOGRAPHY_IS_LIBRESSL
#define CRYPTOGRAPHY_LIBRESSL_LESS_THAN_322 \
    (LIBRESSL_VERSION_NUMBER < 0x3020200f)
#define CRYPTOGRAPHY_LIBRESSL_LESS_THAN_332 \
    (LIBRESSL_VERSION_NUMBER < 0x3030200f)
#define CRYPTOGRAPHY_LIBRESSL_LESS_THAN_340 \
    (LIBRESSL_VERSION_NUMBER < 0x3040000f)
#define CRYPTOGRAPHY_LIBRESSL_LESS_THAN_350 \
    (LIBRESSL_VERSION_NUMBER < 0x3050000f)

#else
#define CRYPTOGRAPHY_LIBRESSL_LESS_THAN_322 (0)
#define CRYPTOGRAPHY_LIBRESSL_LESS_THAN_332 (0)
#define CRYPTOGRAPHY_LIBRESSL_LESS_THAN_340 (0)
#define CRYPTOGRAPHY_LIBRESSL_LESS_THAN_350 (0)
#endif

#if OPENSSL_VERSION_NUMBER < 0x10100000
    #error "pyca/cryptography MUST be linked with Openssl 1.1.0 or later"
#endif

#define CRYPTOGRAPHY_OPENSSL_111D_OR_GREATER \
    (OPENSSL_VERSION_NUMBER >= 0x10101040 && !CRYPTOGRAPHY_IS_LIBRESSL)
#define CRYPTOGRAPHY_OPENSSL_300_OR_GREATER \
    (OPENSSL_VERSION_NUMBER >= 0x30000000 && !CRYPTOGRAPHY_IS_LIBRESSL)

#define CRYPTOGRAPHY_OPENSSL_LESS_THAN_111 \
    (OPENSSL_VERSION_NUMBER < 0x10101000 || CRYPTOGRAPHY_IS_LIBRESSL)
#define CRYPTOGRAPHY_OPENSSL_LESS_THAN_111B \
    (OPENSSL_VERSION_NUMBER < 0x10101020 || CRYPTOGRAPHY_IS_LIBRESSL)
#define CRYPTOGRAPHY_OPENSSL_LESS_THAN_111D \
    (OPENSSL_VERSION_NUMBER < 0x10101040 || CRYPTOGRAPHY_IS_LIBRESSL)
#if (CRYPTOGRAPHY_OPENSSL_LESS_THAN_111D && !CRYPTOGRAPHY_IS_LIBRESSL && \
    !defined(OPENSSL_NO_ENGINE)) || defined(USE_OSRANDOM_RNG_FOR_TESTING)
#define CRYPTOGRAPHY_NEEDS_OSRANDOM_ENGINE 1
#else
#define CRYPTOGRAPHY_NEEDS_OSRANDOM_ENGINE 0
#endif
"""

TYPES = """
static const int CRYPTOGRAPHY_OPENSSL_111D_OR_GREATER;
static const int CRYPTOGRAPHY_OPENSSL_300_OR_GREATER;

static const int CRYPTOGRAPHY_OPENSSL_LESS_THAN_111;
static const int CRYPTOGRAPHY_OPENSSL_LESS_THAN_111B;
static const int CRYPTOGRAPHY_NEEDS_OSRANDOM_ENGINE;

static const int CRYPTOGRAPHY_LIBRESSL_LESS_THAN_340;
static const int CRYPTOGRAPHY_LIBRESSL_LESS_THAN_350;

static const int CRYPTOGRAPHY_IS_LIBRESSL;
static const int CRYPTOGRAPHY_IS_BORINGSSL;
"""

FUNCTIONS = """
"""

CUSTOMIZATIONS = """
"""
