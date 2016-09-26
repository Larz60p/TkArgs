# TkArgs
## Find widgets for arguments/arguments for widgets

This program can find all attributes for any tkinter widget.
It can also find all widgets for a particular attribute.

Requires: json, Record.py (https://github.com/Larz60p/Python-Record-Structure)

**Here's what it can do:**

**Needed for all examples**
```
>>> targs = TkArgs(filename='tkinterCommandArgumnts.json')
>>> attrrec = targs.rec.record
```

**To find Attributes for a widget**
```
>>> print('Attributes for Button: {}'.format(targs.attributes_by_widget('Button')))
>>> Attributes for Button: ['repeatinterval', 'highlightbackground', 'bitmap', 'relief', 'text', 'textvariable', 'activeforeground', 'pady', 'wraplength', 'highlightthickness', 'foreground', 'activebackground', 'highlightcolor', 'underline', 'image', 'font', 'repeatdelay', 'disabledForeground', 'borderWidth', 'justify', 'cursor', 'compound', 'background', 'anchor', 'padx', 'takefocus']
```

**To find widgets that use an attribute**
```
>>> print('\nWidgets that use activeForeground: {}'.format(targs.widgets_by_attribute('activeForeground')))
>>> Widgets that use activeForeground: ['Misc.tk_setPalette', 'Button', 'Checkbutton', 'Label', 'Menu', 'Radiobutton']
```

**Get individual attribute records by name**
```
>>> print('\nRecord for setgrid: {}'.format(attrrec.setgrid))
>>> Record for setgrid: data(value_type='boolean', valid_for=['Listbox', 'Text'], command_line='-setgrid', description='Specifies a boolean value that determines whether this widget controls the resizing grid for its top-level window. This option is typically used in text widgets, where the information in the widget has a natural size (the size of a character) and it makes sense for the windows dimensions to be integral numbers of these units. These natural window sizes form a grid. If the setGrid option is set to true then the widget will communicate with the window manager so that when the user interactively resizes the top-level window that contains the widget, the dimensions of the window will be displayed to the user in grid units and the window size will be constrained to integral numbers of grid units. See the section GRIDDED GEOMETRY MANAGEMENT in the wm manual entry for more details.', database_class='SetGrid')
```

**Reference record element by name**
```
>>> print('\nunderline description: {}'.format(attrrec.underline.description))
>>> underline description: Specifies the integer index of a character to underline in the widget. This option is used by the default bindings to implement keyboard traversal for menu buttons and menu entries. 0 corresponds to the first character of the text displayed in the widget, 1 to the next character, and so on.
```

**To get record keys**
```
>>> print('\nkeys: {}'.format(targs.get_keys()))
>>> keys: ['text', 'insertwidth', 'pady', 'activebackground', 'foreground', 'textvariable', 'insertofftime', 'highlightcolor', 'padx', 'repeatinterval', 'underline', 'background', 'orient', 'insertborderWidth', 'selectbackground', 'selectborderWidth', 'bitmap', 'repeatdelay', 'exportselection', 'takefocus', 'font', 'activeforeground', 'yscrollcommand', 'borderWidth', 'disabledForeground', 'insertontime', 'highlightthickness', 'anchor', 'compound', 'wraplength', 'troughcolor', 'justify', 'highlightbackground', 'selectforeground', 'jump', 'setgrid', 'image', 'xscrollcommand', 'cursor', 'relief', 'insertbackground']
```

