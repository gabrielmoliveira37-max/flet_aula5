import flet as ft

def main(page: ft.Page):
    mensagem = ft.Text("Que personagem é esse? 🤪", size=20)
    resposta_correta = "Sonic"

    def verificar_resposta(e):
        if e.control.content == resposta_correta:
            mensagem.value = "Boaaaa, acertou em cheio 😒"
        else:
            mensagem.value = "Errouuu 🤣"
        page.update()

    page.title = "Game: Adivinhe a imagem"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#0A2775"

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "Adivinhe o personagem 🫣",
                    size=24,
                    weight="bold"
                ),
                ft.Image(
                    src="images/sonic.png",
                    height=200,
                    border_radius=69
                ),
                ft.Row(
                    controls=[
                        ft.Button(
                            content="Flash",
                            on_click=verificar_resposta,
                            color = "#000000",
                            bgcolor = "#43d1ed"
                        ),
                        ft.Button(
                            content="Sonic",
                            on_click=verificar_resposta,
                            color = "#000000",
                            bgcolor = "#43d1ed"
                        ),
                        ft.Button(
                            content="Ouriço Azul",
                            on_click=verificar_resposta,
                            color = "#000000",
                            bgcolor = "#43d1ed"
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                mensagem
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.run(main)