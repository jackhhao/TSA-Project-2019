from win10toast import ToastNotifier

toaster = ToastNotifier()

toaster.show_toast("Stock Bot", "Buy stock {stock} right now!".format(stock = "AAPL"), duration = 5)
