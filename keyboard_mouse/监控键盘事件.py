#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 9:12
# @Author  : ZhangChaowei

"""
使用pynput.keyboard.Listener监听键盘事件
"""

from pynput import keyboard


def on_press(key):
    try:
        print(f'字母 {key.char} 被按下了')
    except AttributeError:
        print(f'特殊的键 {key} 被按下了')


def on_release(key):
    print(f'{key} 被释放了')
    if key == keyboard.Key.esc:
        # 停止监听
        return False


if __name__ == '__main__':
    with keyboard.Listener(on_press=on_press, on_release=on_press) as listener:
        listener.join()




