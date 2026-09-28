# 自定义水印-eafc_cus_watermark_bas

## 自定义水印-主表 tk_eafc_cus_watermark_bas

- **表名称：** 自定义水印-主表
- **表名：** tk_eafc_cus_watermark_bas

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fk_eafc_fontsize_jy | 水印字号 | varchar | 50 |  | √ | ' ' | 水印字号,枚举: 12 :12 14 :14 16 :16 18 :18 20 :20 22 :22 24 :24 26 :26 28 :28 36 :36 48 :48 72 :72 |
| 4 | fk_eafc_texttype_dc | 文字内容 | varchar | 200 |  | √ | ' ' | 文字内容 |
| 5 | fk_eafc_type_dy | 水印类型 | varchar | 50 |  | √ | ' ' | 水印类型,枚举: 1 :不显示 2 :文字 |
| 6 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fk_eafc_type_jy | 水印类型 | varchar | 50 |  | √ | ' ' | 水印类型,枚举: 1 :不显示 2 :文字 |
| 9 | fk_eafc_color_jy | 水印颜色 | varchar | 50 |  | √ | ' ' | 水印颜色,枚举: #333 :黑色 #D0010A :红色 #F09913 :橙色 #FDF31C :黄色 #149117 :绿色 #1998F1 :蓝色 |
| 10 | fk_eafc_globalalpha_dc | 透明度 | varchar | 50 |  | √ | ' ' | 透明度 |
| 11 | fk_eafc_texttype_dy | 文字内容 | varchar | 200 |  | √ | ' ' | 文字内容 |
| 12 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 13 | fk_eafc_fontsize_dy | 水印字号 | varchar | 50 |  | √ | ' ' | 水印字号,枚举: 12 :12 14 :14 16 :16 18 :18 20 :20 22 :22 24 :24 26 :26 28 :28 36 :36 48 :48 72 :72 |
| 14 | fk_eafc_globalalpha_dy | 透明度 | varchar | 50 |  | √ | ' ' | 透明度 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fk_eafc_color_dy | 水印颜色 | varchar | 50 |  | √ | ' ' | 水印颜色,枚举: #333 :黑色 #D0010A :红色 #F09913 :橙色 #FDF31C :黄色 #149117 :绿色 #1998F1 :蓝色 |
| 17 | fk_eafc_fontsize_dc | 水印字号 | varchar | 50 |  | √ | ' ' | 水印字号,枚举: 12 :12 14 :14 16 :16 18 :18 20 :20 22 :22 24 :24 26 :26 28 :28 36 :36 48 :48 72 :72 |
| 18 | fk_eafc_texttype_jy | 文字内容 | varchar | 200 |  | √ | ' ' | 文字内容 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fk_eafc_type_dc | 水印类型 | varchar | 50 |  | √ | ' ' | 水印类型,枚举: 1 :不显示 2 :文字 |
| 21 | fk_eafc_color_dc | 水印颜色 | varchar | 50 |  | √ | ' ' | 水印颜色,枚举: #333 :黑色 #D0010A :红色 #F09913 :橙色 #FDF31C :黄色 #149117 :绿色 #1998F1 :蓝色 |
| 22 | fk_eafc_globalalpha_jy | 透明度 | varchar | 50 |  | √ | ' ' | 透明度 |
| 23 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 24 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__tk_eafc_cus_watermark_bas |  | fid |
