# 检修工序计划派工日志(废弃)-sfc_mromanuftechlog

## 检修工序计划派工日志(废弃)-主表 t_sfc_mromanuftechlog

- **表名称：** 检修工序计划派工日志(废弃)-主表
- **表名：** t_sfc_mromanuftechlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanbillentryid | 检修工序计划分录ID | varchar | 50 |  | √ | ' ' | 检修工序计划分录ID |
| 3 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 4 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 5 | fmanbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 6 | fmanoprno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 7 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 8 | fmanbillid | 检修工序计划ID | varchar | 50 |  | √ | ' ' | 检修工序计划ID |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_mromanuftechlog |  | fid |
| 2 | idx_mrolog_fmanbillentryid |  | fmanbillentryid |

---

## 单据体-子表 t_sfc_mromanlogentry

- **表名称：** 单据体-子表
- **表名：** t_sfc_mromanlogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassignor | 派工人 | varchar | 255 |  | √ | ' ' | 派工人 |
| 3 | fassignor_tag | 派工人_详情 | text | 0 |  |  | null | 派工人_详情 |
| 4 | fplanbegintime | 计划开始时间 | varchar | 50 |  | √ | ' ' | 计划开始时间 |
| 5 | freceiver | 接收人 | varchar | 255 |  | √ | ' ' | 接收人 |
| 6 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fchangetime | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 8 | freceiver_tag | 接收人_详情 | text | 0 |  |  | null | 接收人_详情 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fplanendtime | 计划完工时间 | varchar | 50 |  | √ | ' ' | 计划完工时间 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_mromanlogentry |  | fentryid |
| 2 | idx_sfc_mromanlogentry_fk |  | fid |
