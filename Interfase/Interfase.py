import reflex as rx
import Interfase.styles.styles as styles
from Interfase.header.header import header
from Interfase.views.inter_part import inter_part
from Interfase.views.green_part import middle_part
from Interfase.views.info_part import places_info



def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            inter_part(),
            middle_part(),
            places_info(),
            #header(),
        )
    )


app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
