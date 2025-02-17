import flet as ft

def main (page: ft.Page):
    page.window_width= 1000
    page.window_height= 600
    page.bgcolor = '#8A2BE2'
    page.theme_mode = ft.Theme(color_scheme_seed=ft.colors.GREEN)
    page.window_center()
    page.horizontal_alignment ='start'


    c1 = ft.Row([
                    
                    
        ft.Container(
            
            bgcolor= '#E0FFFF', 
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
                                    color='#000000',
                                    prefix_icon=ft.icons.ACCOUNT_BOX),

                            


                            ft.TextField(
                                    label="Senha",
                                    hint_text="Digite sua Senha",
                                    width=400,
                                    color= '#000000',
                                    prefix_icon=ft.icons.PASSWORD),])),

                        ft.FilledButton(text="Entrar",width= 200, height= 50, on_click= lambda e: entrar(e) ),

                        ft.TextButton(text="Esquecei minha Senha "),
                    
            ],spacing=50, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),

        ),

        ft.Container(
            
            
            width= 500,
            height=540,
            content= ft.Column([
                    
                        ft.Image(src=f"lancar.png", width=280, height = 280),
                        ft.Text("A melhor experiência de login\n" "que você ja teve na sua vida.", size = 18, color="#FFFFFF")

                ],spacing= 20,horizontal_alignment= ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER)
        )            
                    
    ])



    #cadastro

    cadastro = ft.Column([
        
        ft.Container(
        width= 1000,
        height=270,
        bgcolor= "#E0FFFF",
        padding= 50,
        border_radius= 10,
        content= ft.Column([
            
                            ft.Text(
                                    "Dados do Usuário:",
                                    size= 18,
                                    
                                    color='#000000',
                                    font_family= 'robotoslad',
                                    weight=ft.FontWeight.W_200,
                                    ),

                           


            ft.Row([

                            ft.TextField(label="Nome completo:",
                                        color= "black87",
                                        width=300,
                                        height=40,
                                        border_color= "0D0D0D",
                                        border_radius= 5),



                            ft.TextField(label="CPF:",
                                        color= "black87",
                                        width=150,
                                        height=40,
                                        border_color= "0D0D0D",
                                        border_radius= 5)


            ]),
                            
                            ft.TextField(label="Nome",
                                        color= "black87",
                                        width=300,
                                        height=40,
                                        border_color= "0D0D0D",
                                        border_radius= 5),


                            ft.FilledButton(text= "Salvar",
                                            width=100,
                                            height=50,
                                            
                                            ),
                                            
                            

        ], spacing= 20)

                            

        ),

        ft.Container(
            
                                            bgcolor= "#E0FFFF",
                                            width= 1000,
                                            height=260,
                                            border_radius= 10,
                                            padding=50,
                                            content= 
  


            ft.DataTable(
                        columns=[
                    ft.DataColumn(ft.Text("Primeiro Nome",color= "black87")),
                    ft.DataColumn(ft.Text("Último Nome",color= "black87")),
                    ft.DataColumn(ft.Text("Idade",color= "black87"), numeric=True),
                ],
                rows=[
                    ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("John",color= "black87")),
                        ft.DataCell(ft.Text("Smith",color= "black87")),
                        ft.DataCell(ft.Text("43",color= "black87")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Jack",color= "black87")),
                        ft.DataCell(ft.Text("Brown",color= "black87")),
                        ft.DataCell(ft.Text("19",color= "black87")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Alice",color= "black87")),
                        ft.DataCell(ft.Text("Wong",color= "black87")),
                        ft.DataCell(ft.Text("25",color= "black87")),
                    ],
                ),
            ],
        )

            
        
        )                
    ])
                                


    #Controles da Pagina

    def entrar(e: ft.ControlEvent):

        page.remove(c1)
        page.add(cadastro)

    


    page.add(c1)

ft.app(target = main)
