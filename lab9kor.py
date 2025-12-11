import tkinter as tk
from tkinter import messagebox
import random

class Minesweeper:
    def __init__(self, master):
        self.master = master
        self.master.title("Сапер (Lab 9)")
        
        # Настройки игры
        self.ROWS = 10
        self.COLS = 10
        self.MINES = 15
        
        # Цвета для цифр (как в оригинале)
        self.colors = {
            1: 'blue', 2: 'green', 3: 'red', 4: 'darkblue',
            5: 'darkred', 6: 'cyan', 7: 'black', 8: 'gray'
        }

        # Инициализация переменных
        self.game_over = False
        self.buttons = [] # Хранит объекты кнопок
        self.field = []   # Хранит логику (мины и цифры)
        self.flags = []   # Хранит координаты флагов

        # Создание интерфейса
        self._create_widgets()
        self.start_new_game()

    def _create_widgets(self):
        # Верхняя панель с кнопкой сброса
        self.top_frame = tk.Frame(self.master)
        self.top_frame.pack(side=tk.TOP, fill=tk.X, pady=5)
        
        self.btn_reset = tk.Button(self.top_frame, text="Новая игра", command=self.start_new_game)
        self.btn_reset.pack()

        # Основное поле (используем Frame для группировки)
        self.game_frame = tk.Frame(self.master)
        self.game_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

    def start_new_game(self):
        self.game_over = False
        self.flags = []
        
        # Очистка старых кнопок
        for widget in self.game_frame.winfo_children():
            widget.destroy()

        self.buttons = []
        self.field = []

        # Генерация мин
        mines_coords = set()
        while len(mines_coords) < self.MINES:
            r = random.randint(0, self.ROWS - 1)
            c = random.randint(0, self.COLS - 1)
            mines_coords.add((r, c))

        # Создание логического поля
        # 0 - пусто, -1 - мина, 1-8 - количество мин вокруг
        for r in range(self.ROWS):
            row_data = []
            row_buttons = []
            for c in range(self.COLS):
                # Логика: если координата в списке мин, ставим -1, иначе 0
                val = -1 if (r, c) in mines_coords else 0
                row_data.append(val)

                # Визуал: создаем кнопку
                btn = tk.Button(self.game_frame, width=3, height=1, font=('Arial', 10, 'bold'))
                
                # Привязываем события: ЛКМ и ПКМ
                # Используем lambda для передачи координат
                btn.bind('<Button-1>', lambda event, r=r, c=c: self.on_left_click(r, c))
                btn.bind('<Button-3>', lambda event, r=r, c=c: self.on_right_click(r, c))
                
                # Размещаем через grid
                btn.grid(row=r, column=c)
                row_buttons.append(btn)
            
            self.field.append(row_data)
            self.buttons.append(row_buttons)

        # Подсчет цифр вокруг мин
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if self.field[r][c] == -1:
                    continue
                # Считаем соседей
                count = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        nr, nc = r + i, c + j
                        if 0 <= nr < self.ROWS and 0 <= nc < self.COLS:
                            if self.field[nr][nc] == -1:
                                count += 1
                self.field[r][c] = count

    def on_left_click(self, r, c):
        if self.game_over or (r, c) in self.flags:
            return

        btn = self.buttons[r][c]
        val = self.field[r][c]

        if val == -1:
            # Нарвались на мину
            self.game_over = True
            btn.config(text="*", bg="red")
            self.show_all_mines()
            messagebox.showinfo("Game Over", "Вы проиграли! БУМ!")
        elif val == 0:
            # Пустая клетка - открываем соседей (рекурсивно)
            self.open_empty_cells(r, c)
        else:
            # Клетка с цифрой
            btn.config(text=str(val), fg=self.colors.get(val, 'black'), relief=tk.SUNKEN, bg="lightgrey")
            # Отключаем кнопку, чтобы нельзя было нажать снова
            btn.unbind('<Button-1>')
            btn.unbind('<Button-3>')

        self.check_win()

    def on_right_click(self, r, c):
        if self.game_over:
            return
        
        btn = self.buttons[r][c]
        # Проверяем, нажата ли уже кнопка (relief SUNKEN означает нажатую)
        if btn['relief'] == tk.SUNKEN:
            return

        if (r, c) in self.flags:
            self.flags.remove((r, c))
            btn.config(text="")
        else:
            self.flags.append((r, c))
            btn.config(text="F", fg="red")

    def open_empty_cells(self, r, c):
        # Алгоритм заливки (Flood Fill) для открытия пустых областей
        if not (0 <= r < self.ROWS and 0 <= c < self.COLS):
            return
        
        btn = self.buttons[r][c]
        if btn['relief'] == tk.SUNKEN: # Уже открыта
            return
        if (r, c) in self.flags: # Флаг не трогаем
            return

        val = self.field[r][c]
        btn.config(relief=tk.SUNKEN, bg="lightgrey")
        btn.unbind('<Button-1>')
        btn.unbind('<Button-3>')

        if val > 0:
            btn.config(text=str(val), fg=self.colors.get(val, 'black'))
        elif val == 0:
            # Рекурсивно открываем соседей
            for i in range(-1, 2):
                for j in range(-1, 2):
                    self.open_empty_cells(r + i, c + j)

    def show_all_mines(self):
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if self.field[r][c] == -1:
                    self.buttons[r][c].config(text="*", bg="red")

    def check_win(self):
        # Победа, если количество закрытых клеток == количеству мин
        closed_cells = 0
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if self.buttons[r][c]['relief'] != tk.SUNKEN:
                    closed_cells += 1
        
        if closed_cells == self.MINES:
            self.game_over = True
            messagebox.showinfo("Победа", "Поздравляем! Вы разминировали поле!")

if __name__ == "__main__":
    root = tk.Tk()
    game = Minesweeper(root)
    root.mainloop()