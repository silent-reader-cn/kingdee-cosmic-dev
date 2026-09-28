# 物料-bd_material

## 辅助属性单据体-子表 t_bd_matscmproapentry

- **表名称：** 辅助属性单据体-子表
- **表名：** t_bd_matscmproapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fiscomcontrol | 组合控制 | bpchar | 1 |  | √ | '0' | 组合控制 |
| 3 | fisaffectplan | 影响计划 | bpchar | 1 |  | √ | '0' | 影响计划 |
| 4 | fisvaluecontrol | 值范围控制 | bpchar | 1 |  | √ | '0' | 值范围控制 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | 辅助属性定义 bd_auxproperty |
| 6 | fissetvalue | 已维护属性值 | bpchar | 1 |  | √ | '0' | 已维护属性值 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fisaffectinv | 影响库存 | bpchar | 1 |  | √ | '0' | 影响库存 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fisaffectprice | 影响成本 | bpchar | 1 |  | √ | '0' | 影响成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_matscmproapentry_fid |  | fid |
| 2 | t_bd_matscmproapentry_pkey |  | fentryid |

---

## 物料-主表 t_bd_material

- **表名称：** 物料-主表
- **表名：** t_bd_material

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fgroupid | 物料分类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 4 | flength | 长度 | numeric | 23 | 10 | √ | 0.0000000000 | 长度 |
| 5 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fgrossweight | 毛重 | numeric | 23 | 10 | √ | 0.0000000000 | 毛重 |
| 7 | fispurchasing | fispurchasing | bpchar | 1 |  | √ | '0' |  |
| 8 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fnetweight | 净重 | numeric | 23 | 10 | √ | 0.0000000000 | 净重 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fisassets | fisassets | bpchar | 1 |  | √ | '0' |  |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fissales | fissales | bpchar | 1 |  | √ | '0' |  |
| 16 | fisasstattr | fisasstattr | bpchar | 1 |  | √ | '0' |  |
| 17 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 18 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 20 | fhelpcode | 助记码 | varchar | 80 |  | √ | ' ' | 助记码 |
| 21 | fvolumnunit | 容积单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | flengthunit | 尺寸单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 23 | fsimplepinyin | 简拼 | varchar | 255 |  | √ | ' ' | 简拼 |
| 24 | fweightunit | 重量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | funitconvertdir | 换算方向 | varchar | 10 |  | √ | ' ' | 换算方向,枚举: A :正向换算 B :逆向换算 |
| 27 | fofferingcode | Offering | int8 | 64 |  | √ | 0 | 产品目录 bd_productsummary |
| 28 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 29 | foldnumber | 旧物料编码 | varchar | 80 |  | √ | ' ' | 旧物料编码 |
| 30 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 31 | flogo | 图片 | varchar | 255 |  | √ | ' ' | 图片 |
| 32 | fmodel | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 33 | fisplan | fisplan | bpchar | 1 |  | √ | '0' |  |
| 34 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 35 | fsuite | 套件 | bpchar | 1 |  | √ | '0' | 套件 |
| 36 | ferpclsid | ferpclsid | varchar | 30 |  | √ | '10040' |  |
| 37 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 38 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 40 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 41 | ftaxrateid | 默认税率(%) | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 42 | fissubcontract | fissubcontract | bpchar | 1 |  | √ | '0' |  |
| 43 | fapprovedate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 44 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 46 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 47 | fvolume | 容积 | numeric | 23 | 10 | √ | 0.0000000000 | 容积 |
| 48 | fismanufacture | fismanufacture | bpchar | 1 |  | √ | '0' |  |
| 49 | fwidth | 宽度 | numeric | 23 | 10 | √ | 0.0000000000 | 宽度 |
| 50 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 51 | fisinventory | fisinventory | bpchar | 1 |  | √ | '0' |  |
| 52 | fadminorgid | fadminorgid | int8 | 64 |  | √ | 0 |  |
| 53 | fheight | 高度 | numeric | 23 | 10 | √ | 0.0000000000 | 高度 |
| 54 | fauxptyunit2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_material_number |  | fnumber |
| 2 | idx_t_bd_materialsrcid |  | fsourcedataid |
| 3 | idx_t_bd_material_masterid |  | fmasterid |
| 4 | idx_t_bd_material_createorg |  | fcreateorgid |
| 5 | idx_t_bd_material_orgstrat |  | fctrlstrategy,forgid |
| 6 | idx_t_bd_material_group |  | fgroupid |
| 7 | t_bd_material_pkey |  | fid |
| 8 | idx_t_bd_material_master |  | fmasterid |
| 9 | idx_t_bd_material_status |  | fenable,fstatus |
| 10 | idx_t_bd_materialbit |  | fbitindex |
| 11 | idx_t_bd_material_sp |  | fsimplepinyin |

---

## 物料-多语言表 t_bd_material_l

- **表名称：** 物料-多语言表
- **表名：** t_bd_material_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodel | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_material_l_model |  | fmodel |
| 2 | idx_t_bd_material_l_fid |  | fid,flocaleid |
| 3 | t_bd_material_l_pkey |  | fpkid |
| 4 | idx_bd_material_l_name |  | fname |

---

## 物料-使用范围位图表 t_bd_material_m

- **表名称：** 物料-使用范围位图表
- **表名：** t_bd_material_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_material_m |  | forgid |

---

## 物料-分表 t_bd_material_s

