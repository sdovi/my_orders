import pyautogui
import panedwindow as gw
import time


def get_browser_windows():
    yandex_window = None
    edge_window = None
    for window in gw.getAllWindows():
        if 'Yandex' in window.title:
            yandex_window = window
        elif 'Microsoft Edge' in window.title:
            edge_window = window
    return yandex_window, edge_window


def mirror_mouse_events(yandex_window, edge_window):
    if not yandex_window or not edge_window:
        print("Could not find both browser windows.")
        return

    while True:
        x, y = pyautogui.position()
        in_yandex = yandex_window.left <= x <= yandex_window.right and yandex_window.top <= y <= yandex_window.bottom
        if in_yandex:
            # Convert coordinates to relative positions in the Yandex window
            rel_x = x - yandex_window.left
            rel_y = y - yandex_window.top
            # Convert relative positions to coordinates in the Edge window
            edge_x = edge_window.left + rel_x
            edge_y = edge_window.top + rel_y
            pyautogui.moveTo(edge_x, edge_y)

            if pyautogui.mouseDown():
                pyautogui.mouseDown(edge_x, edge_y)
            if pyautogui.mouseUp():
                pyautogui.mouseUp(edge_x, edge_y)

        time.sleep(0.01)


yandex_window, edge_window = get_browser_windows()
mirror_mouse_events(yandex_window, edge_window)
