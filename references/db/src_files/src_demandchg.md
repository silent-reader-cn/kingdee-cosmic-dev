# 需求扩充-src_demandchg

## 标的分录-子表 t_src_demandchgentry

- **表名称：** 标的分录-子表
- **表名：** t_src_demandchgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 预估含税采购金额(变更前) | numeric | 23 | 10 | √ | 0 | 预估含税采购金额(变更前) |
| 3 | famount1 | 预估未税采购金额(变更后) | numeric | 23 | 10 | √ | 0 | 预估未税采购金额(变更后) |
| 4 | ftaxamount1 | 预估含税采购金额(变更后) | numeric | 23 | 10 | √ | 0 | 预估含税采购金额(变更后) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | famount | 预估未税采购金额(变更前) | numeric | 23 | 10 | √ | 0 | 预估未税采购金额(变更前) |
| 7 | fproject | 寻源项目 | varchar | 50 |  | √ | ' ' | 寻源项目 |
| 8 | fpurlistid | 标的ID | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_demandchgentry |  | fentryid |
| 2 | idx_src_demandchgentry_fid |  | fid |

---

## 需求扩充-主表 t_src_demandchg

- **表名称：** 需求扩充-主表
- **表名：** t_src_demandchg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | [寻源项目变更F7 src_bidchangef7](../pds_files/src_bidchangef7.md) |
| 3 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 4 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 7 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 9 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 10 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_demandchg_pid |  | fparentid |
| 2 | pk_src_demandchg |  | fid |
