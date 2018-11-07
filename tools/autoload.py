import json
import win32gui
import win32api
import win32con
import win32clipboard
from ctypes import *
import time
import os

import group.function

VK_CODE = {
    'backspace': 0x08,
    'tab': 0x09,
    'clear': 0x0C,
    'enter': 0x0D,
    'shift': 0x10,
    'ctrl': 0x11,
    'alt': 0x12,
    'pause': 0x13,
    'caps_lock': 0x14,
    'esc': 0x1B,
    'spacebar': 0x20,
    'page_up': 0x21,
    'page_down': 0x22,
    'end': 0x23,
    'home': 0x24,
    'left_arrow': 0x25,
    'up_arrow': 0x26,
    'right_arrow': 0x27,
    'down_arrow': 0x28,
    'select': 0x29,
    'print': 0x2A,
    'execute': 0x2B,
    'print_screen': 0x2C,
    'ins': 0x2D,
    'del': 0x2E,
    'help': 0x2F,
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    'a': 0x41,
    'b': 0x42,
    'c': 0x43,
    'd': 0x44,
    'e': 0x45,
    'f': 0x46,
    'g': 0x47,
    'h': 0x48,
    'i': 0x49,
    'j': 0x4A,
    'k': 0x4B,
    'l': 0x4C,
    'm': 0x4D,
    'n': 0x4E,
    'o': 0x4F,
    'p': 0x50,
    'q': 0x51,
    'r': 0x52,
    's': 0x53,
    't': 0x54,
    'u': 0x55,
    'v': 0x56,
    'w': 0x57,
    'x': 0x58,
    'y': 0x59,
    'z': 0x5A,
    'numpad_0': 0x60,
    'numpad_1': 0x61,
    'numpad_2': 0x62,
    'numpad_3': 0x63,
    'numpad_4': 0x64,
    'numpad_5': 0x65,
    'numpad_6': 0x66,
    'numpad_7': 0x67,
    'numpad_8': 0x68,
    'numpad_9': 0x69,
    'multiply_key': 0x6A,
    'add_key': 0x6B,
    'separator_key': 0x6C,
    'subtract_key': 0x6D,
    'decimal_key': 0x6E,
    'divide_key': 0x6F,
    'F1': 0x70,
    'F2': 0x71,
    'F3': 0x72,
    'F4': 0x73,
    'F5': 0x74,
    'F6': 0x75,
    'F7': 0x76,
    'F8': 0x77,
    'F9': 0x78,
    'F10': 0x79,
    'F11': 0x7A,
    'F12': 0x7B,
    'F13': 0x7C,
    'F14': 0x7D,
    'F15': 0x7E,
    'F16': 0x7F,
    'F17': 0x80,
    'F18': 0x81,
    'F19': 0x82,
    'F20': 0x83,
    'F21': 0x84,
    'F22': 0x85,
    'F23': 0x86,
    'F24': 0x87,
    'num_lock': 0x90,
    'scroll_lock': 0x91,
    'left_shift': 0xA0,
    'right_shift ': 0xA1,
    'left_control': 0xA2,
    'right_control': 0xA3,
    'left_menu': 0xA4,
    'right_menu': 0xA5,
    'browser_back': 0xA6,
    'browser_forward': 0xA7,
    'browser_refresh': 0xA8,
    'browser_stop': 0xA9,
    'browser_search': 0xAA,
    'browser_favorites': 0xAB,
    'browser_start_and_home': 0xAC,
    'volume_mute': 0xAD,
    'volume_Down': 0xAE,
    'volume_up': 0xAF,
    'next_track': 0xB0,
    'previous_track': 0xB1,
    'stop_media': 0xB2,
    'play/pause_media': 0xB3,
    'start_mail': 0xB4,
    'select_media': 0xB5,
    'start_application_1': 0xB6,
    'start_application_2': 0xB7,
    'attn_key': 0xF6,
    'crsel_key': 0xF7,
    'exsel_key': 0xF8,
    'play_key': 0xFA,
    'zoom_key': 0xFB,
    'clear_key': 0xFE,
    '+': 0xBB,
    ',': 0xBC,
    '-': 0xBD,
    '.': 0xBE,
    '/': 0xBF,
    '\`': 0xC0,
    ';': 0xBA,
    '[': 0xDB,
    '\\': 0xDC,
    ']': 0xDD,
    "'": 0xDE,
    '`': 0xC0}


def mouse_move(x, y):
    windll.user32.SetCursorPos(x, y)


