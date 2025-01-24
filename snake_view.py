def get_color(value):
        if value < 0:
              return "red"
        elif value == 0:
              return "#7CFC00"
        else: return "orange"




def draw_board(canvas, x1, y1, x2, y2, board, debug_mode):
    rows = (len(board)) 
    colums = (len(board[0])) 
    cell_width = (x2 - x1) / colums
    cell_height = (y2 -y1) / rows
    
    


    for row in range(rows):
        for col in range(colums):
            cell_x1 = x1 + cell_width*col
            cell_x2 = cell_x1 + cell_width
            cell_y1 = y1 + cell_height*row
            cell_y2 = cell_y1 + cell_height
            cell_mid_x = (cell_x1 + cell_x2)/2
            cell_mid_y = (cell_y1 + cell_y2)/2
            canvas.create_rectangle(cell_x1, cell_y1, cell_x2, cell_y2, fill=get_color(board[row][col]))
            if debug_mode:
                canvas.create_text(cell_mid_x, cell_mid_y, text = f"{row},{col}\n{board[row][col]}" )

    
    