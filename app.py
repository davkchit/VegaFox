import asyncio
import flet as ft
import sqlite3

async def main(page: ft.Page) -> None:
    page.title = "Moy Click"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0F1525"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    async def score_up(event: ft.ContainerTapEvent) -> None:
        if hasattr(event, 'control'):
            score.data += 1
            score.value = str(score.data)

            image.scale = 0.90

            score_counter.opacity = 50
            score_counter.value = "+1"
            # Assuming you want to position the score_counter at a fixed point
            score_counter.right = 0
            score_counter.left = tap_position[0]
            score_counter.top = tap_position[1]
            score_counter.bottom = 0   # Adjust as needed

            progress_bar.value += (1 / 100)
            if score.data % 100 == 0:
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(
                        value="+100 🦊",
                        size=20,
                        color="#ffffff",
                        text_align=ft.TextAlign.CENTER
                    ), 
                    bgcolor="#13AEEE"
                )
                page.snack_bar.open = True
                progress_bar.value = 0

            page.update()
            await asyncio.sleep(0.1)
            image.scale = 1
            score_counter.opacity = 0
            page.update()

    

    score = ft.Text(value="0", size=100, data=0)
    score_counter = ft.Text(size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN))

    image = ft.Image(
    src="https://sun9-20.userapi.com/impf/JXoS6QxtrYeUJi2C2T3dH5ojvgc2dTc_BD-xKQ/GycEtXCVeWU.jpg?quality=96&as=32x32,48x49,72x73,108x109,160x162,240x243,360x365,480x486,518x525&sign=ee5a148577c2387e336376356cc5cef7&from=bu&u=T5yR26rxY83XmGKkMxBtbeVcLj0AtG40mhzsLy1YaRM&cs=518x525",
    fit=ft.ImageFit.CONTAIN, 
    animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE),
    border_radius=ft.border_radius.all(90)#НЕ РАБОТАЕТ ПОЧЕМУ-ТО
    )

    progress_bar = ft.ProgressBar(
        value=0,
        width=page.width - 100,
        bar_height=20,
        color="#ffffff",
        bgcolor="#1483B0"
    )

    def on_tap_down(event: ft.ContainerTapEvent):
        global tap_position
        tap_position = (event.local_x, event.local_y)

    page.add(
        score,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            on_click=score_up,
            on_tap_down=on_tap_down,
            margin=ft.Margin(0, 0, 0, 30)
        ),
        ft.Container(
            content=progress_bar,
            border_radius=ft.BorderRadius(10, 10, 10, 10)
        )
    )

if __name__ == "__main__":
    tap_position = (0, 0)
    ft.app(target=main, view=ft.WEB_BROWSER)
