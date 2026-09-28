# 标包与标的F7-src_bidpackagef7

## 关联的标的-多选基础资料表 t_src_packagepurlist

- **表名称：** 关联的标的-多选基础资料表
- **表名：** t_src_packagepurlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_packagepurlist |  | fpkid |
| 2 | idx_src_packagepurlist_eid |  | fentryid |

---

## 标包与标的F7-主表 t_src_packageentry

- **表名称：** 标包与标的F7-主表
- **表名：** t_src_packageentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 3 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fpackagename | 标包名称 | varchar | 100 |  | √ | ' ' | 标包名称 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryparentid | 父单据ID(寻源项目ID) | varchar | 50 |  | √ | ' ' | 父单据ID(寻源项目ID) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_packageentry_fid |  | fid |
| 2 | pk_src_packageentry |  | fentryid |
| 3 | idx_src_packageentry_pid |  | fentryparentid |
