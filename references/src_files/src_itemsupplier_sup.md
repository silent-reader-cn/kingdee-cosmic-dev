# 标的供应商(后台元数据)-src_itemsupplier_sup

## 标的供应商(后台元数据)-主表 t_src_itemsupentry_sup

- **表名称：** 标的供应商(后台元数据)-主表
- **表名：** t_src_itemsupentry_sup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | FBasedataId | int8 | 64 |  | √ | 0 | FBasedataId |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |
| 3 | fentryid | FEntryId | int8 | 64 |  | √ | 0 | FEntryId |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_itemsupentry_sup_fid |  | fentryid |
| 2 | pk_src_itemsupentry_sup |  | fpkid |
