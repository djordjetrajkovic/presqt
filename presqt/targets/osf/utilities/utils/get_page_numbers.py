import requests
import math


def get_page_numbers(url, token):
    """
    """
    headers = {"Authorization": "Bearer {}".format(token)}

    pagination_info = requests.get(url, headers=headers).json()['links']

    next_page = pagination_info['next']
    previous_page = pagination_info['prev']

    if next_page:
        next_page = next_page.partition('?page=')[2]
    if previous_page:
        previous_page = previous_page.partition('?page=')[2]
        if previous_page == '':
            previous_page = '1'
    total_pages = math.ceil(pagination_info['meta']['total']/pagination_info['meta']['per_page'])

    pages = {
        "first_page": '1',
        "previous_page": previous_page,
        "next_page": next_page,
        "last_page": str(total_pages),
        "total_pages": total_pages,
        "per_page": pagination_info['meta']['per_page']}

    return pages
