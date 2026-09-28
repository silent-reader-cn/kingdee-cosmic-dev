# 模板样式规则配置-rdem_template_rule_style

## 模板样式规则配置-主表 t_rdem_template_rs

- **表名称：** 模板样式规则配置-主表
- **表名：** t_rdem_template_rs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ftemplateid | 模板配置 | int8 | 64 |  | √ | 0 | [模板配置 rdem_template](../rdem_files/rdem_template.md) |
| 4 | fstyleid | 样式规则 | int8 | 64 |  | √ | 0 | [样式规则 rdem_rule_style](../rdem_files/rdem_rule_style.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodelid | 体系 | int8 | 64 |  | √ | 0 | [体系管理 rdem_model](../rdem_files/rdem_model.md) |
| 7 | freportitemid | 报表项 | int8 | 64 |  | √ | 0 | [报表项 rdem_report_item](../rdem_files/rdem_report_item.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_template_rs |  | fid |
| 2 | idx_rdem_template_rs_m0 |  | fmodelid |
