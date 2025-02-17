import reflex as rx
import Interfase.styles.styles as styles



def header() -> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.center(
                rx.text(
                    "InterFase",
                    style=styles.text_body_style
                ),
            ),
            rx.spacer(),
            rx.center(
                rx.text(
                    "Home",
                    style=styles.text_body_style
                ),
            ),
            rx.spacer(),
            rx.center(
                rx.text(
                    "About",
                    style=styles.text_body_style
                )
            ),
        ),
        spacing="9",
        width="100%"
    )