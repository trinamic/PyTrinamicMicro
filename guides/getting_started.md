# Getting Started

This is a guide on how to use the PyTrinamicMicro specific modules.  
For a MicroPython specific guide, please refer to [docs.micropython.org](https://docs.micropython.org).

## TMCM-0960-MotionPy preparation

This is on how to prepare the TMCM-0960-MotionPy reference board.  
If you are not using this, refer to the preparation guide of your target system and skip the
following steps.

1. Build the PYBv11 STM32 firmware. For that, refer to the [build guide](https://github.com/trinamic/micropython/blob/master/ports/stm32/README.md).  
*TL;DR*: `cd micropython && make -C mpy-cross PYTHON=python && cd ports/stm32 && make submodules PYTHON=python && make BOARD=PYBV11 PYTHON=python`,
assuming `python` is the linked Python binary.
2. Flash the `micropython/ports/stm32/build/firmware.hex` file using your favorite SWD interface.
3. Reset the board with a `low` signal on the `NRST` pin, or power cycle.

If you are developing on windows:  

4. (Re-)attach the board to the PC, without the SD card inserted in it.
5. The boards internal flash should be mounted as mass storage device directly.
Install the Serial Port Drivers `pybcdc.inf` from the root of the attached storage to your system.
6. Insert the SD card in the board and reattach it.

## General

1. Prepare the target system to run MicroPython. If there is already a MicroPython port available for the
target system, there might be a guide for that in the official MicroPython docs.
Make sure to also install the Serial Port Drivers for USB communication to work.
2. If the target platform is a microcontroller, there might be not enough space for the packages in the internal flash.
In that case, some kind of memory (i.e. SD card) needs to be provided and properly mounted.
Refer to the MicroPython docs on how to do this.
3. If the target platform is a microcontroller, plug in the MicroPython board to the PC.
It should already get detected as mass storage device, with the SD card mounted directly to the root.
4. Invoke the installation script `install.py`. For full installation, run the command `python install.py D:\`,
assuming `python` is properly linked to your python binary and `D:\` is the installation directory for the target platform.
As installing incrementally is not supported atm, invoke `python install.py D:\ -c` if you have already an installation
in that target directory.
5. Move the `main.py` and `boot.py` scripts for the desired platform manually out of `PyTrinamicMicro/platforms/x` to the platforms root.
6. Soft-Reset MicroPython by restarting it, or, if it is a microcontroller, hard-reset the microcontroller
with a `low` signal on the `NRST` pin, or power cycle.
7. If the target system is a microcontroller, connect to the corresponding serial port via terminal.
This might be `COMX` for Windows (determine *X* in the Device Manager), or `/dev/ttyACMX`
(determine *X* in the mounted devices in `/dev`) for Linux.
8. Now, being in the Python shell, any MicroPython compatible statement can be interpreted.
The PyTrinamicMicro package can be used.
Examples can be executed by e.g. `exec(MP.script("blinky"))`.

## Remarks

In the default environment for the target platform a global configuration class
is defined. This might be `PTM` (short for *PyTrinamicMicro*) in the general case.
For TMCM-0960-MotionPy this configuration class is wrapped and accessible as `MP` (short for *MotionPy*).
All of its members can be accessed statically and globally, especially from the Python shell.  
All global configuration is intended to be done in this class and its methods.
So make sure to use that whenever possible.

## Execute example scripts

By default, all example scripts can be executed via standard commands, i.e.

```Python
exec(open("PyTrinamicMicro/platforms/motionpy/examples/io/blinky.py").read())
```

Example scripts can also be linked manually by the user in the `MP` configuration class, and
executed via shortcut, i.e.

```Python
exec(MP.script("blinky"))
```

The script identifier (e.g. "blinky") is mapped internally to a corresponding script.
For the complete map, refer to [documentation](DOC.MD#PyTrinamicMicro).
