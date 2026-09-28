# 结算路径-ism_settlerelations

## 结算路径-主表 t_ism_settlerelations

- **表名称：** 结算路径-主表
- **表名：** t_ism_settlerelations

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialgroup | 物料分组 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 3 | fbulerelation | 正向结算路径 | int8 | 64 |  | √ | 0 | [结算路径 ism_settlerelations](../ism_files/ism_settlerelations.md) |
| 4 | ftransitonwer | 在途物权归属方 | varchar | 60 |  | √ | ' ' | 在途物权归属方,枚举: supplier :供应方结算组织 demand :需求方结算组织 |
| 5 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 60 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fdamagecostbear | 途损成本承担方 | varchar | 60 |  | √ | ' ' | 途损成本承担方,枚举: supplier :供应方结算组织 demand :需求方结算组织 |
| 11 | fmaterialgroupstand | 物料分组标准 | int8 | 64 |  | √ | 0 | [物料分类标准 bd_materialgroupstandard](../basedata_files/bd_materialgroupstandard.md) |
| 12 | ftooutgenerateplan | 对外单据生成方案 | int8 | 64 |  | √ | 0 | [内部单据生成方案 ism_botpconfig](../ism_files/ism_botpconfig.md) |
| 13 | fcostbear | 费用承担方 | varchar | 60 |  | √ | ' ' | 费用承担方,枚举: supplier :供应方结算组织 demand :需求方结算组织 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 18 | fsettleorg | 供应方业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fstarteffectivedate | 生效日期范围.开始 | timestamp | 0 |  |  | null | 生效日期范围.开始 |
| 20 | fowner | 需求方业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fprerelationid | 参考结算路径 | int8 | 64 |  | √ | 0 | [结算路径 ism_settlerelations](../ism_files/ism_settlerelations.md) |
| 22 | fgensequence | 对外单据生成时点 | bpchar | 1 |  | √ | 'B' | 对外单据生成时点,枚举: A :最先生成 B :最后生成 |
| 23 | fissys | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 24 | fenable | 使用状态 | varchar | 60 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fisdynapath | 动态路径 | bpchar | 1 |  | √ | '0' | 动态路径 |
| 26 | fnumber | 编码 | varchar | 120 |  | √ | ' ' | 编码 |
| 27 | fbizdirect | 业务方向 | bpchar | 1 |  | √ | 'B' | 业务方向,枚举: B :正向业务 R :反向业务 |
| 28 | fendeffectivedate | 生效日期范围.结束 | timestamp | 0 |  |  | null | 生效日期范围.结束 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ism_setlt_fno |  | fnumber |
| 2 | t_ism_settlerelations_pkey |  | fid |
| 3 | idx_ism_setlt_fsorg |  | fsettleorg |
| 4 | idx_ism_setlt_fown |  | fowner |

---

## 匹配条件.基本设置-子表 t_ism_settlerelation_mc

