# EAI凭证拉取规则(五菱)-fpy_voucherconversio

## EAI凭证拉取规则(五菱)-主表 tk_fpy_voucherconversios

- **表名称：** EAI凭证拉取规则(五菱)-主表
- **表名：** tk_fpy_voucherconversios

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fk_lhqb_period | period | varchar | 50 |  | √ | ' ' | period |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fk_lhqb_checkboxfield | 按小时查询 | bpchar | 1 |  | √ | '0' | 按小时查询 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fk_lhqb_organizationno | organizationNo | varchar | 50 |  | √ | ' ' | organizationNo |
| 9 | fk_lhqb_combofield | 同步状态 | varchar | 50 |  | √ | ' ' | 同步状态,枚举: A :未同步 B :已同步 |
| 10 | fk_lhqb_textfield | day | varchar | 50 |  | √ | ' ' | day |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fk_lhqb_textfield1 | 查询日期 | varchar | 50 |  | √ | ' ' | 查询日期 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__fpy_voucherconversios |  | fid |
