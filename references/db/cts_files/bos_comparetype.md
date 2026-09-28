# 比较符自定义-bos_comparetype

## 比较符自定义-多语言表 t_bas_comparetypes_l

- **表名称：** 比较符自定义-多语言表
- **表名：** t_bas_comparetypes_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 200 |  |  | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_comparetypes_l_fid |  | fid,flocaleid |
| 2 | t_bas_comparetypes_l_pkey |  | fpkid |

---

## 应用-多选基础资料表 t_bas_comparetypeapps

- **表名称：** 应用-多选基础资料表
- **表名：** t_bas_comparetypeapps

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_comparetypeapps_bdid |  | fbasedataid |
| 2 | t_bas_comparetypeapps_pkey |  | fpkid |

---

## 比较符自定义-主表 t_bas_comparetypes

- **表名称：** 比较符自定义-主表
- **表名：** t_bas_comparetypes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | fname | varchar | 200 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | ffield | 适用类型 | int8 | 64 |  | √ | 0 | [比较符适用类型 bos_comparetypefield](../cts_files/bos_comparetypefield.md) |
| 6 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 7 | finputtype | 录入形式 | varchar | 20 |  | √ | ' ' | 录入形式,枚举: INTEGER :整数 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcontantclass | 解析类 | varchar | 200 |  | √ | ' ' | 解析类 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fneedinput | 值录入 | bpchar | 1 |  | √ | '0' | 值录入 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | fforbiddate | fforbiddate | timestamp | 0 |  |  | null |  |
| 17 | fforbidderid | fforbidderid | int8 | 64 |  | √ | 0 |  |
| 18 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_comparetypes_pkey |  | fid |
| 2 | idx_bas_comparetypes_fnumber |  | fnumber |
