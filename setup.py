#!/usr/bin/env python
"""
Setup script for the `PyTrinamicMicro` package.
"""

import setuptools

setuptools.setup(
    name='PyTrinamicMicro',
    author='Maxim-Trinamic Software Team',
    author_email='pypi.trinamic@maximintegrated.com',
    description='PyTrinamicMicro package for TMCM-0960-MotionPy python master board.',
    long_description_content_type='text/markdown',
    url='https://github.com/trinamic/PyTrinamicMicro',
    packages=[
        "PyTrinamicMicro"
    ],
    include_package_data=True,
    scripts=[
        "PyTrinamicMicro/platforms/motionpy/examples/firmware_update/firmware_update_can.py",
        "PyTrinamicMicro/platforms/motionpy/examples/io/blinky.py",
        "PyTrinamicMicro/platforms/motionpy/examples/io/buttons_leds.py",
        "PyTrinamicMicro/platforms/motionpy/examples/linear_distance/linear_distance_bounds.py",
        "PyTrinamicMicro/platforms/motionpy/examples/linear_distance/linear_distance_velocity.py",
        "PyTrinamicMicro/platforms/motionpy/examples/modules/hc_sr04_multi/hc_sr04_multi_log.py",
        "PyTrinamicMicro/platforms/motionpy/examples/modules/max/max14001pmb.py",
        "PyTrinamicMicro/platforms/motionpy/examples/TMCM1161/TMCM1161_RS232_rotate.py",
        "PyTrinamicMicro/platforms/motionpy/examples/TMCM1161/TMCM1161_RS485_rotate.py",
        "PyTrinamicMicro/platforms/motionpy/examples/TMCM1240/TMCM1240_CAN_rotate.py",
        "PyTrinamicMicro/platforms/motionpy/examples/TMCM1240/TMCM1240_RS485_rotate.py",
        "PyTrinamicMicro/platforms/motionpy/examples/TMCM1270/TMCM1270_rotate.py",
        "PyTrinamicMicro/platforms/motionpy/examples/tmcl_analyzer/can_logger.py",
        "PyTrinamicMicro/platforms/motionpy/examples/tmcl_bridge/tmcl_bridge_uart_can.py",
        "PyTrinamicMicro/platforms/motionpy/examples/tmcl_bridge/tmcl_bridge_uart_rs232.py",
        "PyTrinamicMicro/platforms/motionpy/examples/tmcl_bridge/tmcl_bridge_uart_rs485.py",
        "PyTrinamicMicro/platforms/motionpy/examples/tmcl_bridge/tmcl_bridge_uart_x.py",
        "PyTrinamicMicro/platforms/motionpy/examples/tmcl_bridge/tmcl_bridge_usb_can.py",
        "PyTrinamicMicro/platforms/motionpy/examples/tmcl_bridge/tmcl_bridge_usb_rs232.py",
        "PyTrinamicMicro/platforms/motionpy/examples/tmcl_bridge/tmcl_bridge_usb_rs485.py",
        "PyTrinamicMicro/platforms/motionpy/examples/tmcl_bridge/tmcl_bridge_usb_uart.py",
        "PyTrinamicMicro/platforms/motionpy/examples/tmcl_bridge/tmcl_bridge_usb_x.py",
        "PyTrinamicMicro/platforms/motionpy/examples/tmcl_slave/tmcl_slave_motionpy_uart.py",
        "PyTrinamicMicro/platforms/motionpy/examples/tmcl_slave/tmcl_slave_motionpy.py",
        "PyTrinamicMicro/platforms/motionpy/examples/tmcl_slave/tmcl_slave_uart.py",
        "PyTrinamicMicro/platforms/motionpy/examples/tmcl_slave/tmcl_slave_usb.py",
        "PyTrinamicMicro/platforms/motionpy/tests/interfaces/can_version.py",
        "PyTrinamicMicro/platforms/motionpy/tests/interfaces/rs232_version.py",
        "PyTrinamicMicro/platforms/motionpy/tests/interfaces/rs485_version.py",
        "PyTrinamicMicro/platforms/motionpy/tests/interfaces/version.py",
        "PyTrinamicMicro/platforms/motionpy/tests/modules/TMCM1161/parameters_rs232.py",
        "PyTrinamicMicro/platforms/motionpy/tests/modules/TMCM1161/parameters_rs485.py",
        "PyTrinamicMicro/platforms/motionpy/tests/modules/TMCM1240/parameters_can.py",
        "PyTrinamicMicro/platforms/motionpy/tests/modules/TMCM1240/parameters_rs485.py",
        "PyTrinamicMicro/platforms/motionpy/tests/modules/TMCM1270/parameters.py",
        "PyTrinamicMicro/platforms/motionpy/tests/modules/TMCM1640/parameters.py",
        "PyTrinamicMicro/platforms/motionpy/tests/performance/latency_module_can.py",
        "PyTrinamicMicro/platforms/motionpy/tests/performance/latency_module_rs232.py",
        "PyTrinamicMicro/platforms/motionpy/tests/performance/latency_module_rs485.py",
        "PyTrinamicMicro/platforms/motionpy/tests/performance/throughput_module_can.py",
        "PyTrinamicMicro/platforms/motionpy/tests/performance/throughput_module_rs232.py",
        "PyTrinamicMicro/platforms/motionpy/tests/performance/throughput_module_rs485.py",
        "PyTrinamicMicro/platforms/motionpy/tests/tmcl_slave/tmcl_slave.py",
        "PyTrinamicMicro/platforms/motionpy/tests/scheduler.py",
        "PyTrinamicMicro/platforms/motionpy/tests/tmcl_bridge.py",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
    ],
    license='MIT',
)
