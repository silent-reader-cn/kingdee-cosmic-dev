# 市场费用类型f7-ocdbd_expensetypef7

## 市场费用类型f7-主表 t_ocdbd_expensetype

- **表名称：** 市场费用类型f7-主表
- **表名：** t_ocdbd_expensetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexpenseitemid | fexpenseitemid | int8 | 64 |  | √ | 0 |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fisleaf | fisleaf | bpchar | 1 |  | √ | '1' |  |
| 5 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 6 | fparentid | fparentid | int8 | 64 |  | √ | 0 |  |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ffullname | ffullname | varchar | 1000 |  | √ | ' ' |  |
| 9 | flongnumber | flongnumber | varchar | 1000 |  | √ | ' ' |  |
| 10 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 11 | fexpensetype | fexpensetype | bpchar | 1 |  | √ | ' ' |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | flevel | flevel | int4 | 32 |  | √ | 0 |  |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fcontrol | 控制粒度 | varchar | 80 |  | √ | ' ' | 控制粒度,枚举: 1 :组织 2 :渠道 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 20 | fmustinputtype | fmustinputtype | bpchar | 1 |  | √ | 'C' |  |
| 21 | fifbudget | 是否启用预算 | bpchar | 1 |  | √ | '0' | 是否启用预算 |
| 22 | faccountid | faccountid | int8 | 64 |  | √ | 0 |  |
| 23 | ftypesign | ftypesign | bpchar | 1 |  | √ | 'C' |  |
| 24 | ffeecashtypeid | ffeecashtypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_expensetype_no |  | fnumber |
| 2 | pk_ocdbd_expensetype |  | fid |

---

## 市场费用类型f7-多语言表 t_ocdbd_expensetype_l

- **表名称：** 市场费用类型f7-多语言表
- **表名：** t_ocdbd_expensetype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | ffullname | ffullname | varchar | 1000 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 5 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_expensetypel_flid |  | fid,flocaleid |
| 2 | pk_ocdbd_expensetype_l |  | fpkid |
