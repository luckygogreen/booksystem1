from django.shortcuts import HttpResponse,render,redirect
#中间件，只需要定义中间件包，然后在Setting中调用即可
from django.utils.deprecation import MiddlewareMixin
whiteurl = ['/ajaxdemo/','/ajaxtest/']
# 判断路径是否在白名单中，如果在返回页面，如果不在，给出提示
class MD1(MiddlewareMixin):
    def process_request(self, request):
        pass
        # print("MD1里面的 process_request")
        # geturl = request.path_info
        # print(geturl)
        # if geturl in whiteurl:
        #     return # render(request,geturl)
        # else:
        #     return HttpResponse("gun")

#response  按照Setting 注册顺序倒序执行，必须返回一个HTTP相应，HttpResponse
    def process_response(self, request, response):
        # print("MD1里面的 process_response")
        return response

    # Django会在调用视图函数之前调用process_view方法。
    # 它应该返回None或一个HttpResponse对象。 如果返回None，Django将继续处理这个请求，执行任何其他中间件的process_view方法，
    # 然后在执行相应的视图。 如果它返回一个HttpResponse对象，Django不会调用适当的视图函数。
    # 它将执行中间件的process_response方法并将应用到该HttpResponse并返回结果。
    def process_view(self, request, view_func, view_args, view_kwargs):
        pass
        # print("-" * 80)
        # print("MD1 中的process_view")
        # print(view_func, view_func.__name__)

# process_exception(self, request, exception)
# 该方法两个参数:
# 一个HttpRequest对象
# 一个exception是视图函数异常产生的Exception对象。
# 这个方法只有在视图函数中出现异常了才执行，它返回的值可以是一个None也可以是一个HttpResponse对象。
# 如果是HttpResponse对象，Django将调用模板和中间件中的process_response方法，并返回给浏览器，
# 否则将默认处理异常。如果返回一个None，则交给下一个中间件的process_exception方法来处理异常。
# 它的执行顺序也是按照中间件注册顺序的倒序执行。
# 如果想触发一个异常来验证，可以在任何函数下面加上一句
# raise ValueError("呵呵")    触发异常
    def process_exception(self, request, exception):
        print(exception)
        print("MD1 中的process_exception")


# process_template_response(self, request, response)
# 它的参数，一个HttpRequest对象，response是TemplateResponse对象（由视图函数或者中间件产生）。
# process_template_response是在视图函数执行完成后立即执行，
# 但是它有一个前提条件，那就是视图函数返回的对象有一个render()方法
# （或者表明该对象是一个TemplateResponse对象或等价方法）。
# 详情请查看下面链接
# https://www.cnblogs.com/liwenzhou/p/8761803.html