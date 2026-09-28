# 定标汇总招标项目-src_decisionsum_pro

## 项目分录-子表 t_src_decisionsum_pro

- **表名称：** 项目分录-子表
- **表名：** t_src_decisionsum_pro

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectid | 寻源项目编号 | int8 | 64 |  | √ | 0 | [定标F7 src_decisionf7](../src_files/src_decisionf7.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_sum_pro_fprojectid |  | fprojectid |
| 2 | pk_src_decisionsum_pro |  | fentryid |

---

## 定标汇总招标项目-主表 t_src_decisionsum

- **表名称：** 定标汇总招标项目-主表
- **表名：** t_src_decisionsum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisproject | fisproject | bpchar | 1 |  | √ | '0' |  |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fsourceid | 寻源项目 | int8 | 64 |  | √ | 0 | [项目立项F7 src_demandnotwo](../src_files/src_demandnotwo.md) |
| 5 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | fbilldate | fbilldate | timestamp | 0 |  |  | null |  |
| 7 | fpurdeptid | fpurdeptid | int8 | 64 |  | √ | 0 |  |
| 8 | fsrctypeid | fsrctypeid | int8 | 64 |  | √ | 0 |  |
| 9 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | forigin | 发起方 | varchar | 30 |  | √ | ' ' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 12 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 13 | fsumamount | fsumamount | numeric | 23 | 10 | √ | 0 |  |
| 14 | fispackage | fispackage | bpchar | 1 |  | √ | '0' |  |
| 15 | fpurgroupid | fpurgroupid | int8 | 64 |  | √ | 0 |  |
| 16 | fismultipackage | fismultipackage | bpchar | 1 |  | √ | '0' |  |
| 17 | fbudgetamount | fbudgetamount | numeric | 23 | 10 | √ | 0 |  |
| 18 | fsumtype | fsumtype | bpchar | 1 |  | √ | ' ' |  |
| 19 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 20 | fbidname | fbidname | varchar | 300 |  | √ | ' ' |  |
| 21 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 22 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 23 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 24 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 25 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 26 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 27 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 28 | fiscategory | fiscategory | bpchar | 1 |  | √ | '0' |  |
| 29 | fsourcetypeid | fsourcetypeid | int8 | 64 |  | √ | 0 |  |
| 30 | fsumtaxamount | fsumtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 31 | fisprice | fisprice | bpchar | 1 |  | √ | '0' |  |
| 32 | fcurrentnode | fcurrentnode | int8 | 64 |  | √ | 0 |  |
| 33 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 34 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_decisionsum_fparentid |  | fparentid |
| 2 | pk_src_decisionsum |  | fid |
| 3 | idx_src_decisionsum_fsourceid |  | fsourceid |
| 4 | idx_src_decisionsum_fbilldate |  | fbilldate |
| 5 | idx_src_decisionsum_fbillno |  | fbillno |
