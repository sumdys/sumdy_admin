from django.db import models

# Create your models here.
class item_type(models.Model):
    title = models.CharField(max_length=255)
    pid = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    sort = models.IntegerField(default=0)
    top = models.IntegerField(default=0)
    icon = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    ascription_type = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'items'
<<<<<<< HEAD
        db_table = 'item_type'
        ordering = ['-id']


class item_template(models.Model):
    name = models.CharField('商品名字',max_length=128)
    define_code = models.CharField('自定义编码',max_length=64)
    brand_id = models.SmallIntegerField('品牌ID')
    barcode = models.CharField('标准条形码 必须唯一',max_length=64)
    type = models.ForeignKey("item_type", null=True, blank=True)
    unit = models.ForeignKey("item_unit", null=True, blank=True)
    cost_price = models.IntegerField('建立成本价')
    default_price = models.IntegerField('默认价格(建立零售价)')
    image_url = models.CharField('默认图片地址',max_length=256)
    banner_url = models.CharField('banner图地址',max_length=256)
    introduction_page = models.CharField('介绍页面 不存在时可为null',max_length=256,null=False)
    status = models.SmallIntegerField('状态 0-可用 1-提交审核 2-审核不通过 3-失效',default=0)
    description = models.CharField('商品描述',max_length=512)
    uploaders_passport_id = models.BigIntegerField('上传者通行证ID',default=0)
    upload_time = models.DateTimeField('上传时间',auto_now_add=True)
    ascription_type = models.IntegerField('操作类型：1，POS,0供应链',default=0)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'items'
        db_table = 'item_template'
        ordering = ['-id']

class item_unit(models.Model):
    title = models.CharField('单位标题',max_length=20)
    status = models.SmallIntegerField('状态 0-不启动 1启动',default=1)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'items'
        db_table = 'item_unit'
=======
        ordering = ['-id']
>>>>>>> master
