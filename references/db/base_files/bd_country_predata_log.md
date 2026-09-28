# 国家更新记录-bd_country_predata_log

## 国家更新记录-主表 t_bd_country_log

- **表名称：** 国家更新记录-主表
- **表名：** t_bd_country_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 2000 |  | √ | ' ' | 名称 |
| 3 | ftwocountrycode | 二字码 | varchar | 50 |  | √ | ' ' | 二字码 |
| 4 | fpresetlogid | 版本更新记录id | int8 | 64 |  | √ | 0 | 版本更新记录id |
| 5 | ffullname | 全称 | varchar | 2000 |  | √ | ' ' | 全称 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fcountryid | 国家或地区id | int8 | 64 |  | √ | 0 | 国家或地区id |
| 8 | fdescription | 英文全称 | varchar | 512 |  | √ | ' ' | 英文全称 |
| 9 | fthreecountrycode | 三字码 | varchar | 100 |  | √ | ' ' | 三字码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fupdatemode | 更新方式 | varchar | 18 |  | √ | ' ' | 更新方式,枚举: insert :新增 update :更新 disable :禁用 |
| 12 | fnumericcode | 数字编码 | varchar | 100 |  | √ | ' ' | 数字编码 |
| 13 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 14 | fareacode | 国际电话区号 | varchar | 20 |  | √ | ' ' | 国际电话区号 |
| 15 | fsimplespell | 英文简称 | varchar | 128 |  | √ | ' ' | 英文简称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_country_log |  | fid |
| 2 | idx_bd_country_prelogid |  | fpresetlogid |
