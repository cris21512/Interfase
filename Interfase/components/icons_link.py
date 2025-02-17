import reflex as rx


def link_icons(icon: str, text: str) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(
                icon,
                stroke_width="2",
                size=20
            ),
            style={
                "color": "white",
                "border": "2px inset white",
                "border_radius": "10px",
                "padding": "10px",
                "background_color": "rgba(0, 0, 0, 0.3)",
                "transition": "0.3s",
                "_hover": {
                    "transform": "scale(1.1)",
                }
            },
            spacing="5"
        ),
        rx.text(
            text,
            style={
                "color": "white",
                "font:family": "Kanit",
                "font_size": "0.65em",
            },
        ),
        style={
            "max_width": "12em",
            "align_items": "center",
        }
    )
