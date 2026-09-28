# 招标项目时间变更-src_timechg

## 招标项目时间变更-主表 t_src_timechg

- **表名称：** 招标项目时间变更-主表
- **表名：** t_src_timechg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freplydate | 报名截止时间(变更前) | timestamp | 0 |  |  | null | 报名截止时间(变更前) |
| 3 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fnewaptitudedate | 资审截止时间(变更后) | timestamp | 0 |  |  | null | 资审截止时间(变更后) |
| 7 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 8 | fopendate | 预计开标时间(变更前) | timestamp | 0 |  |  | null | 预计开标时间(变更前) |
| 9 | fnewreplydate | 报名截止时间(变更后) | timestamp | 0 |  |  | null | 报名截止时间(变更后) |
| 10 | fnewplanopendate | 预计竞价开始时间(变更后) | timestamp | 0 |  |  | null | 预计竞价开始时间(变更后) |
| 11 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 12 | fplanopendate | 预计竞价开始时间(变更前) | timestamp | 0 |  |  | null | 预计竞价开始时间(变更前) |
| 13 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | [寻源项目变更F7 src_bidchangef7](../pds_files/src_bidchangef7.md) |
| 14 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 15 | faptitudedate | 资审截止时间(变更前) | timestamp | 0 |  |  | null | 资审截止时间(变更前) |
| 16 | fstopbiddate | 投标截止时间(变更前) | timestamp | 0 |  |  | null | 投标截止时间(变更前) |
| 17 | fnewopendate | 预计开标时间(变更后) | timestamp | 0 |  |  | null | 预计开标时间(变更后) |
| 18 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fprojectfid | 寻源项目F7 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 20 | fnewstopbiddate | 投标截止时间(变更后) | timestamp | 0 |  |  | null | 投标截止时间(变更后) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_timechg |  | fid |
| 2 | idx_src_timechg_pid |  | fparentid |
