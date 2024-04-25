import random 
from Logica_LL import DoubleLinkedList

class Game():
    def __init__(self, n,game_difficulty) -> None:
        self.n = n
        self.matrix = DoubleLinkedList()
        self.alien_row = 0
        self.alien_col = 0
        self.alien_hp = 50
        self.predator_row = random.randint(0,n-1)
        self.predator_col = random.randint(0,n-1)
        self.predator_hp = 50
            
        for i in range(n):
            new_row = DoubleLinkedList()
            for j in range(n):
                if i != self.predator_row or j != self.predator_col:
                    new_row.append('O')
                else:
                    new_row.append("🤖")
            self.matrix.append(new_row)


        count_minus = round(n*game_difficulty/100) 
        count_plus = n-count_minus

        while count_minus != 0:
            x = random.randint(0,n-1)
            y = random.randint(0,n-1)
            
            row_node = self.matrix.get(x)
            value_node = row_node.value.get(y)

            if value_node.value == 'O':
                value_node.value = "-"
                count_minus -=1 

        while count_plus != 0:
            x = random.randint(0,n-1)
            y = random.randint(0,n-1)
            
            row_node = self.matrix.get(x)
            value_node = row_node.value.get(y)

            if value_node.value == "O":
                value_node.value = "+"
                count_plus -=1

    def print_matrix(self):
        print(f"Alien: {self.alien_hp} - Depredador: {self.predator_hp} ")
        print()
        for row in self.matrix:
            print("[",end="")
            for node in row.value:
                if node.next:
                    print(f"'{node.value}', ",end="")
                else:
                    print(f"'{node.value}']",end="")
            print()
        print()

    def choice_alien_position(self):
        self.print_matrix()
        while True:
            row = int(input("Ingrese el numero de la fila del alien: "))
            if row > 0 and row <= self.n:
                self.alien_row = row
                break
            else:
                print("Ingresaste una fila fuera del rango permitido. Intentalo de nuevo!")

        while True:
            col = int(input("Ingrese el numero de la columna del alien: "))
            if col > 0 and col <= self.n:
                self.alien_col = col
                break
            else:
                print("Ingresaste una columna fuera del rango permitido. Intentalo de nuevo!")

        self.insert_alien_move(row,col)

    def insert_alien_move(self,row,col):
        
        row -=1
        col -=1

        row_node = self.matrix.get(row)
        value_node = row_node.value.get(col)

        if value_node.value == "🤖":
            value_node.value = "🤖👽"
            self.alien_hp -= 25
        else:
            if value_node.value == "+":
                self.alien_hp += 10
            elif value_node.value == "-":
                self.alien_hp -=10
 
            value_node.value = "👽"

        row_node = self.matrix.get(self.alien_row)
        value_node = row_node.value.get(self.alien_col)

        if value_node != None:
            if value_node.value == "👽":
                value_node.value = "O"
            elif value_node.value == "🤖👽":
                value_node.value = "🤖"
        
        self.alien_row = row
        self.alien_col = col

        if row - 1 >= 0:
            if self.predator_row == row -1 and self.predator_col == col:
                self.predator_hp -= 25
        if col - 1 >= 0:
            if self.predator_row == row and self.predator_col == col-1:
                self.predator_hp -= 25
    
        if row + 1 < self.n:
            if self.predator_row == row +1 and self.predator_col == col:
                self.predator_hp -= 25
        if col + 1 < self.n:
            if self.predator_row == row and self.predator_col == col+1:
                self.predator_hp -= 25

    def insert_predator_move(self):
        old_row_node = self.matrix.get(self.predator_row)
        old_value_node = old_row_node.value.get(self.predator_col)
        
        while True:
            move = random.choice(["w","a","s","d"])
            if move == "a":
                if self.predator_col-1 >= 0:          
                    row_node = self.matrix.get(self.predator_row)
                    value_node = row_node.value.get(self.predator_col-1)

                    old_value_node.value = "O"
                    self.predator_row = self.predator_row
                    self.predator_col = self.predator_col-1
                    break
            if move == "w":
                if self.predator_row-1 >= 0:          
                    row_node = self.matrix.get(self.predator_row-1)
                    value_node = row_node.value.get(self.predator_col)

                    old_value_node.value = "O"
                    self.predator_row = self.predator_row-1
                    self.predator_col = self.predator_col
                    break
            if move == "d":
                if self.predator_col+1 < self.n:          
                    row_node = self.matrix.get(self.predator_row)
                    value_node = row_node.value.get(self.predator_col+1)

                    old_value_node.value = "O"
                    self.predator_row = self.predator_row
                    self.predator_col = self.predator_col+1   
                    break                
            if move == "s":
                if self.predator_row+1 < self.n:          
                    row_node = self.matrix.get(self.predator_row+1)
                    value_node = row_node.value.get(self.predator_col)

                    old_value_node.value = "O"
                    self.predator_row = self.predator_row+1
                    self.predator_col = self.predator_col
                    break

        row_node = self.matrix.get(self.predator_row)
        value_node = row_node.value.get(self.predator_col)

        if value_node.value ==  "👽":
            value_node.value = "🤖👽"
            self.alien_hp -= 25
        elif value_node.value == "+":
            value_node.value = "🤖"
            self.predator_hp +=10
        elif value_node.value == "-":
            value_node.value = "🤖"
            self.predator_hp -=10
        else:
            value_node.value = "🤖"


    def choice_alien_move(self):
        while True:
            move = input("Ingresa tu movimiento (w/a/s/d): ").lower()
            if move not in ["w", "a", "s", "d"]: 
                print("Movimiento invalido. Ingresa w, a, s, o d.")
                continue

            if move == "a":
                if self.alien_col-1 >= 0:          
                    return self.alien_row,self.alien_col-1
            if move == "w":
                if self.alien_row-1 >= 0:          
                    return self.alien_row-1,self.alien_col
            if move == "d":
                if self.alien_col+1 < self.n:          
                    return self.alien_row,self.alien_col+1              
            if move == "s":
                if self.alien_row+1 < self.n:          
                    return self.alien_row+1,self.alien_col      
            print("Movimiento invalido!")  

