# 单据配置-ccm_entityconfig

## 单据配置-主表 t_ccm_entityconfig

- **表名称：** 单据配置-主表
- **表名：** t_ccm_entityconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 50 |  | √ | ' ' | id |
| 2 | flinetypekey | 行类型字段 | varchar | 50 |  | √ | ' ' | 行类型字段 |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fplugintype | 插件类型 | varchar | 10 |  | √ | ' ' | 插件类型,枚举: java :java ks :ks |
| 5 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 8 | fjsonvalue | 当前配置json值 | text | 0 |  |  | null | 当前配置json值 |
| 9 | fdefaultvalue | 预设值 | text | 0 |  |  | ' ' | 预设值 |
| 10 | fispre | 是否预设 | bpchar | 1 |  | √ | '0' | 是否预设 |
| 11 | fplugin | 插件 | varchar | 100 |  | √ | ' ' | 插件 |
| 12 | fccmunsettlecount | 信用未结批数字段 | varchar | 50 |  | √ | ' ' | 信用未结批数字段 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fccmexcessdays | 预估信用超标天数字段 | varchar | 50 |  | √ | ' ' | 预估信用超标天数字段 |
| 16 | fbaseunitkey | 基本单位字段 | varchar | 50 |  | √ | ' ' | 基本单位字段 |
| 17 | fccmexcessamount | 预估信用超标额度字段 | varchar | 50 |  | √ | ' ' | 预估信用超标额度字段 |
| 18 | fdatekey | 日期字段 | varchar | 50 |  | √ | ' ' | 日期字段 |
| 19 | fbaseqtykey | 基本单位数量字段 | varchar | 50 |  | √ | ' ' | 基本单位数量字段 |
| 20 | fccmexcessoveramount | 预估信用超标逾期额度字段 | varchar | 50 |  | √ | ' ' | 预估信用超标逾期额度字段 |
| 21 | fcurrencykey | 币种字段 | varchar | 30 |  | √ | ' ' | 币种字段 |
| 22 | fccmexcessbillamount | 预估信用超标单笔限额字段 | varchar | 50 |  | √ | ' ' | 预估信用超标单笔限额字段 |
| 23 | flkentrykey | 关联实体标识 | varchar | 50 |  | √ | ' ' | 关联实体标识 |
| 24 | fenable | 使用状态 | varchar | 5 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fccmupdatetime | 预估信用超标更新时点字段 | varchar | 50 |  | √ | ' ' | 预估信用超标更新时点字段 |
| 26 | fnumber | 单据标识 | varchar | 50 |  | √ | ' ' | 单据标识 |
| 27 | fisredbillkey | 是否红单字段 | varchar | 50 |  | √ | ' ' | 是否红单字段 |
| 28 | forgkey | 信控组织字段 | varchar | 30 |  | √ | ' ' | 信控组织字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_ec_fnumber |  | fnumber |
| 2 | t_ccm_entityconfig_pkey |  | fid |

---

## 维度映射分录-子表 t_ccm_ec_dimensions

- **表名称：** 维度映射分录-子表
- **表名：** t_ccm_ec_dimensions

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 50 |  | √ | ' ' |  |
| 2 | froleid | 维度成员 | int8 | 64 |  | √ | 0 | [维度成员 ccm_role](../ccm_files/ccm_role.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | frolekey | 映射字段 | varchar | 50 |  | √ | ' ' | 映射字段 |
| 5 | fentryid | fentryid | varchar | 50 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_ecd_pk |  | fid |
| 2 | t_ccm_ec_dimensions_pkey |  | fentryid |

---

## 字段分录-子表 t_ccm_ec_selectors

- **表名称：** 字段分录-子表
- **表名：** t_ccm_ec_selectors

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 50 |  | √ | ' ' |  |
| 2 | ffield | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | varchar | 50 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ccm_ec_selectors_pkey |  | fentryid |
| 2 | idx_ccm_ecs_pk |  | fid |

---

## 额度映射分录-子表 t_ccm_ec_quotatypes

- **表名称：** 额度映射分录-子表
- **表名：** t_ccm_ec_quotatypes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 50 |  | √ | ' ' |  |
| 2 | fquotatypekey | 映射字段 | varchar | 50 |  | √ | ' ' | 映射字段 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fquotatypeid | 信用检查范围 | int8 | 64 |  | √ | 0 | [（废弃）信用控制形式 ccm_checktype](../ccm_files/ccm_checktype.md) |
| 5 | fentryid | fentryid | varchar | 50 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ccm_ec_quotatypes_pkey |  | fentryid |
| 2 | idx_ccm_ecq_pk |  | fid |

---

## 单据配置-多语言表 t_ccm_entityconfig_l

- **表名称：** 单据配置-多语言表
- **表名：** t_ccm_entityconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 50 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ccm_entityconfig_l_pkey |  | fpkid |
| 2 | idx_ccm_ec_fid_flocale |  | fid,flocaleid |
