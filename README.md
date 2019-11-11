个人的c语言，轻量便捷开发工具包

```
为了便于个人在 windows 平台上更加轻量快速使用c语言开发 windows 程序。
所以这里将部分比较轻量的工具直接包装在一个 pip 下载里面，总大小约为 10M。
其中包含了：
1) tcc          编译器    (微型c语言编译器)
2) nasm         编译器    (汇编编译器，附带 ndisasm 工具)
3) upx          压缩器    (可执行程序打包工具)
4) ollydbg    32调试器    (纯净版，仅能调试32位程序)
5) procexp    进程管理    (对某些程序需要检查进程状态)
5) procmon    进程监视    (对某些程序需要监视进程行为)
6) notepad++    编辑器    (精心准备主题风格后的IDE)
```

- ##### 安装方式

```bash
cmd> pip install ii
```

- ##### 内部工具的初始化安装以及打开和使用

```bash
cmd> ii install

# 使用以上命令自动将所有工具解压，解压后即可使用
# 如果 python 的环境变量已经配置（在命令行输入 python 能执行 python 程序），则无需配置环境变量
# 即可直接在命令行中直接使用 tcc, upx, nasm(ndisasm) 的指令。
# 其中 tcc 使用了文件包含的处理，将 windows 的更多的 api 函数库文件解压合并在 tcc 工作目录里面
#     所以这里的 tcc 会比一般情况下的 tcc 开发 windows 程序要轻松得多。
# 另外 ollydbg, procexp, notepad++, procmon 均是 gui 工具。所以使用了另一种打开方式。

cmd> igui

# 使用以上命令会打开一个图形窗口，其中就有三个选项。选项的内容就是各自的工具的打开。
# 其中 notepad++ 由于体积很小可定制性强，所以我针对其风格做了个人化处理，至少比原生风格好多了
# 另外 notepad++ 打开后我个人自定义了一部分快捷键，注释的快捷键和原生的不一样。按个人习惯修改即可
# alt + q    使用tcc编译当前文件（命令同 tcc xx.c）如需更加复杂的命令配置，请善用网络搜索功能
# alt + w    执行编译后的文件，默认以当前文件名字和地址索引exe文件，并以cmd执行
# alt + d    根据当前文件位置打开命令行，解决快捷键的一定局限，更多时候还是需要命令行处理
# alt + e    打开左侧的文件夹列表窗口
# alt + r    打开右侧的文档结构图窗口
# alt + `    如果安装 gcc 在环境变量中，使用 gcc 编译当前脚本（命令同 gcc -o xx.exe xx.c）
# ctrl + /   注释/解开注释（修改了原本的 notepad 注释方式，使用了 sublime 快捷键的注释方式）
# ctrl + \              多行注释
# ctrl + shift + \      多行解注释

cmd> inote

# 使用上面的方式可以直接打开 notepad（因为编辑器的特殊性，需要更加顺手的使用方式）
```

- ##### 个人的习惯开发方式

```c
// 1) 适合喜欢轻量级的快速开发，所以通常只有很少的脚本
// 2) 个人习惯在桌面进行开发，所以会在桌面的左侧留出合适的空间用于放置脚本
// 3) win + r 打开运行窗口，输入 inote 打开 notepad++
// 4) 桌面创建一个 test.c 直接拖入notepad++，输入最初的脚本：
#include <stdio.h>
#include <windows.h>
// 注意这里，tcc 编译 win 程序没有编译成功的话，可以使用(alt+d)打开命令行来编译执行定位问题
// 有时 tcc 编译 win 程序时出现问题，只要换上下面 win 的入口的函数替代 main 得话就能编译成功。
// 这种处理的执行文件 tcc 编译后“双击执行”时自动去除黑窗口。不过看不到 printf 输出了。
// 如果要在 main 里面也能实现win函数，tcc 需注意使用 -luser32 -lkernel32 主动去链接需要的函数连接库。
int WINAPI WinMain (HINSTANCE hInstance, HINSTANCE hPrevInstance, PSTR szCmdLine, int iCmdShow) {
    MessageBoxA(NULL,"hello world.","test",0);
}
// 5) alt+q 编译， alt+w 执行。
```