def main():
    while True:
        try:
            # Solicitar al usuario el tamaño de la matriz
            print("Elija el tamaño del tablero:")
            print("1. 4x4")
            print("2. 6x6")
            print("3. 8x8")
            choice = int(input("Ingrese el número correspondiente al tamaño deseado: "))
            
            if choice == 1:
                n = 4
            elif choice == 2:
                n = 6
            elif choice == 3:
                n = 8
            else:
                print("Opción inválida. Por favor, elija 1, 2 o 3.")
                continue
            
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido para seleccionar el tamaño del tablero.")

    while True:
        try:
            # Solicitar al usuario la dificultad del juego
            game_difficulty = int(input("Ingrese la dificultad del juego (en porcentaje): "))
            if game_difficulty < 0 or game_difficulty > 100:
                print("La dificultad del juego debe estar entre 0 y 100.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido para la dificultad del juego.")

    # Crear una instancia del juego con el tamaño de la matriz y la dificultad del juego proporcionados
    game = Game(n, game_difficulty)
    turno = 0
    game.choice_alien_position()
    while True:
        # Jugar el juego
        game.print_matrix()
        if turno % 2 == 0:
            game.insert_predator_move()
            print("TURNO ALIEN!")
        else:
            row,col = game.choice_alien_move()
            print(game.alien_row,game.alien_col)
            print(row,col)
            game.insert_alien_move(row+1,col+1)
            print("TURNO DEPREDADOR!")

        turno += 1

        if game.predator_hp <= 0:
            print("Felicidades! Gano alien")
            break
        
        if game.alien_hp <= 0:
            print("Oh no! Gano depredador")
            break
    print("Gracias por jugar!")
   
if __name__ == "__main__":
    main()
            

            