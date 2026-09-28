# 业务组-pur_bizgroup

## 业务组-主表 t_pur_bizgroup

- **表名称：** 业务组-主表
- **表名：** t_pur_bizgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 6 | fparentid | 上级分组 | int8 | 64 |  | √ | 0 | 业务组 pur_bizgroup |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ffullname | ffullname | varchar | 255 |  | √ | ' ' |  |
| 9 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 10 | flongnumber | 长编码 | varchar | 50 |  | √ | ' ' | 长编码 |
| 11 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 12 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 14 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 1 :按管控单元逐级分配 2 :按管控单元自由分配 3 :按组织逐级分配 4 :按组织自由分配 5 :全局共享 6 :管控范围内共享 |
| 17 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 18 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 20 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 分组编码 | varchar | 30 |  | √ | ' ' | 分组编码 |
| 23 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 24 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_bizgroup_pkey |  | fid |
| 2 | idx_pur_bizgroup_fnumber |  | fnumber |

---

## 业务组-多语言表 t_pur_bizgroup_l

- **表名称：** 业务组-多语言表
- **表名：** t_pur_bizgroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 分组名称 | varchar | 100 |  | √ | ' ' | 分组名称 |
| 3 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_bizgroup_l_pkey |  | fpkid |
| 2 | idx_pur_bizgroup_l_fid |  | fid,flocaleid |
