import reflex as rx



def card_buttom(image: str, title: str , body: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.image(
                src=image,
                width="20em",
                height="7em",
                margin="1em",
                alt=title
            ),
            rx.text(
                title,
                size="5",
                weight="bold"
            ),
            rx.text(
                body,
                size="3",
                weight="medium"
            )
        ),
        width="100%",
        aligm_items="center",
    )
