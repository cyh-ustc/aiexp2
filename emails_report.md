# 人工智能基础编程作业2实验报告

# 垃圾邮件分类

<p align = right>陈翊辉</p>

<p align = right>PB15111656</p>

## 邮件预处理

通过观察发现，邮件数据主要包含头部，html标签，base64，图片等需要处理的部分

邮件预处理分为以下几个步骤：

* 去除头部：寻找第一个空行，删除之前内容
* 去除html标签及js代码等：使用正则表达式匹配js代码，使用简单的状态机去除html标签
* base64解码：使用字符串搜索查找base64部分，解码base64
* 将解码的base64重复第2步
* 将非字母删除
* 将字母变为小写

还有部分邮件为中文、朝鲜语、繁体中文、多部分的，手动处理即可

## 朴素贝叶斯分类器



## 引入规范项的最小二乘分类器



## 支持向量机



## 结果分析

### 朴素贝叶斯



### 最小二乘法



### 支持向量机

* 线性核函数下



* RBF核函数下





## 交叉验证



## 优化

###保存预处理的邮件结果

为了避免每次运行都重复对邮件预处理，将预处理后的邮件保存，为了方便打开，将文件名也修改为纯数字：0001，0002……

处理后的邮件仅包含小写英文字母的单词

如spam的0001

> save up to on life insurance why spend more than you have to life quote savings ensuring your family s financial security is very important life quote savings makes buying life insurance simple and affordable we provide free access to 
>
>……
>
>and or wish to be removed from our list please click here and type remove if you reside in any state which prohibits e mail solicitations for insurance please disregard this email 

###朴素贝叶斯做平滑处理



###最小二乘法用梯度下降迭代求解





## 实验心得

本实验应该是这门课程中最难的实验了；本人曾经自学Coursera的machine learning课程，其中也包含了最小二乘法分类器，支持向量机，且支持向量机的实验作业正是垃圾邮件分类，不同的是，ng的课程实验并不需要自行提取邮件，也不强调自己实现核心功能。

如果只是需要自行提取邮件生成数据，或自行实现核心算法，或调参并困难；而这些合并起来就非常困难了，以支持向量机为例：虽然表面上只需要调节sigma和C两个参数，实际上需要调节特征词选取的标准，调节SMO算法的误差接受范围epsilon，最大迭代次数等；其中任何一环不对，都会导致很低的F；还有就是调参需要花费大量时间；使用sklearn的svm能达到0.95的数据，在自行实现的SMO-SVM下就只有0.8甚至更低了。

本实验的最主要的收获是增强了对相关算法原理及应用的理解，比如朴素贝叶斯虽然有公式可以计算概率，但在实际编程中可能出现值太小低于浮点表示范围，而需要做平滑处理，又如svm用直接求解方法几乎不可能，只能使用迭代法；了解了Python非常好用的库如scipy，numpy，cvxopt，sklearn（虽然不让用）。