def load_file(file_path_list, save_path):
    window_unity_studio = win32gui.FindWindow(None, 'unity studio')
    win32gui.SetWindowPos(window_unity_studio, win32con.HWND_NOTOPMOST, 100, 0, 1000, 1000, win32con.SWP_NOSIZE)
    win32gui.SetForegroundWindow(window_unity_studio)

    for name in file_path_list:
        # click press "file"
        mouse_move(120, 45)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 点击鼠标
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

        # click press "load file"
        mouse_move(130, 60)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 点击鼠标
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(0.05)

        # set ship_file path into the Clipboard
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, name)
        win32clipboard.CloseClipboard()

        # key down "Ctrl+V"
        win32api.keybd_event(VK_CODE['ctrl'], 0, 0, 0)
        win32api.keybd_event(VK_CODE['v'], 0, 0, 0)
        win32api.keybd_event(VK_CODE['v'], 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(VK_CODE['ctrl'], 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.05)

        # click press "确定"
        mouse_move(700, 485)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 点击鼠标
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        # wait loading
        time.sleep(1)
        # click press "asset list"
        mouse_move(220, 75)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 点击鼠标
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

        # click press “export”
        mouse_move(230, 40)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 点击鼠标
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(0.5)
        # click press "all asset"
        mouse_move(230, 60)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 点击鼠标
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(0.5)
        # set the save path into the clipboard
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, save_path, )
        win32clipboard.CloseClipboard()
        # key down "ctrl+V"
        win32api.keybd_event(VK_CODE['ctrl'], 0, 0, 0)
        win32api.keybd_event(VK_CODE['v'], 0, 0, 0)
        win32api.keybd_event(VK_CODE['v'], 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(VK_CODE['ctrl'], 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.05)

        # click press "yes"
        mouse_move(700, 485)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 点击鼠标
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        # wait finish save
        time.sleep(3)

        # get the unity studio's window
        window_unity_studio = win32gui.FindWindow(None, 'unity studio - no productName - 5.6.5p3 - Android')
        # set the pos
        win32gui.SetWindowPos(window_unity_studio, win32con.HWND_NOTOPMOST, 100, 0, 1000, 1000, win32con.SWP_NOSIZE)
        # active the window
        win32gui.SetForegroundWindow(window_unity_studio)


def auto_load():
    """main part
    use for loop to export all unity type file"""
    path = os.getcwd()
    unity = path + "\\UnityStudio\\UnityStudio.exe"
    os.system("start " + unity)
    time.sleep(3)
    filelist = group.function.all_file_path('painting')[0]

    for index in range(len(filelist)):
        filelist[index] = path + '\\' + filelist[index]

    load_file(filelist, path)

    time.sleep(2)
    os.system("taskkill /f /im unitystudio.exe")


def compare():
    """remove the file which have exported"""
    texture2d = group.function.all_file('Texture2D')
    Mesh = group.function.all_file('Mesh')
    file_list = group.function.all_file('painting')
    for index in range(len(texture2d)):
        texture2d[index] = texture2d[index].split('.')[0].lower()
        cuts = texture2d[index].split('_')

        if cuts[-1] == 'hx' or cuts[-1] == 'bd':
            texture2d[index] = ''
            for cut in cuts[:-1]:
                texture2d[index] += '%s_' % cut
            texture2d[index] = texture2d[index][:-1]

    for index in range(len(Mesh)):
        Mesh[index] = Mesh[index].split('.')[0].lower()
        cuts = Mesh[index].split('-')
        Mesh[index] = cuts[0]

    for index in range(len(file_list)):
        cuts = file_list[index].split('_')
        if cuts[-1] == 'tex':
            file_list[index] = ''
            for cut in cuts[:-1]:
                file_list[index] += '%s_' % cut
                file_list[index] = file_list[index][:-1]
        else:
            pass

    file_list = set(file_list)

    for tex in texture2d:
        if tex in file_list:
            try:
                os.remove('painting\\%s_tex' % tex)
            except FileNotFoundError:
                pass
    for mesh in Mesh:
        if mesh in file_list:
            try:
                os.remove('painting\\%s' % mesh)
            except FileNotFoundError:
                pass
    try:
        with open('files\\nomeshfile.json', 'r')as file:
            differ_list = json.load(file)
    except FileNotFoundError:
        differ_list = []
    for each in differ_list:
        try:
            os.remove('painting\\%s' % each)
        except FileNotFoundError:
            pass
