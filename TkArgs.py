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
import Record


class TkArgs(object):
    def __init__(self, filename=None):
        if filename:
            self.rec = Record.Record(filename)

    def get_keys(self):
        return self.rec.record._asdict().keys()

    def get_rec(self, key):
        recc = getattr(self.rec.record, key)
        return recc

    def widgets_by_attribute(self, attribute):
        nattr = attribute.lower()
        record = getattr(self.rec.record, nattr)
        if record is not None:
            return record.valid_for
        return None

    def attributes_by_widget(self, widgetname):
        atriblist = []
        wn = widgetname.title()
        keys = self.get_keys()
        for key in keys:
            atribrec = getattr(self.rec.record, key)
            if wn in atribrec.valid_for:
                atriblist.append(key)
        return atriblist


if __name__ == '__main__':
    targs = TkArgs(filename='tkinterCommandArgumnts.json')
    attrrec = targs.rec.record

    print('Attributes for Button: {}'.format(targs.attributes_by_widget('Button')))

    print('\nWidgets that use activeForeground: {}'.format(targs.widgets_by_attribute('activeForeground')))

    print('\nkeys: {}'.format(targs.get_keys()))

    # Get individual attribute records by name
    print('\nRecord for setgrid: {}'.format(attrrec.setgrid))

    # Reference record elements by name as well
    print('\nunderline description: {}'.format(attrrec.underline.description))
