def analyze_inventory(inventory):
    total_books = 0
    genre_counts = {}
    popular_genres = []
    most_stocked_book = None
    highest_copies = None

    book_titles = []
    book_details = []

    # Convert dictionary to list of keys and values
    for title in inventory:
        book_titles.append(title)
        book_details.append(inventory[title])

    i = 0
    while i < len(book_titles):
        book_title = book_titles[i]
        details = book_details[i]
        
        total_books += details['copies']

        genre = details['genre']
        if genre in genre_counts:
            genre_counts[genre] += 1
        else:
            genre_counts[genre] = 1

        if highest_copies is None or details['copies'] > highest_copies:
            highest_copies = details['copies']
            most_stocked_book = book_title
        
        i += 1

    # Identify popular genres
    for genre in genre_counts:
        genre_total = 0
        j = 0
        while j < len(book_titles):
            if book_details[j]['genre'] == genre:
                genre_total += book_details[j]['copies']
            j += 1
        if genre_total > 5:
            popular_genres.append(genre)

    return {
        'total_books': total_books,
        'popular_genres': popular_genres,
        'most_stocked_book': (most_stocked_book, highest_copies),
        'genre_counts': genre_counts
    }

inventory = {
    'Book A': {'author': 'Author 1', 'genre': 'Fiction', 'copies': 3},
    'Book B': {'author': 'Author 2', 'genre': 'Science', 'copies': 5},
    'Book C': {'author': 'Author 1', 'genre': 'Fiction', 'copies': 7},
    'Book D': {'author': 'Author 3', 'genre': 'History', 'copies': 2},
    'Book E': {'author': 'Author 4', 'genre': 'Science', 'copies': 6},
    'Book F': {'author': 'Author 2', 'genre': 'Fiction', 'copies': 4}
}

print(analyze_inventory(inventory))
