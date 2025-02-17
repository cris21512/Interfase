import reflex as rx
from Interfase.components.cards_link import card_buttom



def places_info() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.flex(
                card_buttom(
                    "https://www.pausa.com.ar/wp-content/uploads/2021/03/646452-scaled.jpg",
                    "Argentina",
                    "Discover the best places to visit in Argentina"
                ),
                card_buttom(
                    "https://th.bing.com/th/id/OIP.x7qkmEX0vDYRJfSGgBdzugHaDP?rs=1&pid=ImgDetMain",
                    "Mexico",
                    "Discover the best places to visit in Mexico",
                ),
                card_buttom(
                    "https://content.skyscnr.com/m/7558f8f14562fbe0/original/spain-aragon-teruel-plaza-del-torico-square-gettyimages-513409226.jpg?resize=1800px:1800px&quality=100",
                    "España",
                    "Discover the best places to visit in Spain",
                ),
            ),
            style={
            "margin_left": "30em",
            },
        ),
        spacing="3",
        class_name="white_section"
    )
