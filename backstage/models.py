from django.db import models

# Create your models here.
# 菜单
class Menu(models.Model):
    name = models.CharField(max_length=255)
    pid = models.IntegerField(default=0)
    url = models.CharField(max_length=255)
    sort = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    class Meta:
        app_label = 'backstage'
        ordering = ['-id']

# 角色
class Role(models.Model):
    type_list=[
        [1,'总部'],
        [2, '门店供应商'],
        [3, '平台供应商']
    ]

    name = models.CharField(max_length=255)
    type = models.IntegerField(choices=type_list,default=0)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'backstage'

# 权限规则
class Rule(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'backstage'

# 角色和用户关系
class Passport_Role(models.Model):
    passport_id = models.IntegerField(default=0)
    role_id = models.IntegerField(default=0)

    def __str__(self):
        return self.passport_id

    class Meta:
        app_label = 'backstage'

# 角色和菜单关系
class Role_menu(models.Model):
    role_id = models.IntegerField(default=0)
    menu_id = models.IntegerField(default=0)

    def __str__(self):
        return self.menu_id

    class Meta:
        app_label = 'backstage'

# 角色和权限关系
class Role_Rule(models.Model):
    role_id = models.IntegerField(default=0)
    rule_id = models.IntegerField(default=0)

    def __str__(self):
        return self.rule_id

    class Meta:
        app_label = 'backstage'
