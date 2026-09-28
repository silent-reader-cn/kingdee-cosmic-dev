# 专属前置机关联表-aqap_bank_login_rel

## 专属前置机关联表-主表 t_aqap_bank_login_rel

- **表名称：** 专属前置机关联表-主表
- **表名：** t_aqap_bank_login_rel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fconfig_type | 专属前置机类型 | varchar | 50 |  | √ | ' ' | 专属前置机类型,枚举: 仅支付 :仅支付 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fexclusive_number | 专属前置机编码 | varchar | 50 |  | √ | ' ' | 专属前置机编码 |
| 8 | fmaster_number | 主前置机编码 | varchar | 50 |  | √ | ' ' | 主前置机编码 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 11 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_bank_login_rel_pkey |  | fid |
| 2 | idx_aqap_banklogin_rel |  | fmaster_number,fexclusive_number |
