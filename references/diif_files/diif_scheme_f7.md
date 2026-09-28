# 预测方案F7-diif_scheme_f7

## 预测方案F7-主表 t_diif_scheme

- **表名称：** 预测方案F7-主表
- **表名：** t_diif_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fapproverid | fapproverid | int8 | 64 |  | √ | 0 |  |
| 4 | fnextforecastdate | fnextforecastdate | timestamp | 0 |  |  | null |  |
| 5 | fcycleunit | 预测周期单位 | varchar | 50 |  | √ | ' ' | 预测周期单位,枚举: MONTH :月 WEEK :周 DAY :日 |
| 6 | fsourceid | 数据源 | int8 | 64 |  | √ | 0 | 预测数据源 diif_source |
| 7 | fcustomerstdid | fcustomerstdid | int8 | 64 |  | √ | 0 |  |
| 8 | fmaterialdim | fmaterialdim | varchar | 50 |  | √ | ' ' |  |
| 9 | frefhistorycyclecount | frefhistorycyclecount | int4 | 32 |  | √ | 0 |  |
| 10 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' |  |
| 11 | fusepromodel | fusepromodel | bpchar | 1 |  | √ | '0' |  |
| 12 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 13 | fidsschmeid | fidsschmeid | varchar | 50 |  | √ | ' ' |  |
| 14 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 15 | fcustomdimbasetype | fcustomdimbasetype | varchar | 50 |  | √ | ' ' |  |
| 16 | fsys | fsys | bpchar | 1 |  | √ | '0' |  |
| 17 | fcyclecount | 预测周期数 | int4 | 32 |  | √ | 0 | 预测周期数 |
| 18 | frollingexpirydate | frollingexpirydate | timestamp | 0 |  |  | null |  |
| 19 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 20 | fapprovedate | fapprovedate | timestamp | 0 |  |  | null |  |
| 21 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 22 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 23 | frollingdateset | frollingdateset | varchar | 50 |  | √ | ' ' |  |
| 24 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: Z :暂存 A :创建 B :审核中 C :已审核 |
| 25 | fincludecurrentcycle | 预测包含本期 | bpchar | 1 |  | √ | '0' | 预测包含本期 |
| 26 | flatestforecastcycle | 最新预测运算周期 | varchar | 50 |  | √ | ' ' | 最新预测运算周期 |
| 27 | fmaterialstdid | fmaterialstdid | int8 | 64 |  | √ | 0 |  |
| 28 | fcustomerenable | fcustomerenable | bpchar | 1 |  | √ | '0' |  |
| 29 | flatestforecastdate | 最新预测运算时间 | timestamp | 0 |  |  | null | 最新预测运算时间 |
| 30 | fcustomerdim | fcustomerdim | varchar | 50 |  | √ | ' ' |  |
| 31 | fforecastdim | 预测维度 | varchar | 100 |  | √ | ' ' | 预测维度 |
| 32 | ftype | ftype | varchar | 50 |  | √ | ' ' |  |
| 33 | fscheduleid | fscheduleid | varchar | 100 |  | √ | ' ' |  |
| 34 | fsalesfuncdim | fsalesfuncdim | varchar | 50 |  | √ | ' ' |  |
| 35 | fmodelstatus | fmodelstatus | varchar | 50 |  | √ | ' ' |  |
| 36 | fcustomenable | fcustomenable | bpchar | 1 |  | √ | '0' |  |
| 37 | frollingforecast | 自动执行滚动预测 | bpchar | 1 |  | √ | '0' | 自动执行滚动预测 |
| 38 | fforecastbilltype | fforecastbilltype | varchar | 50 |  | √ | ' ' |  |
| 39 | falgorithm | falgorithm | varchar | 50 |  | √ | ' ' |  |
| 40 | fresponsiblevisible | fresponsiblevisible | bpchar | 1 |  | √ | '0' |  |
| 41 | frollingpredtime | frollingpredtime | int4 | 32 |  | √ | '-1' |  |
| 42 | fcustomdimbasefield | fcustomdimbasefield | varchar | 50 |  | √ | ' ' |  |
| 43 | fnoforcastwithouttrans | fnoforcastwithouttrans | bpchar | 1 |  | √ | '0' |  |
| 44 | frollingcron | frollingcron | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_diif_scheme_billno |  | fbillno |
| 2 | pk_t_diif_scheme |  | fid |

---

## 预测方案F7-多语言表 t_diif_scheme_l

- **表名称：** 预测方案F7-多语言表
- **表名：** t_diif_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_diif_scheme_l |  | fpkid |
| 2 | idx_diif_scheme_l |  | fid,flocaleid |
