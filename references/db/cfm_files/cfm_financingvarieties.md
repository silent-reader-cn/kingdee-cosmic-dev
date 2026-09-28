# 融资品种-cfm_financingvarieties

## 融资品种-多语言表 t_cfm_financingvarieties_l

- **表名称：** 融资品种-多语言表
- **表名：** t_cfm_financingvarieties_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 4 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 5 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_financingvarieties_l_pkey |  | fpkid |
| 2 | idx_t_cfm_financingvarieties_l |  | fid,flocaleid |

---

## 融资品种-主表 t_cfm_financingvarieties

- **表名称：** 融资品种-主表
- **表名：** t_cfm_financingvarieties

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fiswtdk | 是否委托贷款 | bpchar | 1 |  | √ | '0' | 是否委托贷款 |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 4 | fdescrible | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 6 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcredittype | 授信类别 | int8 | 64 |  | √ | 0 | [授信类别 cfm_credittype](../creditm_files/cfm_credittype.md) |
| 10 | fbiztype | 业务种类 | varchar | 80 |  | √ | ' ' | 业务种类,枚举: cfm :融资品种 ifm :存贷款产品 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenablerid | fenablerid | int8 | 64 |  | √ | 0 |  |
| 14 | ffinsource | 融资来源 | varchar | 30 |  | √ | ' ' | 融资来源,枚举: bank :银行市场 other :其它 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 17 | fcenterid | fcenterid | int8 | 64 |  | √ | 0 |  |
| 18 | floanterm | 贷款期限 | varchar | 50 |  | √ | ' ' | 贷款期限,枚举: short :短期 long :长期 |
| 19 | fparentid | 上级品种 | int8 | 64 |  | √ | 0 | [融资品种 cfm_financingvarieties](../cfm_files/cfm_financingvarieties.md) |
| 20 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 23 | flongnumber | 长编码 | varchar | 80 |  | √ | ' ' | 长编码 |
| 24 | fenabledate | fenabledate | timestamp | 0 |  |  | null |  |
| 25 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 26 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 27 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 29 | fcreditratio | 默认授信占比(%) | int4 | 32 |  | √ | 0 | 默认授信占比(%) |
| 30 | fperpetualbond | 永续债 | bpchar | 1 |  | √ | '0' | 永续债 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_financingvarieties_pkey |  | fid |
| 2 | idx_t_cfm_finvarieties_se |  | fstatus,fenable |
