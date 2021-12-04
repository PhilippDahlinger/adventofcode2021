import numpy
import numpy as np


def load_data(path):
    with open(path, "r") as file:
        rng = np.fromstring(file.readline(), dtype=int, sep=", ")
        data = np.fromstring(file.read().replace("\n", " "), dtype=int, sep=" ")
    return rng, data


def first_solution(rng, data):
    n_fields = data.shape[0] // 25
    row_data = data.reshape(n_fields * 5, 5)

    transpose_idx = np.arange(0, 25, 1, dtype=int).reshape((5, 5)).T
    transpose_idx = np.tile(transpose_idx, (n_fields, 1))
    offset = np.repeat(np.arange(0, n_fields*25, 25, dtype=int), 25).reshape((n_fields*5, 5))
    transpose_idx = transpose_idx + offset

    col_data = data[transpose_idx]

    cross_out_row = np.zeros(row_data.shape, dtype=int)
    cross_out_col = np.zeros(col_data.shape, dtype=int)
    for n in rng:
        row_idx = (row_data == n)
        col_idx = (col_data == n)
        cross_out_row[row_idx] = 1
        cross_out_col[col_idx] = 1
        # check for bingo
        if check_bingo(row_data, cross_out_row, n):
            print("row")
            break
        if check_bingo(col_data, cross_out_col, n):
            print("col")
            break

def second_solution(rng, data):
    n_fields = data.shape[0] // 25
    row_data = data.reshape(n_fields * 5, 5)

    transpose_idx = np.arange(0, 25, 1, dtype=int).reshape((5, 5)).T
    transpose_idx = np.tile(transpose_idx, (n_fields, 1))
    offset = np.repeat(np.arange(0, n_fields*25, 25, dtype=int), 25).reshape((n_fields*5, 5))
    transpose_idx = transpose_idx + offset

    col_data = data[transpose_idx]

    cross_out_row = np.zeros(row_data.shape, dtype=int)
    cross_out_col = np.zeros(col_data.shape, dtype=int)

    for n in rng:
        row_idx = (row_data == n)
        col_idx = (col_data == n)
        cross_out_row[row_idx] = 1
        cross_out_col[col_idx] = 1
        check_bingo_second(row_data, col_data, cross_out_row, cross_out_col, n)
        check_bingo_second(col_data, row_data, cross_out_col, cross_out_row, n)



def check_bingo_second(data, other_data, cross_out, other_cross_out, rng_number):
    row_mults = np.prod(cross_out, axis=1)
    if row_mults.any():
        winning_rows = np.array(np.where(row_mults == 1)).reshape(-1)
        for winning_row in winning_rows:
            winning_field_rows = np.arange(5 * (winning_row // 5), 5 * ((winning_row // 5) + 1))
            field = data[winning_field_rows]
            idx = cross_out[winning_field_rows]
            # sum of all non_crossed out values in that field
            non_selected_sum = np.sum(field * (1-idx))
            score = non_selected_sum * rng_number
            print(winning_field_rows[0] // 5, score)
            data[winning_field_rows] = -3000
            other_data[winning_field_rows] = -3000
            cross_out[winning_field_rows] = 0
            other_cross_out[winning_field_rows] = 0
        return True
    return False


def check_bingo(data, cross_out, rng_number):
    row_mults = np.prod(cross_out, axis=1)
    if row_mults.any():
        winning_row = np.argmax(row_mults)
        winning_field_rows = np.arange(5 * (winning_row // 5), 5 * ((winning_row // 5) + 1))
        field = data[winning_field_rows]
        idx = cross_out[winning_field_rows]
        # sum of all non_crossed out values in that field
        non_selected_sum = np.sum(field * (1-idx))
        print(non_selected_sum * rng_number)

        return True
    return False





if __name__ == "__main__":
    rng, data = load_data("data/04.txt")
    # first_solution(rng, data)
    second_solution(rng, data)
