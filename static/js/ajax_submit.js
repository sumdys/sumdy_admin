/**
 * Created by hesheng on 2018-02-05.
 */
$(document).ready(function(){
    var valid = $("#commentForm").Validform({
        tiptype: 4,
        showAllError: true,
        ajaxPost: true,
        postonce: true,
        callback: function (data) {
               // console.log(data.msg);return false;
            var reset = $('button[type=reset]');
            if (data.success) {
                layer.alert(data.msg, function(){
                    $('input').val('');
                    window.location.href = "/backstage_menu";
                });
            } else {
                layer.msg(data.msg, {
                    icon: 2
                });
            }
            $('#btnDefault').button('reset');
            layer.closeAll('loading');
        }
    });


    //提交表单
    $('#btnSubmit').click(function () {
        $(this).button('loading');
        //loading层
        var index = layer.load(1, {
            shade: [0.1, '#fff'] //0.1透明度的白色背景
        });

        var param = $('#commentForm').serializeArray();
//            console.log(param);return false;
        valid.config({
            ajaxpost: {
                data: param
            }
        });

        if (valid.check()) {
            valid.ajaxPost();
        } else {
            $(this).button('reset');
            layer.msg('表单有错哦，检查一下吧', {
                icon: 7
            });
            layer.closeAll('loading'); //关闭加载层
        }
    });
});