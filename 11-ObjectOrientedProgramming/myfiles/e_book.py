class EBook:
    def __init__(self,title,author,number_of_pages,current_page=1,is_open=False):
        self.title=title
        self.author=author
        self.number_of_pages=number_of_pages
        self.current_page=current_page
        self.is_open=is_open
        
    def open_book_at_page(self,page):
        self.is_open=True
        self.current_page=page

    def close_book(self):
        self.is_open=False
        self.current_page=1
    

    def status(self):
        print(f"Title: {self.title} by {self.author}, number of pages: {self.number_of_pages}",end=", ")
        print(f"Book is {'open' if self.is_open else 'closed'} at page {self.current_page}")



    def turn_page_forward(self,page=1):
        if self.is_open and self.current_page+page <= self.number_of_pages:
            self.current_page += page
    
    def turn_page_backward(self,page=1):
        if self.is_open and self.current_page-page >= 1:
            self.current_page -= page