from django.shortcuts import render, get_object_or_404
from blogs.models import Category, Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


# https://docs.djangoproject.com/en/2.0/topics/pagination/
# https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
def index(request):
	category = Category.objects.all()
	posts = Blog.objects.all()

	# 5개를 1페이지 단위로 자동분할
	page = request.GET.get('page', 1)  # 초기값 설정
	paginator = Paginator(posts, 5)
	try:
		post_pag_obj = paginator.page(page)
	except PageNotAnInteger:   # ?page= 쿼리에 숫자아닌 내용이 온 경우
		post_pag_obj = paginator.page(1)
	except EmptyPage:          # ?page= 쿼리에 아무것도 없을 떄
		post_pag_obj = paginator.page(paginator.num_pages)
	content = {'categories':category, 'posts':post_pag_obj}
	return render(request, 'blogs/index.html', content)


# 카테고리 페이지 설정
def category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	print(category)                                  # __str__ 선언된  title 컬럼이 출력
	post = Blog.objects.filter(category=category)    # 외래키 연결 id로 필터링
	content = {'categories':category, 'posts':post}
	return render(request, 'blogs/category.html', content)


# 개별 페이지 설정
def post(request, pk):
	content = {'post':get_object_or_404(Blog, pk=pk)}
	return render(request, 'blogs/post.html', content)


# 블로그 내용 검색
def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:         errors.append('내용을 입력해 주세요.')
		elif len(q) > 20: errors.append('글자가 20자를 넘습니다.')
		else:                 # 1),2)를 통과한 < 정상객체 >
			posts = Blog.objects.filter(title__icontains=q)
			return render(request, 'blogs/search_result.html',
				          {'books':posts, 'query':q})

	return render(request, 'blogs/search_form.html',{'errors':errors})