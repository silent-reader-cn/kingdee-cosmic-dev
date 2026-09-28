# 数据源规则类型关联表-tctb_datasource_pkrules

## 数据源规则类型关联表-主表 t_tctb_datasource_pkrules

- **表名称：** 数据源规则类型关联表-主表
- **表名：** t_tctb_datasource_pkrules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 自定义数据源ID | int8 | 64 |  | √ | 0 | 自定义数据源ID |
| 2 | fbasedataid | 适用取数规则类型 | int8 | 64 |  | √ | 0 | 自定义数据源适用取数规则 tctb_datasource_peek_rule |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_datasource_pkrules_fk |  | fid |
| 2 | pk_tctb_datasource_pkrules |  | fpkid |
