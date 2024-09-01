"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.center(
            rx.hstack(
                rx.text(
                    "Bitcoin",
                    font_weight="900",
                    font_size="256px",
                    letter_spacing="-7.6px",
                    height="225px",
                    line_height="256px"
                ),
                rx.center(
                    rx.text(
                        "#1",
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
            top="25px"
        ),
        rx.center(
            rx.vstack(
                rx.input(
                    rx.center(
                        rx.text(
                            "BTC",
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
                    font_size="48px"
                    
                ),
                rx.text(
                    "=",
                    font_size="256px",
                    line_height="24px"
                ),
                spacing="0",
                gap = "55px"  
            ),
            position="absolute",
            width="100vw",
            height="429px",
            left="0px",
            top="309px"
        )
    )


app = rx.App()
app.add_page(index)
