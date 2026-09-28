# 归档分组-aef_archivegroup

## 归档分组-主表 t_aef_archivegroup

- **表名称：** 归档分组-主表
- **表名：** t_aef_archivegroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 4 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 5 | fparentid | 上级 | int8 | 64 |  | √ | 0 | 归档分组 aef_archivegroup |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ffullname | ffullname | varchar | 255 |  | √ | ' ' |  |
| 8 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aef_archivegroup |  | fnumber |
| 2 | pk_t_aef_archivegroup |  | fid |

---

## 归档分组-多语言表 t_aef_archivegroup_l

- **表名称：** 归档分组-多语言表
- **表名：** t_aef_archivegroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aef_archivegroup_l |  | fid,flocaleid |
| 2 | pk_t_aef_archivegroup_l |  | fpkid |
