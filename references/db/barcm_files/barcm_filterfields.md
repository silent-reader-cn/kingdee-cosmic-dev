# PDA选单过滤字段-barcm_filterfields

## PDA选单过滤字段-多语言表 t_barcm_filterfields_l

- **表名称：** PDA选单过滤字段-多语言表
- **表名：** t_barcm_filterfields_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 450 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 备注 | varchar | 600 |  | √ | ' ' | 备注 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_barcm_filterfields_l |  | fpkid |
| 2 | barcm_filterfields_l_idx |  | fid,flocaleid |

---

## PDA选单过滤字段-主表 t_barcm_filterfields

- **表名称：** PDA选单过滤字段-主表
- **表名：** t_barcm_filterfields

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ffieldname | 字段名 | varchar | 100 |  | √ | ' ' | 字段名 |
| 6 | ffilteralias | 过滤字段 | varchar | 50 |  | √ | ' ' | 过滤字段,枚举: |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ffieldkey | 字段标识 | varchar | 200 |  | √ | ' ' | 字段标识 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ffiledpath | 字段长路径 | varchar | 500 |  | √ | ' ' | 字段长路径 |
| 13 | ffieldtype | 字段类型 | varchar | 100 |  | √ | ' ' | 字段类型 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 150 |  | √ | ' ' | 编码 |
| 16 | fdesc | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 17 | fentityid | 实体 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 18 | fisdefault | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 19 | fdatatype | 基础资料类型 | varchar | 100 |  | √ | ' ' | 基础资料类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_barcm_filterfields |  | fid |
| 2 | barcm_filterfields_e_idx |  | fentityid |
| 3 | barcm_filterfields_n_idx |  | fnumber |
