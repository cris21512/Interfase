import reflex as rx
from Interfase.components.icons_link import link_icons



def middle_part() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Visit your dream places",
                weight="bold",
                size="6",
                style={
                    "margin_left": "6.3em",
                }
            ),
            rx.text(
                "¡With our travel guide you can travel to your favorite places easily!",
                size="3",
                style={
                    "margin_left": "3.5em"
                }
            ),
            rx.hstack(
                link_icons(
                    "plane",
                    "Check flight schedules, the best routes, and tips for getting cheaper tickets."
                ),
                link_icons(
                    "map-pinned",
                    "Explore the most popular destinations around the world. Find itineraries, points of interest, and local guides."
                ),
                link_icons(
                    "luggage",
                    "Discover the best packing tips, what to bring, and how to prepare for your next adventure."
                )
            )
        ),
        class_name="green_section"
    )
