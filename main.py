import flet as ft


def main(page: ft.Page):
    page.title = 'Instagram Profile'
    page.bgcolor = '#FFFFFF'
    page.scroll = ft.ScrollMode.HIDDEN
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_title_bar_hidden = False

    def follow(e):
        e.control.content.value = 'Seguindo'
        e.control.content.color = ft.colors.BLACK
        e.control.bgcolor = ft.colors.GREY_300
        e.control.update()

    header = ft.Container(
        padding=ft.padding.all(20),
        content=ft.ResponsiveRow(
            controls=[
                ft.Container(
                    col={'xs': 12, 'sm': 4},
                    padding=40,
                    bgcolor='#222b30',
                    shape=ft.BoxShape.CIRCLE,
                    height=200,
                    content=ft.Image(
                        src='images/logo2.png',
                        fit=ft.ImageFit.CONTAIN,
                    )
                ),
                ft.Container(
                    col={'xs': 12, 'sm': 8},

                    content=ft.ResponsiveRow(
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        run_spacing=20,
                        controls=[
                            ft.Row(
                                col=11,
                                controls=[
                                    ft.Text(
                                        value='python_brasil',
                                        size=24,
                                        color=ft.colors.BLACK,
                                    ),
                                    ft.Icon(
                                        name=ft.icons.VERIFIED,
                                        color=ft.colors.BLUE_500,
                                        size=20,
                                    )
                                ]
                            ),
                            ft.Icon(
                                col=1,
                                name=ft.icons.MORE_HORIZ,
                                color=ft.colors.BLACK,
                                size=20,
                            ),
                            ft.Container(
                                col=4,
                                bgcolor=ft.colors.BLUE_500,
                                content=ft.Text(
                                    value='Seguir',
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.colors.WHITE,
                                ),
                                border_radius=ft.border_radius.all(10),
                                padding=ft.padding.symmetric(vertical=5, horizontal=10),
                                alignment=ft.alignment.center,
                                on_click=follow,
                            ),
                            ft.Container(
                                col=6,
                                bgcolor=ft.colors.GREY_300,
                                content=ft.Text(
                                    value='Enviar mensagem',
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.colors.BLACK,
                                    max_lines=1,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                ),
                                border_radius=ft.border_radius.all(10),
                                padding=ft.padding.symmetric(vertical=5, horizontal=10),
                                alignment=ft.alignment.center,
                            ),
                            ft.Text(
                                col={'xs': 12, 'sm': 4},
                                spans=[
                                    ft.TextSpan(
                                        text='1064',
                                        style=ft.TextStyle(
                                            color=ft.colors.BLACK,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ),
                                    ft.TextSpan(
                                        text=' publicações',
                                        style=ft.TextStyle(
                                            color=ft.colors.BLACK,
                                        )
                                    )
                                ]
                            ),
                            ft.Text(
                                col={'xs': 12, 'sm': 4},
                                spans=[
                                    ft.TextSpan(
                                        text='12,2 ',
                                        style=ft.TextStyle(
                                            color=ft.colors.BLACK,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ),
                                    ft.TextSpan(
                                        text='mil',
                                        style=ft.TextStyle(
                                            color=ft.colors.BLACK,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ),
                                    ft.TextSpan(
                                        text=' publicações',
                                        style=ft.TextStyle(
                                            color=ft.colors.BLACK,
                                        )
                                    )
                                ]
                            ),
                            ft.Text(
                                col={'xs': 12, 'sm': 4},
                                spans=[
                                    ft.TextSpan(
                                        text='463',
                                        style=ft.TextStyle(
                                            color=ft.colors.BLACK,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ),
                                    ft.TextSpan(
                                        text=' publicações',
                                        style=ft.TextStyle(
                                            color=ft.colors.BLACK,
                                        )
                                    )
                                ]
                            ),
                            ft.Text(
                                col=12,
                                value='A MELHOR COMUNIDADE DE PYTHON DO BRASIL',
                                weight=ft.FontWeight.W_400,
                                color=ft.colors.BLACK,
                            ),

                            ft.Text(
                                col=12,
                                value='python_brasil',
                                color=ft.colors.BLACK,
                            ),
                            ft.Text(
                                col=12,
                                value='Comunidade',
                                color=ft.colors.GREY_500,
                            ),
                            ft.Text(
                                col=12,
                                color=ft.colors.BLACK,
                                spans=[
                                    ft.TextSpan(
                                        text='🐍| Python Brasil \n'
                                    ),
                                    ft.TextSpan(
                                        text='👨‍💻| Entre para a comunidade mais unida de Devs \n'
                                    ),
                                    ft.TextSpan(
                                        text='🍷| Conteúdos exclusivos no Discord da comunidade \n'
                                    ),
                                    ft.Icon(
                                        name=ft.icons.LINK,
                                        color=ft.colors.BLACK,
                                        size=20,
                                    ),
                                    ft.TextSpan(
                                        text='linktr.ee/python_brasil_links\n',
                                        url='https://linktr.ee/python_brasil_links',
                                        style=ft.TextStyle(
                                            color='#00379b',
                                        )
                                    ),
                                ]
                            ),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(
                                        text='Seguido(a) por ',
                                        style=ft.TextStyle(
                                            color=ft.colors.GREY_700,
                                        ),
                                    ),
                                    ft.TextSpan(
                                        text='usandopython, ',
                                        style=ft.TextStyle(
                                            color=ft.colors.BLACK,
                                            weight=ft.FontWeight.W_600,
                                        )
                                    ),
                                    ft.TextSpan(
                                        text='oficinapython, ',
                                        style=ft.TextStyle(
                                            color=ft.colors.BLACK,
                                            weight=ft.FontWeight.W_600,
                                        )
                                    ),
                                    ft.TextSpan(
                                        text='data.sciencebr',
                                        style=ft.TextStyle(
                                            color=ft.colors.BLACK,
                                            weight=ft.FontWeight.W_600,
                                        )
                                    ),
                                    ft.TextSpan(
                                        text=' e outras 11 pessoas',
                                        style=ft.TextStyle(
                                            color=ft.colors.GREY_700,
                                        ),
                                    ),
                                ],
                                size=14,
                            )

                        ]
                    )
                )
            ]
        )
    )

    stories = ft.Container(
        padding=ft.padding.all(20),
        content=ft.Row(
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                ft.Image(
                    src=f'https://picsum.photos/150/150?{num}',
                    border_radius=ft.border_radius.all(100),
                    width=100,
                ) for num in range(20)
            ]
        )
    )
    grid = ft.GridView(
        runs_count=3,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
        controls=[
            ft.Image(
                src=f'https://picsum.photos/300/300?{num}',
                fit=ft.ImageFit.COVER,
                width=100,
            ) for num in range(15)
        ]
    )

    grid_reels = ft.GridView(
        runs_count=3,
        child_aspect_ratio=9 / 16,
        spacing=5,
        run_spacing=5,
        controls=[
            ft.Image(
                src=f'https://picsum.photos/600/600?{num}',
                fit=ft.ImageFit.COVER,
                width=100,
            ) for num in range(15)
        ]
    )

    posts = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        label_color=ft.colors.BLACK,
        indicator_color=ft.colors.WHITE,
        divider_color=ft.colors.WHITE,
        unselected_label_color=ft.colors.GREY_500,
        scrollable=False,
        tabs=[
            ft.Tab(
                icon=ft.icons.GRID_ON,
                text='PUBLICAÇÕES',
                content=grid,
            ),
            ft.Tab(
                icon=ft.icons.VIDEO_COLLECTION_OUTLINED,
                text='REELS',
                content=grid_reels,

            ),
            ft.Tab(
                icon=ft.icons.BOOKMARK_BORDER,
                text='SALVOS',
                content=grid,

            )
        ]
    )

    layout = ft.Container(
        height=900,
        content=ft.Column(
            spacing=0,
            controls=[
                header,
                stories,
                ft.Divider(color=ft.colors.GREY, opacity=0.4),
                posts,
            ]
        )
    )
    page.add(layout)


ft.app(target=main, assets_dir='assets')
