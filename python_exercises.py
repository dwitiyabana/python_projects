#practice for *args and **kwargs
def shiping_label(**kwargs):
    for keys,values in kwargs.items():
        print(f"{keys} {values}")
shiping_label(name="dwitiya",
              mobile="8745486451",
              area="ghaziabad")