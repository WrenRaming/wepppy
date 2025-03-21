from glob import glob
from os.path import split as _split
import os

from wepppy.wepp.soils.utils import WeppSoilUtil

if __name__ == "__main__":
    fns = glob('../Forest2006/*.sol')
    for fn in fns:
        fn = os.path.abspath(fn)
        print(fn)
        head, tail = _split(fn)

        soil = WeppSoilUtil(fn)
        new = soil.to7778()
        new.write(f'../Forest/{tail}')
