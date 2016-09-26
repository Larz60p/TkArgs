"""
The MIT License (MIT)

Copyright (c) <2016> <Larry McCaig (aka: Larz60+ aka: Larz60p)>

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import json


class MakeTkArgsDb:
    def __init__(self):
        self.commands = {
            'activebackground': {
                'command_line': '-activebackground',
                'database_class': 'Foreground',
                'description': 'Specifies background color to use when drawing active elements. '
                               'An element (a widget or portion of a widget) is active if the '
                               'mouse cursor is positioned over the element and pressing a '
                               'mouse button will cause some action to occur. If strict Motif '
                               'compliance has been requested by setting the tk_strictMotif '
                               'variable, this option will normally be ignored; the normal '
                               'background color will be used instead. For some elements on '
                               'Windows and Macintosh systems, the active color will only be '
                               'used while mouse button 1 is pressed over the element.',
                'valid_for': [
                    'Misc.tk_setPalette', 'Button', 'Checkbutton', 'Label', 'Menu',
                    'Radiobutton', 'Scale', 'Scrollbar', 'Spinbox',
                ],
                'value_type': 'color'
            },
            'activeforeground': {
                'command_line': '-activeforeground',
                'database_class': 'Background',
                'description': 'Specifies foreground color to use when drawing active elements. '
                               'See above for definition of active elements.',
                'valid_for': [
                    'Misc.tk_setPalette', 'Button', 'Checkbutton', 'Label', 'Menu', 'Radiobutton'
                ],
                'value_type': 'color'
            },
            'anchor': {
                'command_line': '-anchor',
                'database_class': 'Anchor',
                'description': 'Specifies how the information in a widget (e.g. text or a bitmap) '
                               'is to be displayed in the widget. Must be one of the values n, '
                               'ne, e, se, s, sw, w, nw, or center. For example, nw means display '
                               'the information such that its top-left corner is at the top-left '
                               'corner of the widget.',
                'valid_for': [
                    'grid_anchor', 'Pack', 'Place', 'Button', 'Checkbutton', 'Label', 'Radiobutton',
                    'OptionMenu', 'LabelFrame'
                ],
                'value_type': 'compass_point'
            },
            'background': {
                'command_line': '-background or -bg',
                'database_class': 'Background',
                'description': 'Specifies the normal background color to use when displaying the '
                               'widget.',
                'valid_for': [
                    'Misc.tk_setPalette', 'Toplevel', 'Button', 'Canvas', 'Checkbutton', 'Entry',
                    'Frame', 'Label', 'Listbox', 'Menu', 'Radiobutton', 'Scale', 'Scrollbar',
                    'Text', 'BitmapImage', 'Spinbox', 'LabelFrame', 'PanedWindow'
                ],
                'value_type': 'color'
            },
            'bitmap': {
                'command_line': 'bitmap',
                'database_class': 'Bitmap',
                'description': 'Specifies a bitmap to display in the widget, in any of the forms '
                               'acceptable to Tk_GetBitmap. The exact way in which the bitmap is '
                               'displayed may be affected by other options such as anchor or '
                               'justify. Typically, if this option is specified then it overrides '
                               'other options that specify a textual value to display in the '
                               'widget but this is controlled by the compound option; the bitmap '
                               'option may be reset to an empty string to re-enable a text '
                               'display. In widgets that support both bitmap and image options, '
                               'image will usually override bitmap.',
                'valid_for': [
                    'Wm.wm_iconbitmap', 'Wm.wm_iconmask', 'Button', 'create_bitmap', 'Checkbutton',
                    'Label', 'Radiobutton', 'Image.type', 'BitmapImage'
                ],
                'value_type': 'X11_bitmaps'
            },
            'borderWidth': {
                'command_line': '-borderwidth or -bd',
                'database_class': 'BorderWidth',
                'description': 'Specifies a non-negative value indicating the width of the 3-D '
                               'border to draw around the outside of the widget (if such a '
                               'border is being drawn; the relief option typically determines '
                               'this). The value may also be used when drawing 3-D effects in '
                               'the interior of the widget. The value may have any of the forms '
                               'acceptable to Tk_GetPixels.',
                'valid_for': [
                    'Toplevel', 'Button', 'Canvas', 'Checkbutton', 'Entry', 'Frame', 'Label',
                    'Listbox', 'Menu', 'Radiobutton', 'Scale', 'Scrollbar', 'Text', 'OptionMenu',
                    'Spinbox', 'LabelFrame', 'PanedWindow'
                ],
                'value_type': 'int'
            },
            'cursor': {
                'command_line': '-cursor',
                'database_class': 'Cursor',
                'description': 'Specifies the mouse cursor to be used for the widget. The value '
                               'may have any of the forms acceptable to Tk_GetCursor. examples:'
                               'arrow, boat, pencil, man, ... see Grayson page 13',
                'valid_for': [
                    'Toplevel', 'Button', 'Canvas', 'Canvas.icursor', 'Canvas.index',
                    'Canvas.select_adjust', 'Checkbutton', 'Entry', 'Entry.icursor', 'Entry.index',
                    'Entry.selection_adjust', 'Frame', 'Label', 'Listbox', 'Menu', 'Radiobutton',
                    'Scale', 'Scrollbar', 'Text', 'Spinbox', 'Spinbox.icursor', 'LabelFrame',
                    'PanedWindow'
                ],
                'value_type': 'str'
            },
            'compound': {
                'command_line': '-compound',
                'database_class': 'Compound',
                'description': 'Specifies if the widget should display text and bitmaps/images '
                               'at the same time, and if so, where the bitmap/image should be '
                               'placed relative to the text. Must be one of the values none, '
                               'bottom, top, left, right, or center. For example, the (default) '
                               'value none specifies that the bitmap or image should (if defined) '
                               'be displayed instead of the text, the value left specifies that '
                               'the bitmap or image should be displayed to the left of the text, '
                               'and the value center specifies that the bitmap or image should '
                               'be displayed on top of the text.',
                'valid_for': [
                    'Button'
                ],
                'value_type': 'LEFT, RIGHT, CENTER, TOP, BOTTOM'
            },
            'disabledForeground': {
                'command_line': '-disabledforeground',
                'database_class': 'DisabledForeground',
                'description': 'Specifies foreground color to use when drawing a disabled '
                               'element. If the option is specified as an empty string (which '
                               'is typically the case on monochrome displays),  disabled '
                               'elements are drawn with the normal foreground color but they '
                               'are dimmed by drawing them with a stippled fill pattern.',
                'valid_for': [
                    'Misc.tk_setPalette', 'Button', 'Checkbutton', 'Label', 'Menu',
                    'Radiobutton', 'Spinbox'
                ],
                'value_type': 'color'
            },
            'exportselection': {
                'command_line': '-exportselection',
                'database_class': 'ExportSelection',
                'description': 'Specifies whether or not a selection in the widget should also '
                               'be the X selection. The value may have any of the forms '
                               'accepted by Tcl_GetBoolean, such as true, false, 0, 1, yes, or '
                               'no. If the selection is exported, then selecting in the widget '
                               'deselects the current X selection, selecting outside the widget '
                               'deselects any widget selection, and the widget will respond to '
                               'selection retrieval requests when it has a selection. The '
                               'default is usually for widgets to export selections.',
                'valid_for': [
                    'Entry', 'Listbox', 'Text', 'Spinbox'
                ],
                'value_type': 'boolean'
            },
            'font': {
                'command_line': '-font',
                'database_class': 'Font',
                'description': 'Specifies the font to use when drawing text inside the widget. '
                               'The value may have any of the forms accepted by Tk_GetFont.',
                'valid_for': [
                    'Button', 'Checkbutton', 'Entry', 'Label', 'Listbox', 'Menu', 'Radiobutton',
                    'Scale', 'Text', 'Spinbox', 'LabelFrame'
                ],
                'value_type': 'font - see https://www.tcl.tk/man/tcl8.4/TkCmd/font.htm'
            },
            'foreground': {
                'command_line': '-foreground or -fg',
                'database_class': 'Foreground',
                'description': 'Specifies the normal foreground color to use when displaying '
                               'the widget.',
                'valid_for': [
                    'Misc.tk_setPalette', 'Button', 'Canvas', 'Checkbutton', 'Entry', 'Label',
                    'Listbox', 'Listbox.itemconfigure', 'Menu', 'Radiobutton', 'Scale',
                    'Text', 'BitmapImage', 'Spinbox', 'LabelFrame'
                ],
                'value_type': 'color'
            },
            'highlightbackground': {
                'command_line': '-highlightbackground',
                'database_class': 'HighlightBackground',
                'description': 'Specifies the color to display in the traversal highlight '
                               'region when the widget does not have the input focus.',
                'valid_for': [
                    'Misc.tk_setPalette', 'Toplevel', 'Button', 'Canvas', 'Checkbutton',
                    'Entry', 'Frame', 'Label', 'Listbox', 'Radiobutton', 'Scale',
                    'Scrollbar', 'Text', 'Spinbox', 'LabelFrame'
                ],
                'value_type': 'color'
            },
            'highlightcolor': {
                'command_line': '-highlightcolor',
                'database_class': 'HighlightColor',
                'description': 'Specifies the color to use for the traversal highlight '
                               'rectangle that is drawn around the widget when it has the '
                               'input focus.',
                'valid_for': [
                    'Misc.tk_setPalette', 'Toplevel', 'Button', 'Canvas', 'Checkbutton',
                    'Entry', 'Frame', 'Label', 'Listbox', 'Radiobutton', 'Scale',
                    'Scrollbar', 'Text', 'Spinbox', 'LabelFrame'
                ],
                'value_type': 'color'
            },
            'highlightthickness': {
                'command_line': '-highlightthickness',
                'database_class': 'HighlightThickness',
                'description': 'Specifies a non-negative value indicating the width of the '
                               'highlight rectangle to draw around the outside of the widget '
                               'when it has the input focus. The value may have any of the '
                               'forms acceptable to Tk_GetPixels. If the value is zero, no '
                               'focus highlight is drawn around the widget.',
                'valid_for': [
                    'Toplevel', 'Button', 'Canvas', 'Checkbutton', 'Entry', 'Frame', 'Label',
                    'Listbox', 'Radiobutton', 'Scale', 'Scrollbar', 'Text', 'OptionMeu',
                    'Spinbox', 'LabelFrame'
                ],
                'value_type': 'int'
            },
            'image': {
                'command_line': '-image',
                'database_class': 'Image',
                'description': 'Specifies an image to display in the widget, which must have '
                               'been created with the image create command. Typically, if the '
                               'image option is specified then it overrides other options '
                               'that specify a bitmap or textual value to display in the '
                               'widget, though this is controlled by the compound option; '
                               'the image option may be reset to an empty string to re-enable '
                               'a bitmap or text display.',
                'valid_for': [
                    'Misc.image_names', 'Misc.image_types', 'Misc.image_name', 'Button',
                    'Button.create_image', 'Checkbutton', 'Label', 'Radiobutton',
                    'Text.image_cget', 'Text.image_configure', 'Text.image_create',
                    'Text.image_names', 'Image', 'Image.__del__', 'Image.configure',
                    'Image.height', 'Image.type', 'Image.width', 'PhotoImage',
                    'PhotoImage.blank', 'PhotoImage.copy', 'PhotoImage.zoom',
                    'PhotoImage.subsample', 'PhotoImage.put', 'PhotoImage.write', 'image_names',
                    'image_types'
                ],
                'value_type': 'image_name'
            },
            'insertbackground': {
                'command_line': '-insertbackground',
                'database_class': 'Foreground',
                'description': 'Specifies the color to use as background in the area covered '
                               'by the insertion cursor. This color will normally override '
                               'either the normal background for the widget (or the selection '
                               'background if the insertion cursor happens to fall in the '
                               'selection).',
                'valid_for': [
                    'Misc.tk_setPalette', 'Canvas', 'Entry', 'Text', 'Spinbox'
                ],
                'value_type': 'color'
            },
            'insertborderWidth': {
                'command_line': '-insertborderwidth',
                'database_class': 'BorderWidth',
                'description': 'Specifies a non-negative value indicating the width of the '
                               '3-D border to draw around the insertion cursor. The value '
                               'may have any of the forms acceptable to Tk_GetPixels.',
                'valid_for': [
                    'Canvas', 'Entry', 'Text', 'Spinbox'
                ],
                'value_type': 'int'
            },
            'insertofftime': {
                'command_line': '-insertofftime',
                'database_class': 'OffTime',
                'description': 'Specifies a non-negative integer value indicating the number '
                               'of milliseconds the insertion cursor should remain ``off'' '
                               'in each blink cycle. If this option is zero then the cursor '
                               'doesn''t blink: it is on all the time.',
                'valid_for': [
                    'Canvas', 'Entry', 'Text', 'Spinbox'
                ],
                'value_type': 'int'
            },
            'insertontime': {
                'command_line': '-insertontime',
                'database_class': 'OnTime',
                'description': 'Specifies a non-negative integer value indicating the number '
                               'of milliseconds the insertion cursor should remain ``on'' in '
                               'each blink cycle.',
                'valid_for': [
                    'Canvas', 'Entry', 'Text', 'Spinbox'
                ],
                'value_type': 'int'
            },
            'insertwidth': {
                'command_line': '-insertwidth',
                'database_class': 'InsertWidth',
                'description': 'Specifies a value indicating the total width of the '
                               'insertion cursor. The value may have any of the forms '
                               'acceptable to Tk_GetPixels. If a border has been specified '
                               'for the insertion cursor (using the insertBorderWidth '
                               'option), the border will be drawn inside the width '
                               'specified by the insertWidth option.',
                'valid_for': [
                    'Canvas', 'Entry', 'Text', 'Spinbox'
                ],
                'value_type': 'int'
            },
            'jump': {
                'command_line': '-jump',
                'database_class': 'Jump',
                'description': 'For widgets with a slider that can be dragged to adjust a '
                               'value, such as scrollbars, this option determines when '
                               'notifications are made about changes in the value. The '
                               'option''s value must be a boolean of the form accepted by '
                               'Tcl_GetBoolean. If the value is false, updates are made '
                               'continuously as the slider is dragged. If the value is '
                               'true, updates are delayed until the mouse button is released '
                               'to end the drag; at that point a single notification is '
                               'made (the value ``jumps'' rather than changing smoothly).',
                'valid_for': [
                    'Scrollbar'
                ],
                'value_type': 'boolean'
            },
            'justify': {
                'command_line': '-justify',
                'database_class': 'Justify',
                'description': 'When there are multiple lines of text displayed in a widget, '
                               'this option determines how the lines line up with each other. '
                               'Must be one of left, center, or right. Left means that the '
                               'lines'' left edges all line up, center means that the lines'' '
                               'centers are aligned, and right means that the lines'' right '
                               'edges line up.',
                'valid_for': [
                    'Button', 'Checkbutton', 'Entry', 'Label', 'Radiobutton', 'Spinbox'
                ],
                'value_type': ''
            },
            'orient': {
                'command_line': '-orient',
                'database_class': 'Orient',
                'description': 'For widgets that can lay themselves out with either a '
                               'horizontal or vertical orientation, such as scrollbars, '
                               'this option specifies which orientation should be used. '
                               'Must be either horizontal or vertical or an abbreviation '
                               'of one of these.',
                'valid_for': [
                    'Scale', 'Scrollbar', 'PanedWindow'
                ],
                'value_type': 'HORIZONTAL or VERTICAL'
            },
            'padx': {
                'command_line': '-padx',
                'database_class': 'Pad',
                'description': 'Specifies a non-negative value indicating how much extra '
                               'space to request for the widget in the X-direction. The '
                               'value may have any of the forms acceptable to Tk_'
                               'GetPixels. When computing how large a window it needs, '
                               'the widget will add this amount to the width it would '
                               'normally need (as determined by the width of the things '
                               'displayed in the widget); if the geometry manager can '
                               'satisfy this request, the widget will end up with extra '
                               'internal space to the left and/or right of what it displays '
                               'inside. Most widgets only use this option for padding text: '
                               'if they are displaying a bitmap or image, then they usually '
                               'ignore padding options.',
                'valid_for': [
                    'Pack', 'Grid', 'Button', 'Checkbutton', 'Label', 'Radiobutton',
                    'Text', 'LabelFrame', 'PanedWindow.paneconfigure'
                ],
                'value_type': 'int'
            },
            'pady': {
                'command_line': '-pady',
                'database_class': 'Pad',
                'description': 'Specifies a non-negative value indicating how much extra space '
                               'to request for the widget in the Y-direction. The value may '
                               'have any of the forms acceptable to Tk_GetPixels. When '
                               'computing how large a window it needs, the widget will add '
                               'this amount to the height it would normally need (as determined '
                               'by the height of the things displayed in the widget); if the '
                               'geometry manager can satisfy this request, the widget will end '
                               'up with extra internal space above and/or below what it '
                               'displays inside. Most widgets only use this option for padding '
                               'text: if they are displaying a bitmap or image, then they '
                               'usually ignore padding options.',
                'valid_for': [
                    'Pack', 'Grid', 'Button', 'Checkbutton', 'Label', 'Radiobutton',
                    'Text', 'LabelFrame', 'PanedWindow.paneconfigure'
                ],
                'value_type': 'int'
            },
            'relief': {
                'command_line': '-relief',
                'database_class': 'Relief',
                'description': 'Specifies the 3-D effect desired for the widget. Acceptable '
                               'values are raised, sunken, flat, ridge, solid, and groove. '
                               'The value indicates how the interior of the widget should '
                               'appear relative to its exterior; for example, raised means '
                               'the interior of the widget should appear to protrude from '
                               'the screen, relative to the exterior of the widget.',
                'valid_for': [
                    'Toplevel', 'Button', 'Canvas', 'Checkbutton', 'Entry', 'Frame', 'Label',
                    'Listbox', 'Menu', 'Radiobutton', 'Scale', 'Scrollbar', 'Text',
                    'OptionMenu', 'Spinbox', 'LabelFrame', 'PanedWindow'
                ],
                'value_type': 'SUNKEN, FLAT, RAISED, GROOVE, or RIDGE'
            },
            'repeatdelay': {
                'command_line': '-repeatdelay',
                'database_class': 'RepeatDelay',
                'description': 'Specifies the number of milliseconds a button or key must '
                               'be held down before it begins to auto-repeat. Used, for '
                               'example, on the up- and down-arrows in scrollbars.',
                'valid_for': [
                    'Button', 'Scale', 'Scrollbar', 'Spinbox'
                ],
                'value_type': 'int'
            },
            'repeatinterval': {
                'command_line': '-repeatinterval',
                'database_class': 'RepeatInterval',
                'description': 'Used in conjunction with repeatDelay: once auto-repeat begins, '
                               'this option determines the number of milliseconds between '
                               'auto-repeats.',
                'valid_for': [
                    'Button', 'Scale', 'Scrollbar', 'Spinbox'
                ],
                'value_type': 'int'
            },
            'selectbackground': {
                'command_line': '-selectbackground',
                'database_class': 'Foreground',
                'description': 'Specifies the background color to use when displaying '
                               'selected items.',
                'valid_for': [
                    'Misc.tk_setPalette', 'Canvas', 'Entry', 'Listbox', 'Listbox.itemconfigure',
                    'Text', 'Spinbox'
                ],
                'value_type': 'color'
            },
            'selectborderWidth': {
                'command_line': '-selectborderwidth',
                'database_class': 'BorderWidth',
                'description': 'Specifies a non-negative value indicating the width of the '
                               '3-D border to draw around selected items. The value may '
                               'have any of the forms acceptable to Tk_GetPixels.',
                'valid_for': [
                    'Canvas', 'Entry', 'Listbox', 'Text', 'Spinbox'
                ],
                'value_type': 'int'
            },
            'selectforeground': {
                'command_line': '-selectforeground',
                'database_class': 'Background',
                'description': 'Specifies the foreground color to use when displaying selected '
                               'items.',
                'valid_for': [
                    'Misc.tk_setPalette', 'Canvas', 'Entry', 'Listbox', 'Listbox.itemconfigure',
                    'Text', 'Spinbox'
                ],
                'value_type': 'color'
            },
            'setgrid': {
                'command_line': '-setgrid',
                'database_class': 'SetGrid',
                'description': 'Specifies a boolean value that determines whether this '
                               'widget controls the resizing grid for its top-level window. '
                               'This option is typically used in text widgets, where the '
                               'information in the widget has a natural size (the size of '
                               'a character) and it makes sense for the window''s '
                               'dimensions to be integral numbers of these units. These '
                               'natural window sizes form a grid. If the setGrid option is '
                               'set to true then the widget will communicate with the '
                               'window manager so that when the user interactively resizes '
                               'the top-level window that contains the widget, the '
                               'dimensions of the window will be displayed to the user in '
                               'grid units and the window size will be constrained to '
                               'integral numbers of grid units. See the section GRIDDED '
                               'GEOMETRY MANAGEMENT in the wm manual entry for more details.',
                'valid_for': [
                    'Listbox', 'Text'
                ],
                'value_type': 'boolean'
            },
            'takefocus': {
                'command_line': '-takefocus',
                'database_class': 'TakeFocus',
                'description': 'Determines whether the window accepts the focus during '
                               'keyboard traversal (e.g., Tab and Shift-Tab). Before setting '
                               'the focus to a window, the traversal scripts consult the '
                               'value of the takeFocus option. A value of 0 means that the '
                               'window should be skipped entirely during keyboard traversal. '
                               '1 means that the window should receive the input focus as '
                               'long as it is viewable (it and all of its ancestors are '
                               'mapped). An empty value for the option means that the '
                               'traversal scripts make the decision about whether or not '
                               'to focus on the window: the current algorithm is to skip '
                               'the window if it is disabled, if it has no key bindings, '
                               'or if it is not viewable. If the value has any other '
                               'form, then the traversal scripts take the value, append '
                               'the name of the window to it (with a separator space), '
                               'and evaluate the resulting string as a Tcl script. The '
                               'script must return 0, 1, or an empty string: a 0 or 1 value '
                               'specifies whether the window will receive the input focus, '
                               'and an empty string results in the default decision '
                               'described above. Note: this interpretation of the option '
                               'is defined entirely by the Tcl scripts that implement '
                               'traversal: the widget implementations ignore the option '
                               'entirely, so you can change its meaning if you redefine the '
                               'keyboard traversal scripts.',
                'valid_for': [
                    'Misc.tk_focusNext', 'Toplevel', 'Button', 'Checkbutton', 'Checkbutton',
                    'Frame', 'Label', 'Listbox', 'Menu', 'Radiobutton', 'Scale', 'Scrollbar',
                    'Text', 'Spinbox', 'LabelFrame'
                ],
                'value_type': '1 or 0'
            },
            'text': {
                'command_line': '-text',
                'database_class': 'Text',
                'description': 'Specifies a string to be displayed inside the widget. The way '
                               'in which the string is displayed depends on the particular '
                               'widget and may be determined by other options, such as anchor '
                               'or justify.',
                'valid_for': [
                    'Button', 'Canvas.create_text', 'Canvas.dchars', 'Checkbutton', 'Entry',
                    'Entry.delete', 'Entry.get', 'Label', 'Message', 'Radiobutton', 'Text.dump',
                    'Text.get', 'LabelFrame'

                ],
                'value_type': 'str'
            },
            'textvariable': {
                'command_line': '-textvariable',
                'database_class': 'Variable',
                'description': 'Specifies the name of a global variable. The value of the '
                               'variable is a text string to be displayed inside the widget; '
                               'if the variable value changes then the widget will '
                               'automatically update itself to reflect the new value. The '
                               'way in which the string is displayed in the widget depends '
                               'on the particular widget and may be determined by other '
                               'options, such as anchor or justify.',
                'valid_for': [
                    'Button', 'Checkbutton', 'Entry', 'Label', 'Radiobutton', 'OptionMenu',
                    'Spinbox'
                ],
                'value_type': 'tkinter variable, StringVar'
            },
            'troughcolor': {
                'command_line': '-troughcolor',
                'database_class': 'Background',
                'description': 'Specifies the color to use for the rectangular trough areas '
                               'in widgets such as scrollbars and scales. This option is '
                               'ignored for scrollbars on Windows (native widget doesn''t '
                               'recognize this option).',
                'valid_for': [
                    'Misc.tk_setPalette', 'Scale', 'Scrollbar'
                ],
                'value_type': 'color'
            },
            'underline': {
                'command_line': '-underline',
                'database_class': 'Underline',
                'description': 'Specifies the integer index of a character to underline in '
                               'the widget. This option is used by the default bindings to '
                               'implement keyboard traversal for menu buttons and menu '
                               'entries. 0 corresponds to the first character of the text '
                               'displayed in the widget, 1 to the next character, and so on.',
                'valid_for': [
                    'Button', 'Checkbutton', 'Label', 'Radiobutton'
                ],
                'value_type': 'int - index of char'
            },
            'wraplength': {
                'command_line': '-wraplength',
                'database_class': 'WrapLength',
                'description': 'For widgets that can perform word-wrapping, this option '
                               'specifies the maximum line length. Lines that would exceed '
                               'this length are wrapped onto the next line, so that no '
                               'line is longer than the specified length. The value may '
                               'be specified in any of the standard forms for screen '
                               'distances. If this value is less than or equal to 0 then '
                               'no wrapping is done: lines will break only at newline '
                               'characters in the text.',
                'valid_for': [
                    'Button', 'Checkbutton', 'Label', 'Radiobutton'
                ],
                'value_type': 'int'
            },
            'xscrollcommand': {
                'command_line': '-xscrollcommand',
                'database_class': 'ScrollCommand',
                'description': 'Specifies the prefix for a command used to communicate with '
                               'horizontal scrollbars. When the view in the widget''s window '
                               'changes (or whenever anything else occurs that could change '
                               'the display in a scrollbar, such as a change in the total '
                               'size of the widget''s contents), the widget will generate a '
                               'Tcl command by concatenating the scroll command and two '
                               'numbers. Each of the numbers is a fraction between 0 and 1, '
                               'which indicates a position in the document. 0 indicates the '
                               'beginning of the document, 1 indicates the end, .333 '
                               'indicates a position one third the way through the '
                               'document, and so on. The first fraction indicates the '
                               'first information in the document that is visible in the '
                               'window, and the second fraction indicates the information '
                               'just after the last portion that is visible. The command '
                               'is then passed to the Tcl interpreter for execution. '
                               'Typically the xScrollCommand option consists of the path '
                               'name of a scrollbar widget followed by ``set'', e.g. '
                               '``.x.scrollbar set'': this will cause the scrollbar to be '
                               'updated whenever the view in the window changes. If this '
                               'option is not specified, then no command will be executed.',
                'valid_for': [
                    'Canvas', 'Entry', 'Listbox', 'Text', 'Spinbox'
                ],
                'value_type': 'fraction between 0 and 1 see desc'
            },
            'yscrollcommand': {
                'command_line': '-yscrollcommand',
                'database_class': 'ScrollCommand',
                'description': 'Specifies the prefix for a command used to communicate with '
                               'vertical scrollbars. This option is treated in the same way '
                               'as the xScrollCommand option, except that it is used for '
                               'vertical scrollbars and is provided by widgets that '
                               'support vertical scrolling. See the description of '
                               'xScrollCommand for details on how this option is used.',
                'valid_for': [
                    'Canvas', 'Listbox', 'Text', 'Spinbox'
                ],
                'value_type': 'fraction between 0 and 1'
            }
        }

        with open("tkinterCommandArgumnts.json", "w") as f:
            j = json.dumps(self.commands)
            f.write(j)


if __name__ == '__main__':
    MakeTkArgsDb()
