# 水印配置-bos_watermark

## 水印配置-主表 t_bas_watermark

- **表名称：** 水印配置-主表
- **表名：** t_bas_watermark

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftext | 水印文本 | varchar | 100 |  |  | null | 水印文本 |
| 3 | fadddownloadwatermark | 附件下载（仅适用PDF或图片文件） | bpchar | 1 |  | √ | '0' | 附件下载（仅适用PDF或图片文件） |
| 4 | fdensity | 密度 | bpchar | 1 |  | √ | '1' | 密度,枚举: 0 :稀疏 1 :正常 2 :密集 |
| 5 | fcolor | 颜色 | varchar | 36 |  | √ | '#333' | 颜色,枚举: #333 :黑色 #D0010A :红色 #F09913 :橙色 #FDF31C :黄色 #149117 :绿色 #1998F1 :蓝色 |
| 6 | fobjectid | 对象编码 | varchar | 36 |  | √ | ' ' | 对象编码 |
| 7 | ffontsize | 字号 | varchar | 10 |  | √ | '12px' | 字号,枚举: 12px :12 14px :14 16px :16 18px :18 20px :20 22px :22 24px :24 26px :26 28px :28 36px :36 48px :48 72px :72 |
| 8 | fglobalalpha | 不透明度% | int2 | 16 |  | √ | 10 | 不透明度% |
| 9 | ftexttype | 文字内容 | bpchar | 1 |  | √ | '1' | 文字内容,枚举: 3 :用户名+手机尾号 4 :用户名+工号 2 :用户名 1 :自定义文本 |
| 10 | fpicture | 图片 | varchar | 255 |  |  | null | 图片 |
| 11 | flevel | 对象级别 | varchar | 10 |  | √ | 'root' | 对象级别,枚举: root :根节点 cloud :云节点 app :应用节点 object :业务对象节点 |
| 12 | ftype | 水印类型 | bpchar | 1 |  | √ | '0' | 水印类型,枚举: 1 :文字 2 :图片 3 :上图下文 4 :左图右文 5 :自定义插件 0 :不显示 |
| 13 | faddpreviewwatermark | 附件预览 | bpchar | 1 |  | √ | '1' | 附件预览 |
| 14 | fplugin | 插件 | varchar | 2000 |  | √ | ' ' | 插件 |
| 15 | faddimgwatermark | 图片预览（适用于图片字段） | bpchar | 1 |  | √ | '0' | 图片预览（适用于图片字段） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_watermark_pkey |  | fid |
| 2 | idx_bas_watermark_fobjectid |  | fobjectid |
