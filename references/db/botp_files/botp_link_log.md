# 关联关系日志（废弃）-botp_link_log

## 关联关系日志（废弃）-主表 t_botp_link_log

- **表名称：** 关联关系日志（废弃）-主表
- **表名：** t_botp_link_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fttableid | 下游单主表编码 | int8 | 64 |  | √ | 0 | 下游单主表编码 |
| 3 | foptype | 操作类型 | bpchar | 1 |  | √ | '0' | 操作类型,枚举: 0 :下推 1 :选单 S :保存 B :提交 A :审核 D :删除 U :反审核 C :撤销 I :作废 V :反作废 |
| 4 | foperatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 5 | fstableid | 源单主表编码 | int8 | 64 |  | √ | 0 | 源单主表编码 |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fsbillno | 源单编号 | varchar | 200 |  | √ | ' ' | 源单编号 |
| 8 | ftbillid | 下游单内码 | int8 | 64 |  | √ | 0 | 下游单内码 |
| 9 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 10 | ftbillno | 下游单编号 | varchar | 200 |  | √ | ' ' | 下游单编号 |
| 11 | fsentitynumber | 源单类型 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 12 | fsid | 源单分录主键 | int8 | 64 |  | √ | 0 | 源单分录主键 |
| 13 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 14 | fitd | 下游单分录主键 | int8 | 64 |  | √ | 0 | 下游单分录主键 |
| 15 | ftentitynumber | 下游单据类型 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 16 | fdesc_tag | 描述_详情 | text | 0 |  |  | null | 描述_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_botp_link_log_fsbillno |  | fsbillno |
| 2 | pk_t_botp_link_log |  | fid |
| 3 | idx_t_botp_link_log_fsbillid |  | fsbillid |
| 4 | idx_t_botp_link_log_ftbillid |  | ftbillid |
| 5 | idx_t_botp_link_log_foperatetime |  | foperatetime |
| 6 | idx_t_botp_link_log_ftbillno |  | ftbillno |
