from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, \
					  MonthArchiveView, DayArchiveView, TodayArchiveView

from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList
from .models import Post


class PostLV(ListView):
	model               = Post
	template_name       = 'posts/index.html'
	context_object_name = 'posts'
	paginate_by         = 5

class PostDV(DetailView):
	model = Post

class PostTOL(TaggedObjectList):
	model         = Post
	template_name = 'tagging/post_list.html'


# Search Form 의 활용
from django.db.models import Q                 # 검색에 필요한 Q 클래스
from django.shortcuts import render            # 단축함수
from django.views.generic.edit import FormView # Form 객체출력
from .forms import SearchForm

# Post 게시물 중 검색
class Search(FormView):
	form_class = SearchForm                    # form 함수 Class와 연결
	template_name = 'posts/post_search.html'

	# 유효성 검사 후 함수를 실행
	def form_valid(self, form):
		schWord = '%s' %self.request.POST['search_word']      # SearchForm 클래스 POST 전달객체
		post_list = Post.objects.filter(\
					Q(title__icontains=schWord)|\
					Q(description__icontains=schWord)|\
					Q(content__icontains=schWord)).distinct() # distinct() : 중복 객체는 제외

		# 검사 결과를 content {dict}로 저장
		content = {}
		content['form'] = form
		content['search_term'] = schWord
		content['object_list'] = post_list
		return render(self.request, self.template_name, content)


# 사용자 추가 모듈
# https://docs.djangoproject.com/en/2.0/topics/auth/default/
from django.contrib.auth.mixins import LoginRequiredMixin            # 2.0 모듈로 로그인 확인
from django.views.generic import CreateView, UpdateView, DeleteView  # 사용추가
from django.urls import reverse_lazy


# 주의 !!
# fields : s 를 뺴먹어서 LoginRequiredMixin 오류가 발생
class Create(LoginRequiredMixin, CreateView): # 로그인 확인
	model       = Post
	fields      = ['title', 'slug', 'description', 'content', 'tag']  # 생성필드 목록 # id만 자동생성
	initial     = {'slug':'auto-filling-do-not-input'}                # slug 초기값 설정
	success_url = reverse_lazy('blog:index')                          # 결과출력 template

	# 유효성 검사 내용추가
	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super(Create, self).form_valid(form)


# LoginRequiredMixin 확인결과 변경 가능한 목록을 출력
# ListView 편집이 가능한 개체들을 출력
class Change(LoginRequiredMixin, ListView):
	template_name = 'posts/post_change.html'

	# owner 컬럼의 조건문으로 객체를 선별
	def get_queryset(self):
		return Post.objects.filter(owner = self.request.user)


class Update(LoginRequiredMixin, UpdateView):
	model       = Post
	fields      = ['title','slug','description','content','tag']
	success_url = reverse_lazy('post:index')


class Delete(LoginRequiredMixin, DeleteView):
	models        = Post
	template_name = 'posts/post_delete.html'
	success_url   = reverse_lazy('post:index')

	# missing a QuerySet 오류 발생 : 명확하게 객체를 선언함수를 추가
	def get_queryset(self):
		return Post.objects.filter(owner = self.request.user)