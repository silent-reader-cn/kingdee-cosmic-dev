# 合并控制树-xkcr_treeview

## 合并控制树-主表 t_xkcr_treeview

- **表名称：** 合并控制树-主表
- **表名：** t_xkcr_treeview

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fcategory | 分类 | varchar | 10 |  | √ | ' ' | 分类 |
| 4 | fparameter | 参数 | varchar | 50 |  | √ | ' ' | 参数 |
| 5 | fvisible | 是否可见 | bpchar | 1 |  | √ | ' ' | 是否可见 |
| 6 | findex | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | fformtype | 单据类型 | varchar | 36 |  | √ | ' ' | 单据类型 |
| 9 | fnumber | 编码 | varchar | 36 |  | √ | ' ' | 编码 |
| 10 | fformid | 单据标识 | varchar | 36 |  | √ | ' ' | 单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_treeview |  | fid |
| 2 | idx_xkcr_treeview |  | findex |

---

## 合并控制树-多语言表 t_xkcr_treeview_l

- **表名称：** 合并控制树-多语言表
- **表名：** t_xkcr_treeview_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_treeview_l |  | fid,flocaleid |
| 2 | pk_xkcr_treeview_l |  | fpkid |
