# 评审信息-adm_examopinion

## 评审信息-主表 t_pur_regsupaudit

- **表名称：** 评审信息-主表
- **表名：** t_pur_regsupaudit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 供应商ID | int8 | 64 |  | √ | 0 | 供应商ID |
| 2 | fexamtime | 评审时间 | timestamp | 0 |  |  | null | 评审时间 |
| 3 | fexamerid | 评审人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fsrcbillno | 源单单号 | varchar | 80 |  | √ | ' ' | 源单单号 |
| 5 | fexamstatus | 评审结果 | bpchar | 1 |  | √ | ' ' | 评审结果,枚举: A :拟定 B :提交审批 C :审批通过 D :审批驳回 E :退回修改 |
| 6 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 7 | fexamnote | 评审意见 | varchar | 510 |  | √ | ' ' | 评审意见 |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fexamtype | 评审类型 | bpchar | 1 |  | √ | ' ' | 评审类型,枚举: 1 :注册审批 2 :资质审查 3 :现场评审 4 :样品确认 5 :物料试用 6 :供应商生效 7 :品类变更 8 :供应商退出 |
| 10 | fentryid | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |
| 11 | fsrctype | 源单类型 | varchar | 20 |  | √ | ' ' | 源单类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_regsupaudit_pkey |  | fentryid |
| 2 | idx_pur_regsupaudit_fid_fseq |  | fid,fseq |
