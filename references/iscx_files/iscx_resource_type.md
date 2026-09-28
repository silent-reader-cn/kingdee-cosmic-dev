# 资源类型-iscx_resource_type

## 资源类型-主表 t_iscx_res_type

- **表名称：** 资源类型-主表
- **表名：** t_iscx_res_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fname | 名称 | varchar | 150 |  |  | null | 名称 |
| 3 | for_module | 用于模块 | bpchar | 1 |  |  | null | 用于模块 |
| 4 | ficon_url | 图片url | varchar | 255 |  |  | null | 图片url |
| 5 | for_common | 用于公共资源 | bpchar | 1 |  |  | null | 用于公共资源 |
| 6 | fgroup | 分组 | varchar | 50 |  |  | null | 分组 |
| 7 | fpriority | 顺序号 | int8 | 64 |  |  | null | 顺序号 |
| 8 | for_solution | 用于解决方案 | bpchar | 1 |  |  | null | 用于解决方案 |
| 9 | fnumber | 编码 | varchar | 30 |  |  | null | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscx_res_type |  | fid |
| 2 | idx_isc_res_type_n |  | fnumber |

---

## 资源类型-多语言表 t_iscx_res_type_l

- **表名称：** 资源类型-多语言表
- **表名：** t_iscx_res_type_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 150 |  |  | null | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscx_res_type_l |  | fpkid |
| 2 | idx_iscx_res_type_l_0 |  | fid |
