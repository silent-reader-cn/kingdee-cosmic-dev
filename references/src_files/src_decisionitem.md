# 场景关联标的(后台元数据)-src_decisionitem

## 场景关联标的(后台元数据)-主表 t_src_decisionitem

- **表名称：** 场景关联标的(后台元数据)-主表
- **表名：** t_src_decisionitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | 标的ID | int8 | 64 |  | √ | 0 | 标的ID |
| 2 | fpkid | FPKID | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | 场景分录ID | int8 | 64 |  | √ | 0 | 场景分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_decisionitem |  | fpkid |
| 2 | idx_src_decisionitem_bid |  | fbasedataid |
| 3 | idx_src_decisionitem_fid |  | fentryid |
