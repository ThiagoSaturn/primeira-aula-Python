import flet as ft

def main (page: ft.Page):
    page.window_width= 1000
    page.window_height= 600
    page.bgcolor = '#99B4BF'
    page.window_center()
    page.horizontal_alignment ='start'


    c1 = ft.Row([
                    
                    
        ft.Container(
            
            bgcolor= '#FFFFFF', 
            width= 450, 
            height=540, 
            border_radius= 10,
            content = ft.Column([

                       ft.Text("Faça seu Login", size = 40, color="black87"),
                        

                        ft.Container( content= ft.Column([

                            ft.TextField(
                                    label="E-Mail",
                                    hint_text="Digite seu E-Mail",
                                    width=400,
                                    prefix_icon=ft.icons.ACCOUNT_BOX),

                            ft.TextField(
                                    label="Senha",
                                    hint_text="Digite sua Senha",
                                    width=400,
                                    prefix_icon=ft.icons.PASSWORD),])),

                        ft.FilledButton(text="Entrar", on_click=True)
                    
            ],spacing=50, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),

        ),

        ft.Container(
            
            
            width= 500,
            height=540,
            content= ft.Column([
                    
                        ft.Image(src=f"lancar.png", width=280, height = 280),
                        ft.Text("A melhor experiência de login\n" "que você ja teve na sua vida.", size = 18, color="black87")

                ],spacing= 20,horizontal_alignment= ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER)
        )            
                    
    ])
    


    page.add(c1)

ft.app(target = main)
