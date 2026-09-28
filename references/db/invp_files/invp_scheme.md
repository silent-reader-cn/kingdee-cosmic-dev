# 库存计划方案-invp_scheme

## 库存计划方案-多语言表 t_invp_scheme_l

- **表名称：** 库存计划方案-多语言表
- **表名：** t_invp_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_scheme_l |  | fid,flocaleid |
| 2 | pk_t_invp_scheme_l |  | fpkid |

---

## 库存计划方案-使用范围表 t_invp_scheme_u

- **表名称：** 库存计划方案-使用范围表
- **表名：** t_invp_scheme_u

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
| 1 | pk_t_invp_scheme_u |  | fdataid,fuseorgid |
| 2 | idx_t_invp_scheme_u_uo |  | fuseorgid |

---

## 供应参数分录-子表 t_invp_supparamentry

- **表名称：** 供应参数分录-子表
- **表名：** t_invp_supparamentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finsupcal | 参与运算 | bpchar | 1 |  | √ | '0' | 参与运算 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fsupplydatasrcid | 供应单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_invp_supparamentry |  | fentryid |
| 2 | idx_invp_supparamentry |  | fid |

---

## 仓库范围分录-子表 t_invp_warehousparamentry

- **表名称：** 仓库范围分录-子表
- **表名：** t_invp_warehousparamentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fwarehouseid | 仓库编码 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invp_warehousparamentry |  | fentryid |
| 2 | idx_invp_warehousparamentry |  | fid |

---

## 物料范围分录-子表 t_invp_materialparamentry

- **表名称：** 物料范围分录-子表
- **表名：** t_invp_materialparamentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_materialparamentry |  | fid |
| 2 | pk_invp_materialparamentry |  | fentryid |

---

## 组织范围分录-子表 t_invp_orgparamentry

