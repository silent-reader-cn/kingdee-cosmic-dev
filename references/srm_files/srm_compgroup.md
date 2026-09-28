# 门户组件类型-srm_compgroup

## 门户组件类型-主表 t_pur_compgroup

- **表名称：** 门户组件类型-主表
- **表名：** t_pur_compgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 4 | fname | fname | varchar | 200 |  | √ | ' ' |  |
| 5 | fparentid | 上级组件 | int8 | 64 |  | √ | 0 | 门户组件类型 srm_compgroup |
| 6 | fcompobjectid | 组件业务对象 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ffullname | ffullname | varchar | 510 |  | √ | ' ' |  |
| 9 | flongnumber | 长编码 | varchar | 80 |  | √ | ' ' | 长编码 |
| 10 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 11 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fdescription | fdescription | varchar | 510 |  | √ | ' ' |  |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | varchar | 80 |  | √ | ' ' | 数据状态,枚举: A :保存 B :已提交 C :已审核 |
| 15 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fenable | 可用状态 | varchar | 80 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 20 | fissyspreset | 是否预置 | bpchar | 1 |  | √ | ' ' | 是否预置,枚举: 1 :是 0 :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_compgroup_pkey |  | fid |
| 2 | idx_pur_compgroup_fnumber |  | fstatus |
| 3 | idx_pur_compgroup_fctime |  | fcreatetime |

---

## 门户组件类型-多语言表 t_pur_compgroup_l

- **表名称：** 门户组件类型-多语言表
- **表名：** t_pur_compgroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 510 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 510 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_compgroup_l_pkey |  | fpkid |
| 2 | idx_pur_compgroup_l_fid |  | fid,flocaleid |
