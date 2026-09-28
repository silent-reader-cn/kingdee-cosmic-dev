# 中标供应商数量变更-src_winnumchg

## 中标供应商数量变更-主表 t_src_winnumchg

- **表名称：** 中标供应商数量变更-主表
- **表名：** t_src_winnumchg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 3 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fnewbiderqty | 最低邀请供应商数量(新) | int4 | 32 |  | √ | 0 | 最低邀请供应商数量(新) |
| 6 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 8 | fwinerqty | 中标供应商数量(原) | int4 | 32 |  | √ | 0 | 中标供应商数量(原) |
| 9 | fnewwinerqty | 中标供应商数量(新) | int4 | 32 |  | √ | 0 | 中标供应商数量(新) |
| 10 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 11 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | [寻源项目变更F7 src_bidchangef7](../pds_files/src_bidchangef7.md) |
| 12 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 13 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fbiderqty | 最低邀请供应商数量(原) | int4 | 32 |  | √ | 0 | 最低邀请供应商数量(原) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_winnumchg |  | fid |
| 2 | idx_src_winnumchg_pid |  | fparentid |
