from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# 引入能上传文件的字段
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class GoodsCategory(models.Model):
    """
    商品类别
    """
    CATEGORY_TYPE = (
        (1, '一级类目'), (2, '二级类目'), (3, '三级类目')
    )
    name = models.CharField(verbose_name='类别名称', max_length=50, help_text='类别名称')
    code = models.CharField(verbose_name='类别编码', max_length=50, help_text='类别编码')
    desc = models.TextField(verbose_name='类别描述', default='', help_text='类别描述')
    category_type = models.CharField(choices=CATEGORY_TYPE, verbose_name='类目级别', help_text='类目级别',max_length=20)
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name='父类别',
                                        related_name='sub_cat', on_delete=models.CASCADE)  # 无限分类的写法，自己继承自己
    is_tab = models.BooleanField(default=False, verbose_name='是否首页导航', help_text='是否首页导航')
    add_time = models.DateTimeField(default=datetime.utcnow, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name


class GoodsCategoryBrand(models.Model):
    """品牌名"""
    name = models.CharField(verbose_name='品牌名字', max_length=50, default='', help_text='品牌名字')
    desc = models.TextField(verbose_name='品牌描述', max_length=200, default='', help_text='品牌描述')
    image = models.ImageField(upload_to='brand/images/', verbose_name='图片上传', max_length=200)
    # image = RichTextUploadingField()
    add_time = models.DateTimeField(default=datetime.utcnow, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = verbose_name


class Goods(models.Model):
    """商品"""
    category = models.ForeignKey(GoodsCategory, null=True, blank=True, verbose_name='商品类目', on_delete=models.CASCADE)
    goods_sn = models.CharField(verbose_name='商品编码', default='', max_length=50)
    name = models.CharField(verbose_name='商品名称', max_length=300)
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    sold_num = models.IntegerField(default=0, verbose_name='商品销售量')
    fav_num = models.IntegerField(default=0, verbose_name='收藏数')
    goods_num = models.IntegerField(default=0, verbose_name='库存数')
    market_price = models.FloatField(default=0, verbose_name='市场价格')
    shop_price = models.FloatField(default=0, verbose_name='本店价格')
    goods_brief = models.TextField(verbose_name='商品简短描述', max_length=500)
    goods_desc = RichTextUploadingField()
    ship_free = models.BooleanField(default=True, verbose_name='是否承担运费')
    goods_front_image = models.ImageField(upload_to="", null=True, blank=True, verbose_name='封面图片')
    is_new = models.BooleanField(default=False, verbose_name='是否新品')
    is_hot = models.BooleanField(default=False, verbose_name='是否热销')
    add_time = models.DateTimeField(default=datetime.utcnow, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name


class GoodsImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods, verbose_name='商品', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='', verbose_name='图片', null=True, blank=True)
    image_url = models.CharField(max_length=300, null=True, blank=True, verbose_name='图片url')
    add_time = models.DateTimeField(default=datetime.utcnow, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """
    主页轮播商品图
    """
    goods = models.ForeignKey(Goods, verbose_name='商品', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='banner', verbose_name='轮播图片')
    index = models.IntegerField(default=0, verbose_name='轮播顺序')
    add_time = models.DateTimeField(default=datetime.utcnow, verbose_name='添加时间')

    class Meta:
        verbose_name = '首页轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
