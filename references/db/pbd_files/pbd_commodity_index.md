# 大宗商品指标数据单-pbd_commodity_index

## 大宗商品指标数据单-主表 t_pbd_commodity_index

- **表名称：** 大宗商品指标数据单-主表
- **表名：** t_pbd_commodity_index

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frequencycode | 频度编码 | varchar | 50 |  | √ | ' ' | 频度编码 |
| 3 | fmetriccode | 度量编码 | varchar | 50 |  | √ | ' ' | 度量编码 |
| 4 | fcalibername | 口径名称 | varchar | 150 |  | √ | ' ' | 口径名称 |
| 5 | fbreedname | 品种名称 | varchar | 160 |  | √ | ' ' | 品种名称 |
| 6 | fsourcecode | 数据来源编码 | varchar | 50 |  | √ | ' ' | 数据来源编码 |
| 7 | funitcode | 单位编码 | varchar | 50 |  | √ | ' ' | 单位编码 |
| 8 | fmrkbrandcode | 主站品牌编码 | varchar | 50 |  | √ | ' ' | 主站品牌编码 |
| 9 | fcountrycode | 国家编码 | varchar | 50 |  | √ | ' ' | 国家编码 |
| 10 | fstatus | 指标状态 (1:正常维护 3:停止维护) | bpchar | 1 |  | √ | '0' | 指标状态 (1:正常维护 3:停止维护) |
| 11 | fmrkbrandname | 主站品牌别名 | varchar | 150 |  | √ | ' ' | 主站品牌别名 |
| 12 | fmqcode | 材质编码 | varchar | 50 |  | √ | ' ' | 材质编码 |
| 13 | fstandardcode | 标准编码 | varchar | 50 |  | √ | ' ' | 标准编码 |
| 14 | findexname | 指标名称 | varchar | 200 |  | √ | ' ' | 指标名称 |
| 15 | fscname | 规格名称 | varchar | 150 |  | √ | ' ' | 规格名称 |
| 16 | fupdatedate | 数据最新更新日期 | int8 | 64 |  | √ | 0 | 数据最新更新日期 |
| 17 | fbreedcode | 品种编码 | varchar | 50 |  | √ | ' ' | 品种编码 |
| 18 | fcalibercode | 口径编码 | varchar | 50 |  | √ | ' ' | 口径编码 |
| 19 | fstandardname | 标准名称 | varchar | 150 |  | √ | ' ' | 标准名称 |
| 20 | fsourcename | 数据来源名称 | varchar | 150 |  | √ | ' ' | 数据来源名称 |
| 21 | fmetricname | 度量名称 | varchar | 150 |  | √ | ' ' | 度量名称 |
| 22 | funitname | 单位名称 | varchar | 150 |  | √ | ' ' | 单位名称 |
| 23 | frequencyname | 频度名称 | varchar | 150 |  | √ | ' ' | 频度名称 |
| 24 | fcountryname | 国家名称 | varchar | 150 |  | √ | ' ' | 国家名称 |
| 25 | fdescription | 中文描述 | varchar | 600 |  | √ | ' ' | 中文描述 |
| 26 | fmarketname | 市场名称 | varchar | 150 |  | √ | ' ' | 市场名称 |
| 27 | findexcode | 指标编码 | varchar | 50 |  | √ | ' ' | 指标编码 |
| 28 | fmqname | 材质名称 | varchar | 150 |  | √ | ' ' | 材质名称 |
| 29 | fmarketcode | 市场编码 | varchar | 50 |  | √ | ' ' | 市场编码 |
| 30 | fsccode | 规格编码 | varchar | 50 |  | √ | ' ' | 规格编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_commodity_indexcode |  | findexcode |
| 2 | pk_pbd_commodity_index |  | fid |
