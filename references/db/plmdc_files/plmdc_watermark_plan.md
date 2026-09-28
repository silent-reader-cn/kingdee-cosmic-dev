# 水印方案配置-plmdc_watermark_plan

## 水印方案配置-主表 t_plmdc_watermark

- **表名称：** 水印方案配置-主表
- **表名：** t_plmdc_watermark

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwatermarktext | 水印文本 | varchar | 50 |  | √ | ' ' | 水印文本 |
| 3 | fmodelid | 模型id | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 4 | fcolor | 颜色 | varchar | 50 |  | √ | ' ' | 颜色,枚举: #332 :黑色 #D0010A :红色 #F09913 :橙色 #FDF31C :黄色 #149117 :绿色 #1998F1 :蓝色 |
| 5 | fpreviewfont | 字号 | varchar | 50 |  | √ | ' ' | 字号,枚举: 12 :12 14 :14 16 :16 18 :18 20 :20 22 :22 24 :24 26 :26 28 :28 36 :36 48 :48 76 :76 |
| 6 | fwatermarkcontentid | 水印内容 | int8 | 64 |  | √ | 0 | [水印内容配置 plmdc_watermark_conf](../plmdc_files/plmdc_watermark_conf.md) |
| 7 | fpreviewtransparency | 透明度% | int4 | 32 |  | √ | 0 | 透明度% |
| 8 | finherit | 是否继承 | bpchar | 1 |  | √ | '1' | 是否继承 |
| 9 | fwatermarktype | 水印类型 | bpchar | 1 |  | √ | '1' | 水印类型,枚举: 1 :用户名+手机尾号 2 :用户名+工号 3 :用户名 4 :自定义文本 |
| 10 | fpreviewcolor | 颜色 | varchar | 50 |  | √ | ' ' | 颜色,枚举: #332 :黑色 #D0010A :红色 #F09913 :橙色 #FDF31C :黄色 #149117 :绿色 #1998F1 :蓝色 |
| 11 | ffont | 字号 | varchar | 50 |  | √ | ' ' | 字号,枚举: 12px :12 14px :14 16px :16 18px :18 20px :20 22px :22 24px :24 26px :26 28px :28 36px :36 48px :48 76px :76 |
| 12 | fpreviewinherit | 是否继承 | bpchar | 1 |  | √ | '1' | 是否继承 |
| 13 | ftransparency | 透明度% | int4 | 32 |  | √ | 0 | 透明度% |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_watermark_fmodelid |  | fmodelid |
| 2 | pk_t_plmdc_watermark |  | fid |
