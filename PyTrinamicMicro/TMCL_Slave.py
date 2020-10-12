'''
Created on 07.10.2020

@author: LK
'''

# Imports
from PyTrinamic.TMCL import TMCL_Request, TMCL_Reply, TMCL_Status, TMCL_Command
from PyTrinamic.modules.TMCM_Python.TMCM_Python import TMCM_Python
import struct

class TMCL_Slave_Status(object):
    def __init__(self):
        self.stop = False

class TMCL_Slave(object):
    def __init__(self, module_address=1, host_address=2, version_string="0021V100", build_version=0):
        self.__module_address = module_address
        self.__host_address = host_address
        self.__version_string = version_string
        self.__build_version = build_version
        self._status = TMCL_Slave_Status()
        self.__subscript = ""
    def filter(self, request):
        return (request.moduleAddress == self.__module_address)
    def _get_command_func(self):
        return {
            TMCL_Command.GET_FIRMWARE_VERSION: self.get_version,
            TMCL_Command.SGP: self.set_global_parameter,
            TMCL_Command.GGP: self.get_global_parameter,
            TMCL_Command.TMCL_UF0: self.stop,
            TMCL_Command.TMCL_UF1: self.subscript
        }
    def get_status(self):
        return self._status
    def handle_request(self, request):
        reply = TMCL_Reply(reply_address=self.__host_address, module_address=self.__module_address, status=TMCL_Status.SUCCESS, value=0, command=request.command)

        command_func = self._get_command_func().get(request.command)
        if(command_func):
            reply = command_func(request, reply)
        else:
            reply.status = TMCL_Status.INVALID_COMMAND

        if(not(reply.special)):
            #reply.reply_address = self.__host_address
            reply.calculate_checksum()

        return reply
    def get_version(self, request, reply):
        func = {
            TMCM_Python.ENUMs.VERSION_FORMAT_ASCII: self.get_version_ascii,
            TMCM_Python.ENUMs.VERSION_FORMAT_BINARY: self.get_version_binary,
            TMCM_Python.ENUMs.VERSION_FORMAT_BUILD: self.get_version_build
        }.get(request.commandType)

        if(func):
            reply = func(request, reply)
        else:
            reply.status = TMCL_Status.WRONG_TYPE
        return reply
    def get_version_ascii(self, request, reply):
        reply_data = bytearray(1) + self.__version_string.encode("ascii")
        reply_data[0] = self.__host_address
        reply = TMCL_Reply.from_buffer(reply_data)
        reply.special = True
        return reply
    def get_version_binary(self, request, reply):
        version_module_high = int(self.__version_string[0:2])
        version_module_low = int(self.__version_string[2:4])
        version_fw_high = int(self.__version_string[5:6])
        version_fw_low = int(self.__version_string[6:8])
        reply.value = struct.unpack(">I", struct.pack("BBBB", version_module_high, version_module_low, version_fw_high, version_fw_low))[0]
        return reply
    def get_version_build(self, request, reply):
        reply.value = self.__build_version
        return reply
    def set_global_parameter(self, request, reply):
        if(request.commandType == self.GPs.controlHost):
            reply.value = self.__host_address = request.value
        elif(request.commandType == self.GPs.controlModule):
            reply.value = self.__module_address = request.value
        else:
            reply.status = TMCL_Status.WRONG_TYPE
        return reply
    def get_global_parameter(self, request, reply):
        if(request.commandType == self.GPs.controlHost):
            reply.value = self.__host_address
        elif(request.commandType == self.GPs.controlModule):
            reply.value = self.__module_address
        else:
            reply.status = TMCL_Status.WRONG_TYPE
        return reply
    def stop(self, request, reply):
        self._status.stop = True
        return reply
    def subscript(self, request, reply):
        func = {
            TMCM_Python.ENUMs.SUBSCRIPT_METHOD_EXECUTE: self.subscript_execute,
            TMCM_Python.ENUMs.SUBSCRIPT_METHOD_APPEND: self.subscript_append,
            TMCM_Python.ENUMs.SUBSCRIPT_METHOD_CLEAR: self.subscript_clear
        }.get(request.commandType)

        if(func):
            reply = func(request, reply)
        else:
            reply.status = TMCL_Status.WRONG_TYPE
        return reply
    def subscript_execute(self, request, reply):
        exec(open(self.__subscript).read())
        return reply
    def subscript_append(self, request, reply):
        self.__subscript += struct.pack(">I", request.value).decode("ascii")
        return reply
    def subscript_clear(self, request, reply):
        self.__subscript = ""
        return reply

class TMCL_Slave_Main(TMCL_Slave):
    def __init__(self, module_address=1, host_address=2, version_string="0021V100", build_version=0):
        super().__init__(module_address, host_address, version_string, build_version)

class TMCL_Slave_Bridge(TMCL_Slave):
    def __init__(self, module_address=3, host_address=2, version_string="0022V100", build_version=0):
        super().__init__(module_address, host_address, version_string, build_version)
