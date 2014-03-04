'''
Created on Mar 4, 2014

@author: kylerogers
'''

class PageHelper:
    
    @staticmethod
    def get_request_count(request, default_count_per_page, max_count_per_page):
        '''
        Finds the requested number of brothers and corrects it if there are any issues
        If the number is invalid, it will return standard_brothers_per_page
        '''
        brothers_count = request.GET.get('count',str(default_count_per_page))
        try:
            brothers_count = int(brothers_count)
            if brothers_count > max_count_per_page:
                brothers_count = max_count_per_page
        except:
            brothers_count = default_count_per_page
        return brothers_count
    
    @staticmethod
    def get_page_number(request):
        '''
        Finds the page number and corrects it if there are any issues
        If the page number is invalid, it will return 1
        '''
        page_number = request.GET.get('page','1')
        try:
            page_number = int(page_number)
            if page_number < 1:
                page_number = 1
        except:
            page_number = 1
        return page_number
    
    @staticmethod
    def calculate_page_range(total_pages, page_number, max_pages_listed_on_screen):
        '''
        This determines which page numbers to show at the bottom of the brothers list pages.
        It returns a list of integers that should be displayed on the page based on the total
        number of pages and the current page number.
        '''
        if total_pages == 1: # If there is only the one page, there is no need to display page numbers
            return []
        elif total_pages <= max_pages_listed_on_screen: # In this case, just display all of the available pages
            min_page_number_displayed = 1
            max_page_number_displayed = total_pages + 1
        elif page_number - max_pages_listed_on_screen / 2 <= 1: # We are near the beginning. In this case, display from page 1 to max_pages_listed_on_screen
            min_page_number_displayed = 1
            max_page_number_displayed = min_page_number_displayed + max_pages_listed_on_screen
        elif page_number + max_pages_listed_on_screen / 2 >= total_pages: # We are near the end. In this case, display from (end - max_pages_listed_on_screen) to end
            max_page_number_displayed = total_pages + 1
            min_page_number_displayed = max_page_number_displayed - max_pages_listed_on_screen
        else: # We are somewhere in the middle. In this case, just display some pages on either side
            min_page_number_displayed = page_number - max_pages_listed_on_screen / 2
            max_page_number_displayed = min_page_number_displayed + max_pages_listed_on_screen
        
        page_numbers_list = range(min_page_number_displayed,max_page_number_displayed)    
        return page_numbers_list