import reflex as rx


def navbar():
    return rx.box(
        rx.hstack(
                
            rx.link(
                rx.icon(tag="arrow_up"),
                'Inicio', 
            ),
            rx.link(),
            bg="light blue",
            padding="5px",
            z_index='999',
        )
    )