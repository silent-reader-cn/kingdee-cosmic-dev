# 功能差异类型-xkfunc_diff_type

## 功能差异类型-多语言表 t_xk_func_diff_type_l

- **表名称：** 功能差异类型-多语言表
- **表名：** t_xk_func_diff_type_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 标题 | varchar | 500 |  | √ | ' ' | 标题 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xk_func_diff_type_l |  | fpkid |
| 2 | idx_diff_type_l_fid_flocaleid |  | fid,flocaleid |

---

## 功能差异类型-主表 t_xk_func_diff_type

- **表名称：** 功能差异类型-主表
- **表名：** t_xk_func_diff_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftitle | 标题 | varchar | 500 |  | √ | ' ' | 标题 |
| 3 | ftype | 差异类型 | varchar | 16 |  | √ | ' ' | 差异类型,枚举: DIFF_MENU :菜单差异 DIFF_BUSINESS :业务差异 |
| 4 | fguideid | 功能差异指引 | int8 | 64 |  | √ | 0 | [功能差异指引 xkfunc_diff_guide](../xkbase_files/xkfunc_diff_guide.md) |
| 5 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xk_func_diff_type |  | fid |
| 2 | idx_func_diff_type_fguideid |  | fguideid |