- **表名称：** 组织范围分录-子表
- **表名：** t_invp_orgparamentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrydemandorgid | 编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fentrysupplypolicyid | 即时库存供应策略 | int8 | 64 |  | √ | 0 | [即时库存供应策略 invp_supply_policy](../invp_files/invp_supply_policy.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | finnersupplyrelationid | 内部供应关系 | int8 | 64 |  | √ | 0 | [内部供应关系 invp_supplyrelation_inner](../invp_files/invp_supplyrelation_inner.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_invp_orgparamentry |  | fentryid |
| 2 | idx_invp_orgparamentry |  | fid |

---

## 需求优先级分录-子表 t_invp_dempriorityentry

- **表名称：** 需求优先级分录-子表
- **表名：** t_invp_dempriorityentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forderfield | 排序字段 | varchar | 50 |  | √ | ' ' | 排序字段,枚举: demanddate :需求日期 org :需求组织 demandwarehouse :需求仓库 materiel :物料 srcbill :来源单据 billno :来源单据编码 |
| 3 | fdemcolname | fdemcolname | varchar | 255 |  | √ | ' ' |  |
| 4 | fdemandentityid | fdemandentityid | varchar | 50 |  | √ | ' ' |  |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fdemcolsign | fdemcolsign | varchar | 255 |  | √ | ' ' |  |
| 8 | fsorttype | 排序方式 | varchar | 10 |  | √ | ' ' | 排序方式,枚举: asc :升序 desc :降序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_invp_dempriorityentry |  | fentryid |
| 2 | idx_invp_dempriorityentry |  | fid |

---

## 需求参数分录-子表 t_invp_demparamentry

- **表名称：** 需求参数分录-子表
- **表名：** t_invp_demparamentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdemandsrcid | 需求单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | findemcal | 参与运算 | bpchar | 1 |  | √ | '0' | 参与运算 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_invp_demparamentry |  | fentryid |
| 2 | idx_invp_demparamentry |  | fid |

---

## 库存计划方案-主表 t_invp_scheme

- **表名称：** 库存计划方案-主表
- **表名：** t_invp_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funiontype | funiontype | varchar | 30 |  | √ | ' ' |  |
| 3 | fleadtimelackasc | 提前期不足正排 | bpchar | 1 |  | √ | ' ' | 提前期不足正排 |
| 4 | fsupplymodelid | 供应来源模型 | int8 | 64 |  | √ | 0 | [资源注册模型 invp_model_register](../invp_files/invp_model_register.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmergecondition | 计划建议合并条件 | varchar | 100 |  | √ | ' ' | 计划建议合并条件,枚举: org :需求组织 material :物料 advicetype :建议类型 |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fallowadvanceperiod | 允许提前期 | int4 | 32 |  | √ | 0 | 允许提前期 |
| 11 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 12 | fhistorysupplydays | 供应天数 | int4 | 32 |  | √ | 0 | 供应天数 |
| 13 | fhistorydemand | 历史需求 | varchar | 50 |  | √ | '0' | 历史需求,枚举: 0 :所有历史需求 1 :历史需求天数 |
| 14 | fallowdelaytime | fallowdelaytime | int4 | 32 |  | √ | 0 |  |
| 15 | fexcursiondays | fexcursiondays | int4 | 32 |  | √ | 0 |  |
| 16 | fdemtolevelmapping | 需求与水位匹配维度 | int8 | 64 |  | √ | 0 | [匹配映射配置 invp_matchmapping_config](../invp_files/invp_matchmapping_config.md) |
| 17 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 18 | fsuptodemmapping | 供需匹配维度 | int8 | 64 |  | √ | 0 | [匹配映射配置 invp_matchmapping_config](../invp_files/invp_matchmapping_config.md) |
| 19 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fhistorydemanddays | 需求天数 | int4 | 32 |  | √ | 0 | 需求天数 |
| 22 | fadvicestatus | 计划建议状态 | bpchar | 1 |  | √ | ' ' | 计划建议状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fmaterialrange | 物料范围 | varchar | 50 |  | √ | '0' | 物料范围,枚举: 0 :全部物料 1 :指定物料 |
| 24 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 26 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 27 | fdimension | 库存水位维度 | int8 | 64 |  | √ | 0 | [库存水位维度 invp_leveldimension](../invp_files/invp_leveldimension.md) |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | finvlevelfilter_tag | finvlevelfilter_tag | text | 0 |  |  | null |  |
| 30 | finvlevelfilter | finvlevelfilter | varchar | 255 |  | √ | ' ' |  |
| 31 | foperatorid | foperatorid | int8 | 64 |  | √ | 0 |  |
| 32 | falgorithmplanid | 算法方案 | int8 | 64 |  | √ | 0 | [算法方案配置 invp_algoconfig](../invp_files/invp_algoconfig.md) |
| 33 | fsupdelayday | fsupdelayday | int4 | 32 |  | √ | 0 |  |
| 34 | foutofdate | foutofdate | varchar | 50 |  | √ | ' ' |  |
| 35 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 36 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 38 | fupdateinvlevel | fupdateinvlevel | bpchar | 1 |  | √ | ' ' |  |
| 39 | fscoutofdate | fscoutofdate | varchar | 50 |  | √ | ' ' |  |
| 40 | forgshare | 组织间共享 | bpchar | 1 |  | √ | '0' | 组织间共享 |
| 41 | fplangroup | 计划组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 42 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 43 | fcreateorgid | 计划组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 46 | fdemandmodelid | 需求来源模型 | int8 | 64 |  | √ | 0 | [资源注册模型 invp_model_register](../invp_files/invp_model_register.md) |
| 47 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 48 | foperatorgroupid | foperatorgroupid | int8 | 64 |  | √ | 0 |  |
| 49 | fallowleadtime | fallowleadtime | int4 | 32 |  | √ | 0 |  |
| 50 | fwarehouserange | 仓库范围 | varchar | 50 |  | √ | '0' | 仓库范围,枚举: 0 :全部仓库 1 :指定仓库 |
| 51 | fplanadvicemapid | 计划建议映射 | int8 | 64 |  | √ | 0 | [通用映射配置 sbs_billfieldmapping](../mscommon_files/sbs_billfieldmapping.md) |
| 52 | fplanner | 计划员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 53 | finvlevelid | finvlevelid | int8 | 64 |  | √ | 0 |  |
| 54 | fplanoutlook | 展望期 | int4 | 32 |  | √ | 0 | 展望期 |
| 55 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 7 :私有 |
| 56 | fperioddays | fperioddays | int4 | 32 |  | √ | 0 |  |
| 57 | fmainplantype | 计划类型 | bpchar | 1 |  | √ | 'A' | 计划类型,枚举: A :再订货点 B :最大最小 E :安全库存 |
| 58 | fperiodtype | fperiodtype | varchar | 30 |  | √ | ' ' |  |
| 59 | fautoauditplanadv | 自动投放 | bpchar | 1 |  | √ | ' ' | 自动投放 |
| 60 | fhistorysupply | 历史供应 | varchar | 50 |  | √ | '0' | 历史供应,枚举: 0 :所有历史供应 1 :历史供应天数 |
| 61 | fdemdelayday | fdemdelayday | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_invp_scheme_master |  | fmasterid |
| 2 | idx_t_invp_scheme_createorg |  | fcreateorgid |
| 3 | pk_t_invp_scheme |  | fid |
