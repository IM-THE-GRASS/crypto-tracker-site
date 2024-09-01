import reflex as rx
import requests
from reflex_motion import motion

class State(rx.State):
    name = "Bitcoin"
    rank = "#1"
    symbol = "BTC"
    usd_value = 59083.73
    current_input:str
    data:list
    coin_index:int = 1
    @rx.var()
    def result(self):
        try:
            return str(round(float(self.current_input) * self.usd_value)) + " USD"
        except:
            return "0 USD"
    def get_coin_info(self):
        coin = self.data[self.coin_index]
        self.name = coin["name"]
        self.symbol = coin["symbol"]
        self.usd_value = float(coin["price_usd"])
        self.rank = "#" + str(coin["rank"])
    def on_load(self):
        response = requests.get("https://api.coinlore.net/api/tickers/")
        data = response.json()["data"]
        self.data = data
        self.get_coin_info()
        
    def next(self):
        self.coin_index = (self.coin_index + 1) % len(self.data)
        self.get_coin_info()
    def back(self):
        self.coin_index = (self.coin_index - 1) % len(self.data)
        self.get_coin_info()
    def on_change(self, new):
        self.current_input = new

@rx.page(on_load=State.on_load)
def index() -> rx.Component:
    return rx.container(
        rx.center(
            rx.hstack(
                rx.text(
                    State.name,
                    font_weight="900",
                    font_size="256px",
                    letter_spacing="-7.6px",
                    height="225px",
                    line_height="256px",
                    text_wrap="nowrap"
                ),
                rx.center(
                    rx.text(
                        State.rank,
                        font_size="96px",
                        color="#C7C7C7",
                        line_height="96px"
                    ),
                    height="225px",
                ),
                height="225px",
            ),
            position="absolute",
            width="100vw",
            height="225px",
            left="0px",
            top="50px"
        ),
        rx.center(
            rx.vstack(
                rx.input(
                    rx.center(
                        rx.text(
                            State.symbol,
                            font_weight="bold",
                            font_size="64px"
                        ),
                        width="181px",
                        height="90px"
                    ),
                    placeholder="1",
                    width="755px",
                    height="98px",
                    border = "1px solid #626262",
                    font_size="48px",
                    
                    value=State.current_input,
                    on_change=State.on_change
                    
                ),
                rx.center(
                    rx.image(
                        src="/=.png"
                    ),
                    width="755px"
                ),
                rx.center(
                    rx.text(
                        State.result,
                        height="113px",
                        font_size="128px",
                        line_height="80px",
                        margin_right="60px",
                        text_wrap="nowrap",
                        font_weight="bolder"
                    ),
                    width="755px"
                ),
                spacing="0",
                gap = "55px"  
            ),
            position="absolute",
            width="100vw",
            height="429px",
            left="0px",
            top="364px"
        ),
        motion(
            rx.image(
                src="/arrow_back.png",
                on_click=State.back
            ),
            position="absolute",
            left="0px",
            top="287px",
            while_hover={"scale": 1.2},
            while_tap={"scale": 0.9},
            transition={"type": "spring", "stiffness": 400, "damping": 17},
        ),
        motion(
            rx.image(
                src="/arrow_forward.png",
                on_click= State.next
            ),
            position="absolute",
            left="1909px",
            top="287px",
            while_hover={"scale": 1.2},
            while_tap={"scale": 0.9},
            transition={"type": "spring", "stiffness": 400, "damping": 17},
        ),
        overflow="hidden"
    )


app = rx.App()
app.add_page(index)
