# 采购折扣服务-pm_purdiscountservice

## 字段映射单据体-子表 t_pm_purdiscountserentry

- **表名称：** 字段映射单据体-子表
- **表名：** t_pm_purdiscountserentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdiscountsign | 折扣单据字段 | varchar | 100 |  | √ | ' ' | 折扣单据字段 |
| 3 | fsourcesign | 折扣来源字段 | varchar | 100 |  | √ | ' ' | 折扣来源字段 |
| 4 | fdiscountsignname | 折扣单据字段 | varchar | 100 |  | √ | ' ' | 折扣单据字段 |
| 5 | fdiscountpattern | 参与折扣方式 | varchar | 5 |  | √ | ' ' | 参与折扣方式,枚举: A :作为折扣条件 B :作为折扣结果 C :作为折扣因素 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fdiscountsignisnull | 目标字段是否可以为空 | bpchar | 1 |  | √ | ' ' | 目标字段是否可以为空 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fsourcesignname | 折扣来源字段 | varchar | 100 |  | √ | ' ' | 折扣来源字段 |
| 10 | fmatchflag | 比较符 | varchar | 100 |  | √ | ' ' | 比较符,枚举: A :等于 B :大于等于 C :大于 D :小于等于 E :小于 F :等于（优先匹配可以为空） G :等于（按组织隔离为是） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pm_purdiscountserentry |  | fentryid |
| 2 | idx_pm_purdisserentry_fid |  | fid |

---

## 采购折扣服务-多语言表 t_pm_purdiscountser_l

- **表名称：** 采购折扣服务-多语言表
- **表名：** t_pm_purdiscountser_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
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
| 1 | idx_pm_purdisser_l |  | fid,flocaleid |
| 2 | pk_t_pm_purdiscountser_l |  | fpkid |

---

## 折扣排序-子表 t_pm_purdiscountsersort

- **表名称：** 折扣排序-子表
- **表名：** t_pm_purdiscountsersort

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsortsignname | 折扣表字段 | varchar | 100 |  | √ | ' ' | 折扣表字段 |
| 3 | fsortsign | 折扣表字段 | varchar | 100 |  | √ | ' ' | 折扣表字段 |
| 4 | forder | 排序次序 | varchar | 100 |  | √ | ' ' | 排序次序,枚举: A :升序 B :降序 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pm_purdiscountsersort |  | fentryid |
| 2 | idx_pm_purdissersort_fid |  | fid |

---

## 采购折扣服务-主表 t_pm_purdiscountser

- **表名称：** 采购折扣服务-主表
- **表名：** t_pm_purdiscountser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 6 | forgdivide | 按组织隔离 | bpchar | 1 |  | √ | '0' | 按组织隔离 |
| 7 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fdiscountentity | 目标单据 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fdiscountsrccondition | 折扣来源条件 | varchar | 2000 |  | √ | ' ' | 折扣来源条件 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fdiscountsourceentity | 折扣来源单据 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purdisser_fnumber |  | fnumber |
| 2 | pk_t_pm_purdiscountser |  | fid |
