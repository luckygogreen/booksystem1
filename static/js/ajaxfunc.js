//用post方法AJax
    $("#s3").on("click", function () {
        $.ajax({
            url: "/ajaxpost/",
            type: "POST",
            //csrfmiddlewaretoken 这个name是固定的，不可以更改，否则提交到Views的方法是运行不出来的
           // data: {"b1": $("#b1").val(), "b2": $("#b2").val(), "csrfmiddlewaretoken": $("[name='csrfmiddlewaretoken']").val()},
            data: {"b1": $("#b1").val(), "b2": $("#b2").val()},
            success: function (data) {
                $("#b3").val(data);
            }
        })
    })
//用 Get方法Ajax
    $("#s1").on("click", function () {
        $.ajax({
            url: "/ajaxget/",
            type: "GET",
            data: {"b1": $("#b1").val(), "b2": $("#b2").val()},
            success: function (data) {
                $("#b3").val(data);
            }
        })
    })
//AJax添加图片属性
    $("#s2").on("click", function () {
        $.ajax({
            url: "/showimg/",
            type: "get",
            success: function (imgurl) {
                imgval = document.createElement("img")
                imgval.src = imgurl
                $("#s2").after(imgval)
            }
        })
    })