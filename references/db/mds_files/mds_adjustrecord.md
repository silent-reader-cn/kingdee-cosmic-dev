# 状态调整记录-mds_adjustrecord

## 状态调整记录-主表 t_mds_adjustrecord

- **表名称：** 状态调整记录-主表
- **表名：** t_mds_adjustrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 4 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ffield | 字段 | varchar | 50 |  | √ | ' ' | 字段 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fafteradjstus | 调整后状态 | int8 | 64 |  | √ | 0 | 备货状态 mds_stockstatus |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fadjustreason | 调整原因 | varchar | 500 |  | √ | ' ' | 调整原因 |
| 11 | fbeforeadjstus | 调整前状态 | int8 | 64 |  | √ | 0 | 备货状态 mds_stockstatus |
| 12 | fplanid | 计划id | int8 | 64 |  | √ | 0 | 计划id |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fissystem | 是否系统 | bpchar | 1 |  | √ | '0' | 是否系统 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_adjustrecord |  | fid |
| 2 | idx_mds_adjustrecord |  | fplanid,fprojectid |
