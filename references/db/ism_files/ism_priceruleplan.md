# 匹配维度配置-ism_priceruleplan

## 匹配维度配置-多语言表 t_ism_priceruleplan_l

- **表名称：** 匹配维度配置-多语言表
- **表名：** t_ism_priceruleplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ism_priceruleplan_l |  | fpkid |
| 2 | idx_t_ism_priceruleplan_l_id |  | fid,flocaleid |

---

## 取价规则字段配置-子表 t_ism_priceruleplan_e

- **表名称：** 取价规则字段配置-子表
- **表名：** t_ism_priceruleplan_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftargetfieldkey | 目标对象字段标识 | varchar | 100 |  | √ | ' ' | 目标对象字段标识 |
| 3 | ftargetfieldname | 目标对象字段名称 | varchar | 100 |  | √ | ' ' | 目标对象字段名称 |
| 4 | fgrouprelation | 分组关系 | int8 | 64 |  | √ | 0 | [数据分组关系 msmod_datagrouprelation](../mscommon_files/msmod_datagrouprelation.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpricerulefieldname | 源对象字段名称 | varchar | 100 |  | √ | ' ' | 源对象字段名称 |
| 7 | fdefinetype | 匹配类型 | varchar | 60 |  | √ | '0' | 匹配类型,枚举: 0 :直接匹配 1 :分组匹配 |
| 8 | fpricerulefieldkey | 源对象字段标识 | varchar | 100 |  | √ | ' ' | 源对象字段标识 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ism_priceruleplan_e |  | fentryid |
| 2 | idx_t_ism_priceruleplan_e_fid |  | fid |

---

## 匹配维度配置-主表 t_ism_priceruleplan

- **表名称：** 匹配维度配置-主表
- **表名：** t_ism_priceruleplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 60 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ftargetbill | 目标对象 | varchar | 72 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 8 | fenable | 使用状态 | varchar | 60 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 120 |  | √ | ' ' | 编码 |
| 10 | fsrcbillobj | 源对象 | varchar | 100 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ism_priceruleplan |  | fid |
| 2 | idx_t_ism_priceruleplan_fnum |  | fnumber |
