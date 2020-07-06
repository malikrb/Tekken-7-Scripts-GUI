import psutil
import ctypes
import sys
import os

from pymem.ressources import kernel32
from ctypes.wintypes import *
from ctypes import *


# ------------- CONSTANTS ------------- #


PROCESS_VM_READ = 0x0010
TH32CS_SNAPMODULE = 0x00000008
TH32CS_SNAPMODULE32 = 0x00000010

OpenProcess = kernel32.OpenProcess
ReadProcessMemory = kernel32.ReadProcessMemory

Module32Next = ctypes.windll.kernel32.Module32Next
Module32First = ctypes.windll.kernel32.Module32First

GetForegroundWindow = ctypes.windll.user32.GetForegroundWindow
GetWindowThreadProcessId = ctypes.windll.user32.GetWindowThreadProcessId


MAX_PATH = 260
MAX_MODULE_NAME32 = 255 + 1

INVALID_HANDLE_VALUE = -1


# ------------- FUNCTIONS ------------- #


class MODULEENTRY32(ctypes.Structure):
    _fields_ = [("dwSize", DWORD),
                ("th32ModuleID", DWORD),
                ("th32ProcessID", DWORD),
                ("GlblcntUsage", DWORD),
                ("ProccntUsage", DWORD),
                ("modBaseAddr", POINTER(BYTE)),
                ("modBaseSize", DWORD),
                ("hModule", HMODULE),
                ("szModule", c_char*MAX_MODULE_NAME32),
                ("szExePath", c_char*MAX_PATH)]

def GetPid(name: str) -> DWORD:
    for process in psutil.process_iter():
        if process.name() == name:
            return process.pid

    return 0

def GetModule(name: str, pid: DWORD) -> MODULEENTRY32:
    modEntry = MODULEENTRY32()
    hSnapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPMODULE | TH32CS_SNAPMODULE32, pid)

    if hSnapshot != INVALID_HANDLE_VALUE:
        curr = MODULEENTRY32()
        curr.dwSize = ctypes.sizeof(MODULEENTRY32)

        if Module32First(hSnapshot, ctypes.byref(curr)):
            while True:
                if curr.szModule != name:
                    modEntry = curr
                    break

                if not Module32Next(hSnapshot, ctypes.byref(curr)):
                    break
                    
        kernel32.CloseHandle(hSnapshot)

    return modEntry

def GetModuleBaseAddress(module: MODULEENTRY32) -> int:
    LPCB = POINTER(c_ulonglong)
    return LPCB(module.modBaseAddr).contents.value

def GetTekkenInfo(name="TekkenGame-Win64-Shipping.exe") -> tuple:
    pid = GetPid(name)
    if pid:
        module = GetModule(name, pid)
        baseAddress = GetModuleBaseAddress(module)

        data = c_uint8()
        bytesread = c_ulonglong(0)
        processHandle = OpenProcess(PROCESS_VM_READ, False, pid)

        return processHandle, baseAddress, data, bytesread

    else:
        print("Tekken Not Found.\n")
        os.system("pause")
        os.system("cls")
        os._exit(1)

def WhichSide(processHandle, baseAddress, offset, data, bytesread=c_ulonglong(0)):
    ReadProcessMemory(processHandle, baseAddress + offset, byref(data), sizeof(data), byref(bytesread))
    return data.value

def IsIngame(processHandle, baseAddress, offset, data, bytesread=c_ulonglong(0)):
    ReadProcessMemory(processHandle, baseAddress + offset, byref(data), sizeof(data), byref(bytesread))
    return data.value

def IsForeground(processId) -> bool:
    result = DWORD()
    HWND = GetForegroundWindow()
    GetWindowThreadProcessId(HWND, byref(result))
    
    if result.value == processId:
        return True

    return False


# ---------------- DEBUG ----------------- #


if __name__ == "__main__":
    game = "TekkenGame-Win64-Shipping.exe"
    pid = GetPid(name=game)
    print(pid)

    mod = GetModule(game, pid)
    base = GetModuleBaseAddress(mod)

    HWND, BASEADDRESS, DATA, BYTESREAD = GetTekkenInfo()

    print(base)
