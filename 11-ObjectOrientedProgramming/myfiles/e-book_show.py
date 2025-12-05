import e_book

book1=e_book.EBook("1984","George Orwell",328)


book1.open_book_at_page(10)
book1.status()
book1.turn_page_forward()
book1.turn_page_forward()
book1.turn_page_forward()
book1.status()
book1.turn_page_backward(15)
book1.status()
book1.turn_page_backward(12)
book1.turn_page_backward()
book1.status()
book1.close_book()
book1.status()
book1.turn_page_forward(5)

book1.status()


