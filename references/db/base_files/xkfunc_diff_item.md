# 功能差异项-xkfunc_diff_item

## 功能差异项-多语言表 t_xk_func_diff_item_l

- **表名称：** 功能差异项-多语言表
- **表名：** t_xk_func_diff_item_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fto | 目标值 | varchar | 2000 |  | √ | ' ' | 目标值 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdiffitem | 差异项 | varchar | 500 |  | √ | ' ' | 差异项 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | ffrom | 原始值 | varchar | 2000 |  | √ | ' ' | 原始值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_diff_item_fid_flocaleid |  | fid,flocaleid |
| 2 | pk_t_xk_func_diff_item_l |  | fpkid |

---

## 功能差异项-主表 t_xk_func_diff_item

- **表名称：** 功能差异项-主表
- **表名：** t_xk_func_diff_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fto | 目标值 | varchar | 2000 |  | √ | ' ' | 目标值 |
| 3 | ftypeid | 功能差异类型 | int8 | 64 |  | √ | 0 | [功能差异类型 xkfunc_diff_type](../xkbase_files/xkfunc_diff_type.md) |
| 4 | fgroupid | 差异项分组 | int8 | 64 |  | √ | 0 | [功能差异项分组 xkfunc_diff_item_gp](../xkbase_files/xkfunc_diff_item_gp.md) |
| 5 | fext | 额外字段（json） | text | 0 |  |  | null | 额外字段（json） |
| 6 | fop | 操作类型 | varchar | 10 |  | √ | ' ' | 操作类型,枚举: 0 :功能调整 1 :功能删除 2 :功能新增 |
| 7 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 8 | fdiffitem | 差异项 | varchar | 500 |  | √ | ' ' | 差异项 |
| 9 | ffrom | 原始值 | varchar | 2000 |  | √ | ' ' | 原始值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xk_func_diff_item |  | fid |
| 2 | idx_diff_item_fgpid_fseq |  | fgroupid,fseq |
| 3 | idx_diff_item_fop |  | fop |
| 4 | idx_diff_item_ftypeid_fseq |  | ftypeid,fseq |
