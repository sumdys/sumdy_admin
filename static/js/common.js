/**
 * Created by hesheng on 2018-02-05.
 * @param string btnSubmit 点击按钮ID
 * @param string commentForm from表单
 */
function ajaxSubmit(returnUrl,btnSubmit,commentForm,boolStr){
    var valid = $("#"+commentForm).Validform({
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
                    if(boolStr){
                        window.location.href = returnUrl;
                    }
                });
            } else {
                layer.msg(data.msg, {
                    icon: 2
                });
            }
            $('#'+btnDefault).button('reset');
            layer.closeAll('loading');
        }
    });


        //提交表单
    $('#'+btnSubmit).click(function () {
        $(this).button('loading');
        //loading层
        var index = layer.load(1, {
            shade: [0.1, '#fff'] //0.1透明度的白色背景
        });
        var param = $('#'+commentForm).serializeArray();
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
}


/**
 * 异步请求
 * @param string msg 提示信息
 * @param string url 请求地址
 * @param array data 请求数据
 */
function layer_really(msg,url,data) {
	//询问框
	layer.confirm(msg, {
	    btn: ['确定','取消'] //按钮
	}, function(){
		var index = layer.load(1, {
		  shade: [0.1,'#fff'] //0.1透明度的白色背景
		});

		$.post(url,data,function(data){
		    console.log(data);
			if (data.success) {
				layer.alert(data.msg,{icon:1},function(){
				    location.reload(true);
                });

			} else {
				layer.alert(data.msg,{icon:2});
			}
			layer.closeAll('loading');
		}).fail(function(data){

			data = eval('('+data.responseText+')');
			//第三方扩展皮肤
			layer.alert(data.msg, {
			    icon: 7,
			    skin: 'layer-ext-moon' //该皮肤由layer.seaning.com友情扩展。关于皮肤的扩展规则，去这里查阅
			});
			//layer.msg(data.msg,{icon:7});
			layer.closeAll('loading');
		})
	}, function(){
		layer.closeAll();
	});
}
