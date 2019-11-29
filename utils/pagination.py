#此类用于实现列表分页功能
#Kevin 创建与2019年11月29日，12:56AM

#调用快捷键:
# Pagination(Number_of_Data,Selected_Page,display_number_per_page,Maximum_number_of_pages_displayed)
class Pagination(object):
    def __init__(self,datarow,currentpage,dataperpage=10,maxpage=10): # 参数分别为，总返回的数据行数，当前页数，每页显示数量，最多显示多少页
        '''

        :param datarow: 总返回的数据行数
        :param currentpage: 当前页数
        :param dataperpage: 每页显示数量
        :param maxpage: 最多显示多少页
        '''
        self.totalpages, m=divmod(datarow,dataperpage) # divmod（总返回的数据行数，每页显示数量）返回两个数，第一个是倍数，第二个是余数 = 总返回的数据行数 //每页显示数量 取余，分别返回给两个函数totalpages,m
        startpage = 1  #起始页初始值
        endpage = self.totalpages+1 #结束页初始值
        try:  # 用于判断浏览器传入的值currentpage是否是数字，
            self.pagecurrent = int(currentpage)
        except Exception as e:
            print(e)
            self.pagecurrent = 1 #如果不为数字，则默认给当前页赋值为第一页 self.pagecurrent = 1
        self.lastpage = self.totalpages #给默认最后一页赋值为所有页
        self.pagerange = range(1,maxpage) #初始值设定，给浏览器循环取值，定义取值范围
        self.previous =self.pagecurrent-1 #默认上一页等于当前页-1
        self.next = self.pagecurrent + 1 #默认下一页等于当前页+1
        self.previous_switch = 1 #默认显示上一页
        self.next_switch = 1 #默认显示下一页
        self.startnum = (self.pagecurrent-1)*dataperpage #默认给查询数据切片的开始参数赋值  格式为:[开始：结束]
        self.endnum = self.pagecurrent*dataperpage #默认给查询数据切片的结束参数赋值，
        if self.pagecurrent <=1: #判断如果当前页为首页，不显示上一页
            self.previous_switch = 0
        if self.pagecurrent >= self.totalpages: #判断如果当前页为最后一页，不显示下一页
            self.next_switch = 0
        if self.pagecurrent <= 0: #如果当前页小于等于0则没有数据 ，赋值让用户取数据库的第一个数据，然后结束为，每页显示的数据
            self.startnum = 0
            self.endnum = dataperpage
        if self.pagecurrent >self.totalpages: #如果当前页大于总页数，则让开始数据，取倒数后10个
            self.startnum = self.totalpages*dataperpage-dataperpage
            self.endnum = self.totalpages*dataperpage
        if m != 0: #如果上面给self.totalpages赋值有余数，那么总页数+1，因为51条数据，每页显示10天，需要6页显示
            self.totalpages +=1
            self.lastpage = self.totalpages
        halfpages = maxpage//2 #整除去掉余数 ，得到页面显示页数的中间值
        if self.totalpages > maxpage: # 如果总页数大于最大显示页数
            if self.pagecurrent > halfpages: #并且 当前页大于中间页数
                startpage = self.pagecurrent-halfpages #开始页 = 当前页数-中间页数   例如，总页数是18，当夜页是7，那么显示7-5=2【2，3，4。。。。7。。。。。。12】
                endpage = self.pagecurrent + halfpages #结束页 = 当前页+中间页      例如，总页数18，当前页是7，那么显示7+5=12
                if self.pagecurrent >= self.totalpages-halfpages: #如果当前页大于总页数-中间页，例如，当前页50 > 总页数52-中间页5
                    startpage = self.totalpages-maxpage #那么 开始页  = 总页数52 -最大显示页10 = 42
                    endpage = self.totalpages+1 #结束页 = 总页数+1 = 53，因为循环体range(42,53) 表示取大于等于42，且小于53的值
                elif self.pagecurrent <= 1: # 如果总页数大于最大显示页数 并且当前页大于中间页数 并且 当前页小于等于1的时候
                    startpage = 1 #开始页 为第一页
                    endpage = maxpage + 1 #结束页为最大页+1
                else:
                    if self.pagecurrent >= self.totalpages: #如果总页数大于最大显示页数，并且 当前页大于中间页数，并且 当前页大于等于总页
                        endpage = self.totalpages+1 #结束页 = 总页+1
                        startpage = self.totalpages-maxpage #开始页 = 总页-最大显示页
            else: # 如果总页数大于最大显示页数 #并且 当前页小于等于中间页数
                endpage = maxpage+1 # 结束页为最大页+1
        self.pagerange = range(startpage, endpage) #给页面页数循环区间赋值
        #后台打印监控数据
        print('当前页:',self.pagecurrent)
        print('起始数:',self.startnum,'结束数:',self.endnum)
        print('开始页:',startpage,'结束页:',endpage)
        print('上一页：',self.previous,'上一页开关：',self.previous_switch)
        print('下一页：',self.next,'下一页开关：',self.next_switch)
    #显示起始数
    @property
    def begin_num(self):
        return self.startnum
    #显示结尾数
    @property
    def end_num(self):
        return self.endnum
    #显示页数区间
    @property
    def page_range(self):
        return self.pagerange
    #显示尾页数
    @property
    def last_page(self):
        return self.lastpage
    #显示当前页数
    @property
    def page_current(self):
        return self.pagecurrent
    #显示上一页
    @property
    def page_previous(self):
        return self.previous
    #显示下一页
    @property
    def page_next(self):
        return self.next
    #上一页开关
    @property
    def page_previous_switch(self):
        return self.previous_switch
    #下一页开关
    @property
    def page_next_switch(self):
        return self.next_switch