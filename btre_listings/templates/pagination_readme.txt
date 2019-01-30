
        <!-- PAGINATION How It is Used with Bootstrap here   -->
        <!-- 1. Create a UL and place a if loop OUTSIDE the UL  : 'if variable.has_other_pages' -->
        <!-- 2. Create a LI and place a if loop INSIDE the UL but OUTSIDE the li : 'if variable.has_previous' -->
        <!-- 3. Inside li create A-tag, with href of "?page={{listings.previous_page_number}}" : class = 'page-link' | -->
        <!--a.  href of "?page={{listings.previous_page_number}}" -->
        <!--b.  class = 'page-link' -->
        <!--c.  text inside A-tag = '&laquo;'  ==== this gives us the previous arrow -->

        <!-- 4. Else loop with a li tag -->
        <!--a.  class = 'page-item disabled'    ==== This disables the arrow if nothing there-->
        <!--b.  a-tag with class == 'page-link' -->
        <!--c. Close the if loop-->