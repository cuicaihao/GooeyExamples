import wx
import requests
import json
import webbrowser


class AppWindow(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='/r/programming', size=(650, 400))
        self.items = []
        self.panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.table = wx.ListCtrl(self, size=(-1, 400),
                                 style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.row_clicked, self.table)
        self.build_table()
        sizer.Add(self.table, 0, wx.EXPAND)

        self.SetSizer(sizer)
        self.menu_bar = wx.MenuBar()
        self.SetMenuBar(self.menu_bar)
        self.Show()

    def build_table(self):
        self.table.InsertColumn(0, 'Title', width=400)
        self.table.InsertColumn(1, 'User', width=100)
        self.table.InsertColumn(2, 'Comments', width=100)

        response = requests.get(
            'https://www.reddit.com/r/programming.json',
            headers={'User-agent': 'Fancy Reddit GUI 1.0'}
        ).text
        data = json.loads(response)

        i = 0
        for item in data['data']['children']:
            self.items.append(item['data'])
            self.table.InsertItem(i, item['data']['title'])
            self.table.SetItem(i, 1, item['data']['author'])
            self.table.SetItem(i, 2, str(item['data']['num_comments']))
            i += 1

    def row_clicked(self, event):
        row = event.GetIndex()
        item = self.items[row]
        url = item['url']
        webbrowser.open_new_tab(url)


if __name__ == '__main__':
    app = wx.App(False)
    window = AppWindow()
    app.MainLoop()
