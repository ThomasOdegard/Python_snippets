import os
import ctypes
import ctypes.util

class XFixesCursorImage(ctypes.Structure):

    """ 
        See /usr/include/X11/extensions/Xfixes.h
        https://docs.python.org/3/library/ctypes.html

        typedef struct {
            short	    x, y;
            unsigned short  width, height;
            unsigned short  xhot, yhot;
            unsigned long   cursor_serial;
            unsigned long   *pixels;
        if XFIXES_MAJOR >= 2
            Atom	    atom;	/* Version >= 2 only */
            const char	*name;	/* Version >= 2 only */
        endif
        } XFixesCursorImage;
    """

    _fields_ = [
                ('x', ctypes.c_short),
                ('y', ctypes.c_short),
                ('width', ctypes.c_ushort),
                ('height', ctypes.c_ushort),
                ('xhot', ctypes.c_ushort),
                ('yhot', ctypes.c_ushort),
                ('cursor_serial', ctypes.c_ulong),
                ('pixels', ctypes.c_ulong),
                ('atom', ctypes.c_ulong),
                ('name', ctypes.c_char_p)
                ]

class Display(ctypes.Structure):
    pass

class X11cursor:
    display = None

    def __init__(self, display=None):
        if not display:
            try:
                display = os.environ["DISPLAY"].encode("utf-8")
            except KeyError:
                raise Exception("$DISPLAY not set.")

        XFixes_lib_chk = ctypes.util.find_library("Xfixes")
        # TODO: Version control - Major >= 2
        if not XFixes_lib_chk:
            raise Exception("No XFixes library found.")
        self.XFixeslib = ctypes.cdll.LoadLibrary(XFixes_lib_chk)

        x11_lib_chk = ctypes.util.find_library("X11")
        if not x11_lib_chk:
            raise Exception("No X11 library found.")
        self.xlib = ctypes.cdll.LoadLibrary(x11_lib_chk)

        XFixesGetCursorImage = self.XFixeslib.XFixesGetCursorImage
        XFixesGetCursorImage.restype = ctypes.POINTER(XFixesCursorImage)
        XFixesGetCursorImage.argtypes = [ctypes.POINTER(Display)]
        self.XFixesGetCursorImage = XFixesGetCursorImage

        XOpenDisplay = self.xlib.XOpenDisplay
        XOpenDisplay.restype = ctypes.POINTER(Display)
        XOpenDisplay.argtypes = [ctypes.c_char_p]

        if not self.display:
            self.display = self.xlib.XOpenDisplay(display)

    def getCursorStyle(self):
        cursor_data = self.XFixesGetCursorImage(self.display)
        return cursor_data[0]


if __name__ == "__main__":
    cursor = X11cursor()

    # Move mouse over different elements while running.
    while True:
        print(cursor.getCursorStyle().name)
