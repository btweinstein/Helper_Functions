from cython_gsl cimport *

cpdef double get_wigner_3j(int ja, int jb, int jc, int ma, int mb, int mc) nogil:

    cdef int two_ja, two_jb, two_jc, two_ma, two_mb, two_mc

    two_ja, two_jb, two_jc = 2*ja, 2*jb, 2*jc
    two_ma, two_mb, two_mc = 2*ma, 2*mb, 2*mc

    return gsl_sf_coupling_3j(two_ja, two_jb, two_jc, two_ma, two_mb, two_mc)