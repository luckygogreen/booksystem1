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
/*   //删除按钮的第一种弹框方式
$(".del").on("click", function () {
    vartr = $(this).parent().parent()
    //alert(vartr)
    valid = $(this).parents("tr").find("td").eq(1).text()
    //alert(valid)
    //$vallocation = $(this).parent().parent()
    swal({
            title: "Are you sure?",
            text: "You will not be able to recover this imaginary file!",
            type: "warning",
            showCancelButton: true,
            confirmButtonClass: "btn-danger",
            confirmButtonText: "Yes, delete it!",
            cancelButtonText: "No, cancel plx!",
            closeOnConfirm: false,
            closeOnCancel: false
        },
        function (isConfirm) {
            if (isConfirm) {
                alert("ssss")
                $.ajax({
                    url: "/ajaxsweetaleartdelete/",
                    type: "post",  //这里的post大小写无所谓，但是一定不要写成这样 "/post/"
                    data: {"delid": valid},
                    success: function (data) {
                        vartr.remove()
                        swal(data, "Your imaginary file has been deleted.", "success");
                    }
                })
            } else {
                swal("Cancelled", "Your imaginary file is safe :)", "error");
            }


        });
})
*/
//删除按钮的第二种弹框方式
$(".del").on("click", function () {
    vartr = $(this).parent().parent()
    //alert(vartr)
    valid = $(this).parents("tr").find("td").eq(1).text()
    //alert(valid)
    //$vallocation = $(this).parent().parent()

    swal({
            title: "Are you sure?",
            text: "Your will not be able to recover this imaginary file!",
            type: "warning",
            showCancelButton: true,
            confirmButtonClass: "btn-danger",
            confirmButtonText: "Delete",
            cancelButtonClass: "btn-danger",
            cancelButtonText: "No",
            closeOnConfirm: false
        },
        function () {
            $.ajax({
                url: "/ajaxsweetaleartdelete/",
                type: "post",  //这里的post大小写无所谓，但是一定不要写成这样 "/post/"
                data: {"delid": valid},
                success: function (data) {
                    vartr.remove()
                    swal("Success",data, "success");
                }
            })

        })

})

//ajaxtest页面点我功能
$("#button1").click(function () {
        var text = [[1,2,3,5],[6,7,8,9]]
        var jasontext = JSON.stringify(text)
        $.ajax({
                url: "/ajaxtest/",
                type: "post",
                dataType:"json",
              //  traditional:true,
                data:{"name":"kevin","age":18,"status":1,"tags":jasontext},
                //data:{"name":"kevin","age":18,"status":1,"tags":[[1,2,3,5],[6,7,8,9]]},
                success: function (data) {
                    alert(data)
                    if (data.status == 0){
                        alert(data)
                    }else {
                        alert("数据不存在")
                    }

                }
        })

})
//验证用户名是否存在
//$("#text1").blur(function () {
//$("#text1").on("change input",function () {  //如果用input change 方法这个事件可以单独用，也可以一起用，只有这样写可以通过Chrome测试，直接写 input(function ()，Chrome运行不了
$("#text1").on("input",function () {
   // alert("good");
        $.ajax({
                url: "/ajaxblur/",
                type: "POST",
                data: {"text1": $("#text1").val()},
                success: function (data) {
                   // alert(data)
                    if (data == "0"){
                        $("#lable1").text("用户名可以使用")
                        $("#lable1").css("color","black")
                       // alert(data)
                    }else {
                        $("#lable1").text("用户名已经存在,请使用其他用户名");
                        $("#lable1").css("color","red")
                        //alert(data)
                    }
                }
            })
})