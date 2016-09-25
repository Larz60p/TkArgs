# TkArgs
## Find widgets for arguments/arguments for widgets

This program can find all attributes for any tkinter widget.
It can also find all widgets for a particular widget.

**To find Attributes for a widget**
```

>>> targs = TkArgs(filename='tkinterCommandArgumnts.json')
>>> attrrec = targs.rec.record
>>> print('Attributes for Button: {}'.format(targs.attributes_by_widget('Button')))
```

** Results in**
```

```
