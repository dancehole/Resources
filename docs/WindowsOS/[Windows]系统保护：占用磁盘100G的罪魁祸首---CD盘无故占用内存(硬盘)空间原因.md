# 系统保护:占用磁盘100G的罪魁祸首---C/D盘无故占用内存(硬盘)空间原因



> **问题简述：**磁盘（我的为D盘）无故占用约100G，且为**突然发生**(某次开机时发现)，**不明原因**，无法查明原因。
> **解决方案简述：**删除系统保护文件，并关闭系统保护（仅供参考）

# 问题描述

如图，某天早晨打开电脑突然发现，硬盘飙红了，让我非常紧张，因为**前一天硬盘的占用还不到一半**，所以算是突然发生的异常情况。

<img align="middle" src="https://cdn.jsdelivr.net/gh/dancehole/image@main/codelabs/5a1f24ad515140518d3568ad9db97f29.png" alt="如图" style="zoom: 80%;" />
如图，D盘突然满了，但是我们点进去-全选文件-右键属性，搜索结果统计却是占用不到100G（**另外约100G神秘消失了！！**）
<img src="https://cdn.jsdelivr.net/gh/dancehole/image@main/codelabs/bf2165f74dc54ca1b47eac5f2ff2e50b.png" alt="在这里插入图片描述" style="zoom: 67%;" />
（已经显示了隐藏的文件)



# 快速解决（排查问题）

1. win+s搜索“**恢复**”（或控制面板中打开-“恢复”，win11左下角搜索框也可以直接搜索）
<img src="https://cdn.jsdelivr.net/gh/dancehole/image@main/codelabs/e54d3afdbe4541439fcc5e6023cecb9e.png" alt="在这里插入图片描述" style="zoom:50%;" />
2. 配置**系统还原**
![在这里插入图片描述](https://cdn.jsdelivr.net/gh/dancehole/image@main/codelabs/04e2f6e06b28412a91fb49e5205b13f1.png)
3. 依次选中每个磁盘 - 配置 -> 直到我们可以看到“当前使用量”-- 90G！！！我们选择“删除”
![在这里插入图片描述](https://cdn.jsdelivr.net/gh/dancehole/image@main/codelabs/7b841005659f4357b38741c0cb4372a8.png)
4. 确认“保护设置”关闭，防止下次再被莫名占用存储空间



# Debug-解决问题的方案与过程

接上-“问题描述”-：

我们用spacesniffer，查看d盘的占用情况：
![在这里插入图片描述](https://cdn.jsdelivr.net/gh/dancehole/image@main/codelabs/50affd99065d4ae9bd6310f89c0200d8.png)
非常健康，占用99G
那另外的100G呢？？？这不科学啊！！
于是在百度的指引下下载了另一个软件-Disk Space Fan
在一刹那间突然有了灵感：
![在这里插入图片描述](https://cdn.jsdelivr.net/gh/dancehole/image@main/codelabs/b8e9197cbbde4ed1b799b76d80e554c6.png)
我们可以看到有一个 $RECYCLE.BIN,我们都知道那是回收站文件，，但是---他并没有显示在“我的电脑”属性，也就是说：
系统文件我们是看不到的！
那么被占用的很有可能是系统文件
经过一番查找推断可能是一个叫做“system volume information”的文件。
这个文件是什么呢？

> System Volume Information 是一个隐藏的系统文件夹，"系统还原"工具使用该文件夹来存储它的信息和还原点。

最后，我把它关闭了（如果对安全性敏感，可以打开并把阈值调小即可）



# 其他无故占用磁盘空间的补充

除此以外，【**虚拟内存**】也属于隐藏空间内容，稍有不注意就会莫名其妙吃硬盘大部分空间（可能因为系统设置重置等原因）

**解决方案：调整虚拟内存分页的大小**

（win11下）

1. Window+i 打开设置，搜索“高级系统设置”

<img src="https://cdn.jsdelivr.net/gh/dancehole/image@main/codelabs/image-20230627115646413.png" alt="image-20230627115646413" style="zoom:50%;" />

【系统属性页】高级选项卡 ->  性能栏 -> 设置 -> 【性能属性页】高级选项卡 -> 虚拟内存 -> 更改 -> 【虚拟内存页】调整虚拟内存即可

![image-20230627120000318](https://cdn.jsdelivr.net/gh/dancehole/image@main/codelabs/image-20230627120000318.png)





> 最后修改时间：
>
> 2022.11 内容发布
>
> 2023.6.7 回答并更新了评论常见的问题【删除的影响】【其他情况的说明】