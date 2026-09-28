# 印花税税源采集税目-tcret_tax_source_yhssm

## 印花税税源采集税目-主表 t_tcret_sycj_yhssm

- **表名称：** 印花税税源采集税目-主表
- **表名：** t_tcret_sycj_yhssm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisverify | 是否核定征收 | bpchar | 1 |  | √ | '0' | 是否核定征收 |
| 3 | ftaxitem | 税目 | int8 | 64 |  | √ | 0 | 印花税税率 tpo_tcsd_taxrateentry |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | ftaxlimit | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :月 season :季度 halfyear :半年 year :年 single :次 |
| 7 | fhdrate | 核定比例 | numeric | 23 | 10 | √ | 0.0000000000 | 核定比例 |
| 8 | fdeclaretype | 申报期限类型 | varchar | 50 |  | √ | ' ' | 申报期限类型,枚举: aqsb :按期申报 acsb :按次申报 |
| 9 | fgathernumber | 采集编号 | varchar | 50 |  | √ | ' ' | 采集编号 |
| 10 | fpaytype | 缴纳类型 | varchar | 50 |  | √ | ' ' | 缴纳类型,枚举: bdjn :本地缴纳 ydjn :异地缴纳 |
| 11 | feffectivedate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 12 | fexpirydate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 13 | ftaxoffice | 税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_sycj_yhssm |  | fid |
| 2 | idx_tcret_sycj_yhssm |  | forgid,feffectivedate,fexpirydate |
