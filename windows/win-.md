# windows 10 发布者不受信

## 编辑注册表

HKEY\_CURRENT\_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Associations

> 如果没有Associations 新建一个项 在Associations 项下面建立LowRiskFileTypes\(字符串值\) value 填写需要运行的文件后缀名，例如：.exe 允许exe运行

## 更改用户策略

1. “win+x”进入控制面板，选择安全性与维护，在左侧更改windows smartscreen筛选器设置，选择"不执行任何操作"，单击确定即可。

2. “win+x”进入控制面板，选择用户账户，选择最下面的“更改用户账户控制设置”，把滑条拉到最下面“从不通知”。

3. “win+r”打开运行，输入gpedit.msc进入组策略，依次选择“计算机配置”、“windows设置”、“安全设置”、“本地策略”、“安全选项”，在右侧下拉选择“用户账户控制：以管理员批准模式运行所有管理员”，双击它，选择“已禁用”，重启即可关闭用户账户控制。

> PS: 用户账户控制的关闭会导致edge、应用商店、播放器等无法打开。如果只是安装出现此类问题，建议安装后重启用户账户控制。



