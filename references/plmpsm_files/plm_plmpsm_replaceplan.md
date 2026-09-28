# 物料替代方案-plm_plmpsm_replaceplan

## 物料替代方案-使用范围表 t_bd_replaceplan_u

- **表名称：** 物料替代方案-使用范围表
- **表名：** t_bd_replaceplan_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_replaceplan_u |  | fdataid,fuseorgid |
| 2 | idx_t_bd_replaceplan_u_uo |  | fuseorgid |

---

## 替代物料-子表 t_bd_replaceplanentry_r

- **表名称：** 替代物料-子表
- **表名：** t_bd_replaceplanentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frepunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 3 | fisrep | 替代主料 | bpchar | 1 |  | √ | ' ' | 替代主料 |
| 4 | frepmole | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 5 | frepdeno | 基数 | numeric | 23 | 10 | √ | 0 | 基数 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | freppriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 8 | frepbomversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 9 | frepmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 10 | frepuseratio | 使用比例(%) | int8 | 64 |  | √ | 0 | 使用比例(%) |
| 11 | frepauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | frepeffectdate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 14 | frepinvaliddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_replaceplanentry_r_fid |  | fid |
| 2 | pk_bd_replaceplanentry_r |  | fentryid |

---

## 主物料-子表 t_bd_replaceplanentry_m

- **表名称：** 主物料-子表
- **表名：** t_bd_replaceplanentry_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmole | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | fuseratio | 使用比例(%) | int8 | 64 |  | √ | 0 | 使用比例(%) |
| 4 | fdeno | 基数 | numeric | 23 | 10 | √ | 0 | 基数 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 6 | fpriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fbomversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 11 | fisreplace | 替代主料 | bpchar | 1 |  | √ | ' ' | 替代主料 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_replaceplanentry_m_fid |  | fid |
| 2 | pk_bd_replaceplanentry_m |  | fentryid |

---

## 物料替代方案-多语言表 t_bd_replaceplan_l

- **表名称：** 物料替代方案-多语言表
- **表名：** t_bd_replaceplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_replaceplan_l |  | fid,flocaleid |
| 2 | pk_bd_replaceplan_l |  | fpkid |

---

## 物料替代方案-主表 t_bd_replaceplan

- **表名称：** 物料替代方案-主表
- **表名：** t_bd_replaceplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 14 | freplacemethod | 替代方式 | varchar | 30 |  | √ | ' ' | 替代方式,枚举: A :替代 B :取代 |
| 15 | fxkallocationtype | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: 1 :个性化 2 :共享型 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fname | 描述 | varchar | 60 |  | √ | ' ' | 描述 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fenableorid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | freplacestra | 替代策略 | varchar | 30 |  | √ | ' ' | 替代策略,枚举: 1001 :整批替代 1002 :混用替代 1003 :整批+混用 1004 :手工替代 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 23 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 24 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: BD :基础资料 PLM :研发物料管理 |
| 26 | fnumber | 替代编码 | varchar | 60 |  | √ | ' ' | 替代编码 |
| 27 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fdisableorid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_replaceplan_master |  | fmasterid |
| 2 | pk_bd_replaceplan |  | fid |
| 3 | idx_bd_replaceplan_org |  | fnumber,fcreateorgid |
| 4 | idx_t_bd_replaceplan_createorg |  | fcreateorgid |
| 5 | idx_bd_replaceplan_master |  | fmasterid |
| 6 | idx_bd_replaceplan_createorg |  | fcreateorgid |
