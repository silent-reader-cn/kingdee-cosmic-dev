# 归档方案-bos_cbs_archi_plan

## 归档方案-多语言表 t_cbs_archi_plan_l

- **表名称：** 归档方案-多语言表
- **表名：** t_cbs_archi_plan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 50 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_archi_plan_l |  | fid,flocaleid |
| 2 | pk_cbs_archi_plan_l |  | fpkid |

---

## 归档方案-主表 t_cbs_archi_plan

- **表名称：** 归档方案-主表
- **表名：** t_cbs_archi_plan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 4 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [归档方案 bos_cbs_archi_plan](../cbs_files/bos_cbs_archi_plan.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | flongnumber | 长编码 | varchar | 50 |  | √ | ' ' | 长编码 |
| 7 | fsuffix | 方案后缀 | int8 | 64 |  | √ | 0 | 方案后缀 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | flogicsuffix | 逻辑库后缀 | varchar | 2 |  | √ | ' ' | 逻辑库后缀 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | farchiveroute | 目标归档库 | varchar | 50 |  | √ | ' ' | 目标归档库,枚举: scm_archive1 :SCM归档库1 scm_archive2 :SCM归档库2 fi_archive1 :FI归档库1 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_archi_plan |  | fid |
| 2 | idx_cbs_archi_plan |  | fnumber |
