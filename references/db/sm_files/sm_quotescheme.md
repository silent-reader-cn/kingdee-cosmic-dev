# 取价方案-sm_quotescheme

## 字段映射单据体-子表 t_plat_quoteschemeentry

- **表名称：** 字段映射单据体-子表
- **表名：** t_plat_quoteschemeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisconvert | 允许换算 | bpchar | 1 |  | √ | '0' | 允许换算 |
| 3 | fquotesignname | 取价单据字段 | varchar | 100 |  | √ | ' ' | 取价单据字段 |
| 4 | fsourcesign | 价格来源字段 | varchar | 100 |  | √ | ' ' | 价格来源字段 |
| 5 | fquotepattern | 参与取价方式 | varchar | 5 |  | √ | ' ' | 参与取价方式,枚举: A :作为取价条件 B :作为取价结果 |
| 6 | fissumdimension | 合并价格取价维度 | bpchar | 1 |  | √ | '0' | 合并价格取价维度 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fsourcesignname | 价格来源字段 | varchar | 100 |  | √ | ' ' | 价格来源字段 |
| 10 | fquotesign | 取价单据字段 | varchar | 100 |  | √ | ' ' | 取价单据字段 |
| 11 | fmatchflag | 比较符 | varchar | 5 |  | √ | ' ' | 比较符,枚举: A :等于 B :大于等于 C :大于 D :小于等于 E :小于 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_plat_quoteschemeentry_pkey |  | fentryid |
| 2 | idx_plat_quotesche_fid |  | fid |

---

## 取价方案-多语言表 t_plat_quotescheme_l

- **表名称：** 取价方案-多语言表
- **表名：** t_plat_quotescheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plat_quotes_l_fid |  | fid,flocaleid |
| 2 | t_plat_quotescheme_l_pkey |  | fpkid |

---

## 价格排序-子表 t_plat_quotesortentry

- **表名称：** 价格排序-子表
- **表名：** t_plat_quotesortentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcesign | 价格来源字段 | varchar | 100 |  | √ | ' ' | 价格来源字段 |
| 3 | forder | 排序次序 | varchar | 5 |  | √ | ' ' | 排序次序,枚举: A :升序 B :降序 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsourcesignname | fsourcesignname | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_plat_quotesortentry_pkey |  | fentryid |
| 2 | idx_plat_quotesorte_fid |  | fid |

---

## 取价方案-主表 t_plat_quotescheme

- **表名称：** 取价方案-主表
- **表名：** t_plat_quotescheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpricesourceentity | 价格来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fquotesrccondition | 取价来源条件 | varchar | 2000 |  |  | null | 取价来源条件 |
| 4 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fquoteentity | 取价单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | forgdivide | 按组织隔离价格 | bpchar | 1 |  | √ | '0' | 按组织隔离价格 |
| 9 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fuse | 用途 | varchar | 5 |  | √ | ' ' | 用途,枚举: pur :采购 sal :销售 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 16 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | freturnpattern | 价格返回方式 | varchar | 5 |  | √ | ' ' | 价格返回方式,枚举: A :仅返回最高优先级 B :全部返回 |
| 20 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 22 | fctrlstrategy | fctrlstrategy | varchar | 5 |  | √ | ' ' |  |
| 23 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fquotecondition | 取价单据条件 | varchar | 2000 |  |  | null | 取价单据条件 |
| 25 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plat_quotes_fnumber |  | fnumber |
| 2 | t_plat_quotescheme_pkey |  | fid |
