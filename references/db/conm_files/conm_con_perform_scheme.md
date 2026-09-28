# 合同履行方案-conm_con_perform_scheme

## 合同履行方案-主表 t_conm_conperformscheme

- **表名称：** 合同履行方案-主表
- **表名：** t_conm_conperformscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 4 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 5 | forgdivide | 按组织隔离价格 | bpchar | 1 |  | √ | '1' | 按组织隔离价格 |
| 6 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fisndcontract | 匹配无明细合同 | bpchar | 1 |  | √ | '0' | 匹配无明细合同 |
| 12 | fbussinessentity | 采购业务单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 15 | fcontractsourceentity | 合同来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | freturnpattern | 价格返回方式 | varchar | 50 |  | √ | ' ' | 价格返回方式,枚举: A :仅返回最高优先级 B :全部返回 |
| 18 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 20 | fmatchcondition | 匹配合同范围条件 | varchar | 2000 |  | √ | ' ' | 匹配合同范围条件 |
| 21 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fcontrsourceconditon | 合同来源条件 | text | 0 |  |  | null | 合同来源条件 |
| 23 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fcombofield | 用途 | varchar | 50 |  | √ | ' ' | 用途,枚举: pur :采购 sal :销售 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_conperformscheme_m0 |  | fmasterid |
| 2 | pk_conm_conperformscheme |  | fid |

---

## 字段映射单据体-子表 t_conm_conperformentry

- **表名称：** 字段映射单据体-子表
- **表名：** t_conm_conperformentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fisconvert | 允许换算 | bpchar | 1 |  | √ | '0' | 允许换算 |
| 2 | fmatchpattern | 参与匹配方式 | varchar | 50 |  | √ | ' ' | 参与匹配方式,枚举: A :作为匹配条件 B :作为匹配结果 |
| 3 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 4 | fmatchbillsign | 匹配业务单据字段 | varchar | 50 |  | √ | ' ' | 匹配业务单据字段 |
| 5 | fsourcesign | 合同来源字段 | varchar | 50 |  | √ | ' ' | 合同来源字段 |
| 6 | fissumdimension | 合并价格取价维度 | bpchar | 1 |  | √ | '0' | 合并价格取价维度 |
| 7 | fmatchbillsignname | 匹配业务单据字段名 | varchar | 50 |  | √ | ' ' | 匹配业务单据字段名 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fdiscountsignisnull | 目标字段允许为空 | bpchar | 1 |  | √ | '0' | 目标字段允许为空 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fmatchflag | 比较符 | varchar | 50 |  | √ | ' ' | 比较符,枚举: A :等于 B :大于等于 C :大于 D :小于等于 E :小于 |
| 12 | fsourcesignname | 合同来源字段名 | varchar | 50 |  | √ | ' ' | 合同来源字段名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_conperformentry_fk |  | fid |
| 2 | pk_conm_conperformentry |  | fentryid |

---

## 合同优先级设置-子表 t_conm_contractsortentity

- **表名称：** 合同优先级设置-子表
- **表名：** t_conm_contractsortentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcesign | 合同来源字段 | varchar | 50 |  | √ | ' ' | 合同来源字段 |
| 3 | forder | 排序次序 | varchar | 50 |  | √ | ' ' | 排序次序,枚举: A :升序 B :降序 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_conm_contractsortentity |  | fentryid |
| 2 | idx_conm_contractsortentity_fk |  | fid |

---

## 合同履行方案-多语言表 t_conm_conperformscheme_l

- **表名称：** 合同履行方案-多语言表
- **表名：** t_conm_conperformscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 155 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 770 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_conm_conperformscheme_l |  | fpkid |
| 2 | idx_conm_conperformscheme_l_0 |  | fid,flocaleid |
