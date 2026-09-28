# 功能差异项分组-xkfunc_diff_item_gp

## 功能差异项分组-多语言表 t_xk_func_diff_item_gp_l

- **表名称：** 功能差异项分组-多语言表
- **表名：** t_xk_func_diff_item_gp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 分组名称 | varchar | 255 |  | √ | ' ' | 分组名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xk_func_diff_item_gp_l |  | fpkid |
| 2 | idx_diff_item_gp_fid |  | fid |

---

## 功能差异项分组-主表 t_xk_func_diff_item_gp

- **表名称：** 功能差异项分组-主表
- **表名：** t_xk_func_diff_item_gp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 分组名称 | varchar | 255 |  | √ | ' ' | 分组名称 |
| 3 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xk_func_diff_item_gp |  | fid |
| 2 | idx_t_diff_item_gp_fseq |  | fseq |
