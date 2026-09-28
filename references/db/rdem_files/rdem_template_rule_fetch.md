# 模板取数规则配置-rdem_template_rule_fetch

## 模板取数规则配置-主表 t_rdem_template_rf

- **表名称：** 模板取数规则配置-主表
- **表名：** t_rdem_template_rf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ftemplateid | 模板配置 | int8 | 64 |  | √ | 0 | [模板配置 rdem_template](../rdem_files/rdem_template.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodelid | 体系 | int8 | 64 |  | √ | 0 | [体系管理 rdem_model](../rdem_files/rdem_model.md) |
| 6 | fformulaid | 取数规则 | int8 | 64 |  | √ | 0 | [取数规则 rdem_rule_fetch](../rdem_files/rdem_rule_fetch.md) |
| 7 | freportitemid | 报表项 | int8 | 64 |  | √ | 0 | [报表项 rdem_report_item](../rdem_files/rdem_report_item.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_template_rf |  | fid |
| 2 | idx_rdem_template_rf_m0 |  | fmodelid |
