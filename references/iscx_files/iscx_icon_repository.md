# 图标库-iscx_icon_repository

## 图标库-主表 t_iscx_icon_repository

- **表名称：** 图标库-主表
- **表名：** t_iscx_icon_repository

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 150 |  |  | null | 名称 |
| 3 | ficon_url | 图标URL | varchar | 150 |  |  | null | 图标URL |
| 4 | fgroup | 分组 | varchar | 50 |  |  | null | 分组 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscx_icon_resp_g |  | fgroup |
| 2 | pk_t_iscx_icon_repository |  | fid |
