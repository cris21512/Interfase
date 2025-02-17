import reflex as rx
import enum as Enum





BASE_STYLE = {
    "body": {
        "margin": "0",
        "padding": "0",
    },
    ".hero": { 
        "width": "2000px",
        "height": "320px",
        "background_image": "url('https://wallpapercrafter.com/sizes/2048x1152/7478-road-winding-rock-coast-nature-4k.jpg')",
        "background_position": "center",
        "background_repeat": "no_repeat",
        "display": "flex",
        "flex_direction": "column",
        "align_items": "center",
        "justify_content": "center",
        "color": "white",
        "transition": "opacity 2s, width 1s, height 1s",
        "@starting-style": {
            "opacity": 0,
        }
    },
    ".green_section": {
        "width": "100%",
        "height": "200px",
        "background_color": "#6DC36D",
        "text_align": "center",
        "align_items": "center",
        "justify_content": "center",
        "padding_left": "45em"
    },
    ".white_section": {
        "width": "100%",
        "height": "280px",
        "background_color": "white",
        "padding": "1.5em ",
        "text_align": "center",
    },
    rx.card: {
        "width": "100%",
        "height": "100%",
        "padding": "0.6em",
        "display": "block",
        "color": "#8c8c8c",
        "background_color": "transparent",
        "transition": "0.3s",
        "_hover": {
            "color": "white",
            "transform": "scale(1.1)",
            "background": "#23BAC4"
        }
    }
}

text_body_style = {
    "font_family": "Inter",
    "font_size": "2em",
    "color": "#C3B091"
}

text_title_style = {
    "font_family": "Roboto Medium 500 Italic",
    "font_size": "2em",
    "color": "#D2B48C",
    "text-shadow": "4px 4px 6px #020202"
}


