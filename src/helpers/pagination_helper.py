def paginationHelper(data: list, page: int, per_page: int):
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    data = data[start_index: end_index]
    return data