- **表名称：** 匹配条件.基本设置-子表
- **表名：** t_ism_settlerelation_mc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fright |  | varchar | 10 |  | √ | ' ' | ,枚举: ) :) )) :)) ))) :))) |
| 3 | fconditionvalue | 条件值 | varchar | 2000 |  | √ | ' ' | 条件值 |
| 4 | fconditionvaluestr | 条件值内容 | varchar | 255 |  | √ | ' ' | 条件值内容 |
| 5 | fleft |  | varchar | 10 |  | √ | ' ' | ,枚举: ( :( (( :(( ((( :((( |
| 6 | fconditiondimkey | 条件维度标识 | varchar | 100 |  | √ | ' ' | 条件维度标识 |
| 7 | fcomparison | 比较符 | varchar | 10 |  | √ | 'in' | 比较符,枚举: in :在…中 not in :不在...中 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fconditondimtext | 条件维度 | varchar | 100 |  | √ | ' ' | 条件维度 |
| 10 | flogic | 逻辑 | varchar | 5 |  | √ | 'and' | 逻辑,枚举: and :并且 or :或者 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fconditionvaluestr_tag | 条件值内容_详情 | text | 0 |  |  | null | 条件值内容_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ism_settlerelation_mc_pkey |  | fentryid |
| 2 | idx_ism_settlerelat_mc_id_eid |  | fid,fentryid |

---

## 结算路径-多语言表 t_ism_settlerelations_l

- **表名称：** 结算路径-多语言表
- **表名：** t_ism_settlerelations_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ism_setlt_l_flid |  | fid,flocaleid |
| 2 | t_ism_settlerelations_l_pkey |  | fpkid |

---

## 匹配条件.分类设置-子表 t_ism_settlerelation_gmc

- **表名称：** 匹配条件.分类设置-子表
- **表名：** t_ism_settlerelation_gmc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgleft |  | varchar | 10 |  | √ | ' ' | ,枚举: ( :( (( :(( ((( :((( |
| 3 | fgrouprelation | 分组关系 | int8 | 64 |  | √ | 0 | [数据分组关系 msmod_datagrouprelation](../mscommon_files/msmod_datagrouprelation.md) |
| 4 | fgconditiondimtext | 条件维度 | varchar | 100 |  | √ | ' ' | 条件维度 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fgright |  | varchar | 10 |  | √ | ' ' | ,枚举: ) :) )) :)) ))) :))) |
| 7 | fgconditionvalue | 分类值 | varchar | 2000 |  | √ | ' ' | 分类值 |
| 8 | fgconditionvaluestr | 分组值内容 | varchar | 255 |  | √ | ' ' | 分组值内容 |
| 9 | fgconditionvaluestr_tag | 分组值内容_详情 | text | 0 |  |  | null | 分组值内容_详情 |
| 10 | fglogic | 逻辑 | varchar | 5 |  | √ | 'and' | 逻辑,枚举: and :并且 or :或者 |
| 11 | fgconditiondimkey | 条件维度标识 | varchar | 100 |  | √ | ' ' | 条件维度标识 |
| 12 | fgcomparison | 比较符 | varchar | 10 |  | √ | 'in' | 比较符,枚举: in :在…中 not in :不在...中 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ism_settlerelation_gmc |  | fentryid |
| 2 | idx_ism_settlerelation_gmc_id |  | fid,fentryid |

---

## 结算价目表-多选基础资料表 t_ism_sr_settlepricelist

- **表名称：** 结算价目表-多选基础资料表
- **表名：** t_ism_sr_settlepricelist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [组织间结算价目表 ism_settlepricelist](../ism_files/ism_settlepricelist.md) |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_sr_settlepricelist |  | fpkid |
| 2 | idx_ism_sr_settlepricelist_fk |  | fdetailid |

---

## 结算路径明细-子表 t_ism_settlerelation_e

- **表名称：** 结算路径明细-子表
- **表名：** t_ism_settlerelation_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdemandwarehouse | 需求方仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 3 | fpricematchtype | 取价匹配方式_作废 | varchar | 60 |  | √ | '0' | 取价匹配方式_作废,枚举: 0 :来源单据匹配 1 :供应方单据匹配 2 :需求方单据匹配 |
| 4 | fdemandlocation | 需求方仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 5 | fbotpid | fbotpid | int8 | 64 |  | √ | 0 |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | finterorgsettlerule | 取价规则_作废 | int8 | 64 |  | √ | 0 | [结算取价规则 ism_interorgsettlerule](../ism_files/ism_interorgsettlerule.md) |
| 8 | fsupplierwarehouse | 供应方仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 9 | fsupplier | 供应方业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fdemand | 需求方业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fdemandwarehouseorg | 需求方库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fsuppliergenerateplan | 供应方内部单据生成方案 | int8 | 64 |  | √ | 0 | [内部单据生成方案 ism_botpconfig](../ism_files/ism_botpconfig.md) |
| 13 | fsupplierstoreorg | 供应方库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fdemandgenerateplan | 需求方内部单据生成方案 | int8 | 64 |  | √ | 0 | [内部单据生成方案 ism_botpconfig](../ism_files/ism_botpconfig.md) |
| 15 | fsaleorg | 供应方销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fissamecorporate | 是否同一法人 | bpchar | 1 |  | √ | '0' | 是否同一法人 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fpurorg | 需求方采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fsupplierlocation | 供应方仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ism_settlerelation_e_pkey |  | fentryid |
| 2 | idx_ism_settld_fsp |  | fsupplier |
| 3 | idx_ism_settld_fde |  | fdemand |

---

## 核算体系明细-子表 t_ism_settlerelation_d

- **表名称：** 核算体系明细-子表
- **表名：** t_ism_settlerelation_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | facctsysid | 会计核算体系 | int8 | 64 |  | √ | 0 | [核算体系 xkbd_accountingsys](../fibd_files/xkbd_accountingsys.md) |
| 2 | facctapsettleorg | 需求方结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | facctarsettleorg | 供应方结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | facctsettlepricerule | 取价规则 | int8 | 64 |  | √ | 0 | [结算取价规则 ism_interorgsettlerule](../ism_files/ism_interorgsettlerule.md) |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | facctpricematchtype | 取价匹配方式 | varchar | 30 |  | √ | ' ' | 取价匹配方式,枚举: 0 :来源单据匹配 1 :供应方单据匹配 2 :需求方单据匹配 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_settlerelation_d |  | fdetailid |
| 2 | idx_ism_settlerelation_d |  | fentryid |
