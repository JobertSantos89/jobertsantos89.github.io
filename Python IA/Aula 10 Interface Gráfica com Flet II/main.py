import db
import flet as ft


def main(page: ft.Page):
    tarefa_input = ft.TextField(label='Tarefa')
    data_inicio_input = ft.TextField(label='Data Inicio (dd/MM/YYYY)')
    data_limite_input = ft.TextField(label='Data Limite (dd/MM/YYYY)')

    list_view_tarefas = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text('Nome')),
            ft.DataColumn(ft.Text('Data Inicio')),
            ft.DataColumn(ft.Text('Data Limite')),
        ]
    )

    def listar_tarefas_view():
        tarefas = db.listar_tarefas()
        list_view_tarefas.rows.clear()

        for tarefa in tarefas:
            list_view_tarefas.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(tarefa.get('nome'))),
                        ft.DataCell(ft.Text(tarefa.get('data_inicio'))),
                        ft.DataCell(ft.Text(tarefa.get('data_limite'))),
                    ]
                )
            )

    def handle_salvar_tarefa(e):
        nova_tarefa = {
            'nome': tarefa_input.value,
            'data_inicio': data_inicio_input.value,
            'data_limite': data_limite_input.value,
        }

        db.cadastrar_tarefa(nova_tarefa)
        listar_tarefas_view()
        page.update()


    listar_tarefas_view()
    page.add(
        ft.Column([
            ft.Text('Tarefas', size=32),
            ft.Column([
                tarefa_input,
                data_inicio_input,
                data_limite_input,
                ft.Button(
                    'Salvar', 
                    bgcolor=ft.Colors.BLUE, 
                    width=500,
                    on_click=handle_salvar_tarefa
                )
            ]),
            list_view_tarefas
        ])
    )


ft.app(target=main)
