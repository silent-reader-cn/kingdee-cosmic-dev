# 任务标记-wf_taskmark

## 任务标记-多语言表 t_wf_taskmark_l

- **表名称：** 任务标记-多语言表
- **表名：** t_wf_taskmark_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | fcategoryname | 类别名称 | varchar | 100 |  | √ | ' ' | 类别名称 |
| 4 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_taskmark_l_pkey |  | fpkid |
| 2 | idx_wf_taskmark_l |  | fid,flocaleid |

---

## 任务标记-主表 t_wf_taskmark

- **表名称：** 任务标记-主表
- **表名：** t_wf_taskmark

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ficon | 显示图标 | varchar | 100 |  | √ | ' ' | 显示图标 |
| 3 | fvalue | 值 | varchar | 300 |  | √ | ' ' | 值 |
| 4 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 5 | fcategorynumber | 类别编码 | varchar | 100 |  | √ | ' ' | 类别编码 |
| 6 | fcategoryname | 类别名称 | varchar | 100 |  | √ | ' ' | 类别名称 |
| 7 | fcolor | 颜色 | varchar | 100 |  | √ | ' ' | 颜色 |
| 8 | fuserid | 用户id | int8 | 64 |  | √ | 0 | 用户id |
| 9 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_taskmark_catnumber |  | fcategorynumber |
| 2 | t_wf_taskmark_pkey |  | fid |
