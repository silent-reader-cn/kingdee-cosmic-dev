# 收费设置变更-src_feeconfigchg

## 收费设置变更-主表 t_src_feeconfigchg

- **表名称：** 收费设置变更-主表
- **表名：** t_src_feeconfigchg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 变更前信息摘要 | varchar | 510 |  | √ | ' ' | 变更前信息摘要 |
| 3 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 4 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 8 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 9 | fdocamount | 标书费(变更后) | numeric | 23 | 10 | √ | 0 | 标书费(变更后) |
| 10 | ffeewayid | 收费方式(变更后) | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 11 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | 寻源项目变更F7 src_bidchangef7 |
| 12 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 13 | ffeeamount | 投标保证金(变更后) | numeric | 23 | 10 | √ | 0 | 投标保证金(变更后) |
| 14 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | ffeeitemid | 收费项(变更后) | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 16 | fcurrencyid | 币别(变更后) | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_feeconfigchg_pid |  | fparentid |
| 2 | pk_src_feeconfigchg |  | fid |
| 3 | idx_src_feeconfigchg_proid |  | fprojectid |

---

## 标段分录-子表 t_src_feeconfigchgentry

- **表名称：** 标段分录-子表
- **表名：** t_src_feeconfigchgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpackdocamount | 标段标书费(变更后) | numeric | 23 | 10 | √ | 0 | 标段标书费(变更后) |
| 3 | ffeeamount | 标段投标保证金(变更后) | numeric | 23 | 10 | √ | 0 | 标段投标保证金(变更后) |
| 4 | fpackfeeitemid | 标段收费项(变更后) | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 5 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_feeconfigchgentry_fid |  | fid |
| 2 | pk_src_feeconfigchgentry |  | fentryid |
