# 基础语法
## 一、标题
Markdown支持6种级别的标题，对应html标签 h1 ~ h6
```markdown
# h1
## h2
### h3
#### h4
##### h5
###### h6
```
## 二、段落及区块引用
对某段文字进行强调处理
```markdown
> 这段文字将被高亮显示
```
效果如下：
> 这段文字将被高亮显示

## 三、插入链接或者图片
**引用图片和链接的唯一区别就是在最前方添加一个感叹号。**
```markdown
[点击跳转至百度](http://www.baidu.com)
![图片](https://upload-images.jianshu.io/upload_images/703764-605e3cc2ecb664f6.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
效果如下：

[点击跳转至百度](http://www.baidu.com)
![图片](https://upload-images.jianshu.io/upload_images/703764-605e3cc2ecb664f6.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 四、列表
Markdown支持有序列表和无序列表两种形式：
* 无序列表使用*或+或-标识
* 有序列表使用数字加.标识，例如：1.

**如果在单一列表项中包含了多个段落，为了保证渲染正常，\*与段落首字母之间必须保留四个空格**
>使用转义字符 \ 来显示\*,\+等字符
```markdown
*    段落一

     小段一
*    段落二

     小段二
```

### 列表嵌套
上一级和下一级之间敲三个空格即可
```markdown
* 一级无序列表内容
   * 二级无序列表内容
   * 二级无序列表内容
   * 二级无序列表内容
```
效果如下：
* 一级无序列表内容
   * 二级无序列表内容
   * 二级无序列表内容
   * 二级无序列表内容

## 五、分隔线
有时候，为了排版漂亮，可能会加入分隔线。Markdown加入分隔线非常简单，使用下面任意一种形式都可以。
```markdown
***
---
```
***
---
【PS】产生分隔线的语法要求比较松，符号之间添加空格也可以。