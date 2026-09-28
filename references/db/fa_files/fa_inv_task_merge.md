# 盘点任务合并-fa_inv_task_merge

## 单据体-子表 t_fa_inv_tm_entry

- **表名称：** 单据体-子表
- **表名：** t_fa_inv_tm_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finventorytaskid | 盘点任务 | int8 | 64 |  | √ | 0 | [我的盘点任务 fa_inventory_task](../fa_files/fa_inventory_task.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | finventsscopeid | 盘点范围 | int8 | 64 |  | √ | 0 | [盘点范围(原我的盘点任务) fa_inventory_sope](../fa_files/fa_inventory_sope.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fa_inv_tm_entry |  | fentryid |
| 2 | idx_fa_inv_tm_entry_taskid |  | fid,finventorytaskid |

---

## 盘点任务合并-多语言表 t_fa_inv_task_merge_l

- **表名称：** 盘点任务合并-多语言表
- **表名：** t_fa_inv_task_merge_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | int8 | 64 |  | √ | 0 | localeid |
| 4 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fa_inv_task_merge_l |  | fid,flocaleid |
| 2 | pk_t_fa_inv_task_merge_l |  | fpkid |

---

## 盘点任务合并-主表 t_fa_inv_task_merge

- **表名称：** 盘点任务合并-主表
- **表名：** t_fa_inv_task_merge

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finventorychecker | 盘点人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | finventschemeid | 盘点方案 | int8 | 64 |  | √ | 0 | [盘点方案 fa_inventscheme_new](../fa_files/fa_inventscheme_new.md) |
| 4 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fa_inv_task_merge |  | fid |
| 2 | idx_fa_inv_tm_schemeid |  | finventschemeid |