- **表名称：** 物料-分表
- **表名：** t_bd_material_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenableinspect | fenableinspect | bpchar | 1 |  | √ | '0' |  |
| 3 | fisoutputrequest | 仅出货必录序列号 | bpchar | 1 |  | √ | '0' | 仅出货必录序列号 |
| 4 | fhazardous | 物料危险性 | varchar | 30 |  | √ | ' ' | 物料危险性,枚举: 1 :有毒 2 :易燃 3 :易爆 |
| 5 | fenablematerialversion | fenablematerialversion | bpchar | 1 |  | √ | '0' |  |
| 6 | fenableproduct | fenableproduct | bpchar | 1 |  | √ | '0' |  |
| 7 | fsuite | fsuite | bpchar | 1 |  | √ | '0' |  |
| 8 | fisversionaffectplan | 影响计划 | bpchar | 1 |  | √ | '0' | 影响计划 |
| 9 | fsource | 物料来源 | bpchar | 1 |  | √ | '' | 物料来源,枚举: 1 :手动新增 2 :引入 3 :PLM传入 4 :API传入 |
| 10 | fenabletrustee | 可受托 | bpchar | 1 |  | √ | '0' | 可受托 |
| 11 | fisenablematerialversion | 启用版本管理 | bpchar | 1 |  | √ | '0' | 启用版本管理 |
| 12 | fenablevmi | fenablevmi | bpchar | 1 |  | √ | '0' |  |
| 13 | fenablelot | 启用批号管理 | bpchar | 1 |  | √ | '0' | 启用批号管理 |
| 14 | fenablepur | fenablepur | bpchar | 1 |  | √ | '0' |  |
| 15 | fisversionaffectinv | 影响库存 | bpchar | 1 |  | √ | '0' | 影响库存 |
| 16 | fplmmaterialid | PLM物料ID | int8 | 64 |  | √ | 0 | PLM物料ID |
| 17 | fenableasset | fenableasset | bpchar | 1 |  | √ | '0' |  |
| 18 | fcompletetag | 整机标识 | bpchar | 1 |  | √ | '0' | 整机标识 |
| 19 | fenableconsign | fenableconsign | bpchar | 1 |  | √ | '0' |  |
| 20 | fserialunit | 序列号计量单位 | varchar | 10 |  | √ | ' ' | 序列号计量单位,枚举: 1 :天 2 :月 3 :年 |
| 21 | falertleadtime | 寿命预警提前期 | int8 | 64 |  | √ | 0 | 寿命预警提前期 |
| 22 | ffarmproducts | 农产品 | bpchar | 1 |  | √ | '0' | 农产品 |
| 23 | fenablelifemgr | 启用寿命管理 | bpchar | 1 |  | √ | '0' | 启用寿命管理 |
| 24 | fsparepart | 备件 | bpchar | 1 |  | √ | '0' | 备件 |
| 25 | flifetime | 寿命期 | int8 | 64 |  | √ | 0 | 寿命期 |
| 26 | fshelflife | 在架寿命期 | int8 | 64 |  | √ | 0 | 在架寿命期 |
| 27 | fisdisposable | 品类物料 | bpchar | 1 |  | √ | '0' | 品类物料 |
| 28 | fisuseauxpty | 启用辅助属性 | bpchar | 1 |  | √ | '0' | 启用辅助属性 |
| 29 | fmaterialtype | fmaterialtype | varchar | 10 |  | √ | ' ' |  |
| 30 | fenablesersatinf | 序列号启用附属信息 | bpchar | 1 |  | √ | '0' | 序列号启用附属信息 |
| 31 | fenableoutsource | fenableoutsource | bpchar | 1 |  | √ | '0' |  |
| 32 | fenableserial | 启用序列号管理 | bpchar | 1 |  | √ | '0' | 启用序列号管理 |
| 33 | fmaterialform | 物料形态 | varchar | 10 |  | √ | ' ' | 物料形态,枚举: 1 :液体 2 :固体 3 :气体 |
| 34 | fconfigproperties | fconfigproperties | varchar | 10 |  | √ | ' ' |  |
| 35 | fenableinv | fenableinv | bpchar | 1 |  | √ | '0' |  |
| 36 | flotsatinfoscheme | 批号附属信息方案 | varchar | 10 |  | √ | ' ' | 批号附属信息方案,枚举: |
| 37 | fenablesale | fenablesale | bpchar | 1 |  | √ | '0' |  |
| 38 | fenablelotsatinf | 批号启用附属信息 | bpchar | 1 |  | √ | '0' | 批号启用附属信息 |
| 39 | fsersatinfoscheme | 序列号附属信息方案 | varchar | 10 |  | √ | ' ' | 序列号附属信息方案,枚举: |
| 40 | fversionruleid | 版本编码规则 | int8 | 64 |  | √ | 0 | 版本序列 bd_versionseq |
| 41 | fdeductiblerate | 可抵扣率(%) | numeric | 23 | 10 | √ | 0 | 可抵扣率(%) |
| 42 | fserialmu | 序列号计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_material_s_pkey |  | fid |
| 2 | dx_t_bd_material_number_type |  | fmaterialtype |

---

## 物料-使用范围表 t_bd_material_u

- **表名称：** 物料-使用范围表
- **表名：** t_bd_material_u

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
| 1 | idx_t_bd_material_u_uo |  | fuseorgid |
| 2 | t_bd_material_u_pkey |  | fdataid,fuseorgid |
