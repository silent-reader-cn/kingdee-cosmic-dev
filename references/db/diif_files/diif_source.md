# 预测数据源-diif_source

## 预测数据源-主表 t_diif_source

- **表名称：** 预测数据源-主表
- **表名：** t_diif_source

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fapprovedate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 4 | fname | 数据源名称 | varchar | 50 |  | √ | ' ' | 数据源名称 |
| 5 | fbillformid | 单据界面 | varchar | 50 |  | √ | ' ' | 单据界面,枚举: sm_salorder :销售订单 sm_delivernotice :发货通知单 im_saloutbill :销售出库单 |
| 6 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | ffilterscheme | 过滤条件 | text | 0 |  |  | ' ' | 过滤条件 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' |  |
| 10 | fresultupdatetime | 结果集更新时间 | timestamp | 0 |  |  | null | 结果集更新时间 |
| 11 | fsource | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型,枚举: bill :单据界面 |
| 12 | fdatefield | 统计时间 | varchar | 50 |  | √ | ' ' | 统计时间,枚举: |
| 13 | fpricescheme | 预测单价取值 | varchar | 50 |  | √ | ' ' | 预测单价取值,枚举: LATESTPRICE :最新含税单价 PRICEBILL :价目表含税单价 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | ftype | 数据源类型 | varchar | 50 |  | √ | ' ' | 数据源类型,枚举: tradedata :交易数据 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fsys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 20 | fidsdatefield | 时间字段 | varchar | 50 |  | √ | ' ' | 时间字段 |
| 21 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 数据源编码 | varchar | 80 |  | √ | ' ' | 数据源编码 |
| 23 | ffilterschemename | 过滤方案 | varchar | 100 |  | √ | ' ' | 过滤方案 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_diif_source_number |  | fnumber |
| 2 | pk_t_diif_source |  | fid |

---

## 单据体-子表 t_diif_sourceresult

- **表名称：** 单据体-子表
- **表名：** t_diif_sourceresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillentryid | 单据分录id | int8 | 64 |  | √ | 0 | 单据分录id |
| 3 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pk_diif_sourceresult |  | fid |
| 2 | pk_t_diif_sourceresult |  | fentryid |

---

## 预测数据源-多语言表 t_diif_source_l

- **表名称：** 预测数据源-多语言表
- **表名：** t_diif_source_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 数据源名称 | varchar | 100 |  | √ | ' ' | 数据源名称 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_diif_source_l |  | fpkid |
| 2 | idx_diif_source_l |  | fid,flocaleid |
