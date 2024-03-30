class Pratyush:
    def __init__(self):
        self.price_table = dict()
        self.worst_trade_table = dict()

    def process_trade(self, trade_id, instrument_id, buy_sell, price, volume):
        pnl = (price - self.price_table[instrument_id]) * volume
        if instrument_id not in self.worst_trade_table:
            self.worst_trade_table[instrument_id] = (
                trade_id,
                buy_sell,
                price,
                volume,
                pnl,
            )
        else:
            if self.worst_trade_table[instrument_id][4] <= pnl:
                self.worst_trade_table[instrument_id] = (
                    trade_id,
                    buy_sell,
                    price,
                    volume,
                    pnl,
                )

    def process_price_update(self, instrument_id, price):
        self.price_table[instrument_id] = price

    def output_worst_trade(self, instrument_id):
        if instrument_id in self.worst_trade_table:
            return self.worst_trade_table[instrument_id]
        else:
            return "NO BAD TRADES"

    # def run(self):
    #     pass
