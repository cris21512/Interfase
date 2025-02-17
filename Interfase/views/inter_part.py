import reflex as rx



def inter_part() -> rx.Component:
    return rx.box(
        rx.text(
            "Welcome the InterPhase",
            style={
                "font_family": "Roboto Medium 500 Italic",
                "font_size": "2em",
                "color": "#D2B48C",
                "text-shadow": "4px 4px 6px #020202"
            },
        ),
        rx.text(
            "Discover your right place to travel",
            style={
                "font:family": "Kanit",
                "font_size": "0.65em",
            }
        ),
        rx.button(
            "Learn More",
            style={
                "background_color": "transparent",
                "border": "1px solid white",
                "_hover": {
                    "background_color": "#BBA9BB",
                }
            }
        ),
        class_name="hero"
    )
