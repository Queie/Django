from django.urls import include, re_path, path
from books.views import book_list, search, filters, my_image,\
						some_pdf, some_streaming_csv_view, some_pdf_complex,\
						csv_fils, csv_files_2 #,search_form


# include() 연결시 App을 선언 (중복, 오류를 방지)
app_name = 'books'
urlpatterns = [
    re_path(r'^$',            book_list, name='list'  ),
    re_path(r'^search/$',        search, name='search'),   # request.GET : Get Query경로 활용
    re_path(r'^filter/$',       filters, name='filter'),
    re_path(r'^csv/$',         csv_fils, name='csv'   ),
    re_path(r'^csv2/$',     csv_files_2, name='csv2'  ),
    re_path(r'^csv_some/$', some_streaming_csv_view, name='csv_some'),
    re_path(r'^image/$',       my_image, name='image' ),
    re_path(r'^pdf/$',         some_pdf, name='pdf'   ),
    re_path(r'^pdf2/$',some_pdf_complex, name='pdf2'  ),
]