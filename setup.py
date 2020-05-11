from setuptools import setup, find_packages, Extension

c_helper = Extension('klippy/chelper/c_helper',
                    define_macros = [('MAJOR_VERSION', '1'),
                                     ('MINOR_VERSION', '0')],
                    sources = [ 'klippy/chelper/itersolve.c',
                                'klippy/chelper/kin_cartesian.c',
                                'klippy/chelper/kin_corexy.c',
                                'klippy/chelper/kin_delta.c',
                                'klippy/chelper/kin_extruder.c',
                                'klippy/chelper/kin_polar.c',
                                'klippy/chelper/kin_rotary_delta.c',
                                'klippy/chelper/kin_winch.c',
                                'klippy/chelper/pyhelper.c',
                                'klippy/chelper/serialqueue.c',
                                'klippy/chelper/stepcompress.c',
                                'klippy/chelper/trapq.c' ])

setup(
    name = 'klipper',
    version = '0.8.0+git',
    description = 'Klipper 3D Printing Firmware',
    packages=find_packages(),
    include_package_data = True,
    entry_points = { "console_scripts": [ "klippy = klippy.klippy:main" ] },
    url = "https://www.klipper3d.org/",
    ext_modules = [ c_helper ]
)
