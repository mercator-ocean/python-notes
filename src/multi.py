from netCDF4 import Dataset, num2date
from multiprocessing import Pool
from glob import glob
import xarray as xr
import timeit
import os

dataDir = '/dataref/opr/DATA/SST/OSTIA/2017101[0-2]*.nc'
ls = glob(dataDir)

if __name__ == '__main__':

    def getmean(args):

        mode, ind, filename = args[:]

        nc = Dataset(filename, 'r')

        time = num2date(nc.variables['time'][:], nc.variables['time'].units)

        print("[{mode}] run: {file} ({time:%Y-%m-%dT%H:%M})".format(mode=mode,
                                                                    file=os.path.basename(filename),
                                                                    time=time[0]))

        myvars = [var for var in nc.variables if nc.variables[var].dimensions == (u'time', u'lat', u'lon')]

        for var in myvars:
            V = xr.DataArray(nc.variables[var][:])
            mn = V.mean().data
            print("MODE [{mode}] : file {file} / var {var} : mean = {mn} ".format(mode=mode,
                                                                                  file=os.path.basename(filename),
                                                                                  var=var, mn=mn))

        nc.close()

    p = Pool(processes=4)

    # Sequential run
    start_time = timeit.default_timer()
    myArgs = [('Sequential', i, f) for i, f in enumerate(ls)]
    for arg in myArgs:
        getmean(arg)

    interm_time = timeit.default_timer()
    print "ELAPSED TIME [Sequential]:", interm_time - start_time

    # Asynchronous run
    myArgs = [('Asynchronous', i, f) for i, f in enumerate(ls)]
    p.map_async(getmean, myArgs)
    p.close()
    p.join()

    end_time = timeit.default_timer()
    print "ELAPSED TIME [Asynchronous]:", end_time - interm_time