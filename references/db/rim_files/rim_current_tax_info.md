# 销项税额信息-rim_current_tax_info

## 销项税额信息-主表 t_rim_current_tax_info

- **表名称：** 销项税额信息-主表
- **表名：** t_rim_current_tax_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forg_id | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 6 | fsurplus_tax_amount | 预估上期留底税额 | numeric | 23 | 10 | √ | 0.0000000000 | 预估上期留底税额 |
| 7 | fsale_amount | 销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 销售额 |
| 8 | ftax_period | 所属账期 | timestamp | 0 |  |  | null | 所属账期 |
| 9 | fsale_tax_amount | 预估当期销项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 预估当期销项税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_current_tax_info |  | ftax_period,forg_id |
| 2 | pk_rim_current_tax_info |  | fid |
