import wigner_3j.wigner_3j as w
import numpy as np

tolerance = 10.**-10.

result_1 = w.get_wigner_3j(2,6,4,0,0,0)
print result_1

# Make sure the result is expected
assert np.abs(result_1 - np.sqrt(715.)/143. ) < tolerance

result_2 = w.get_wigner_3j(2,6,4,0,0,1)
print result_2

assert np.abs(result_2 - 0 ) < tolerance

print 'Tests passed!'
