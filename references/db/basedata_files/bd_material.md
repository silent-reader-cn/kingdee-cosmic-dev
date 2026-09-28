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
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | [辅助属性定义 bd_auxproperty](../sbd_files/bd_auxproperty.md) |
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

## 已选特征-多选基础资料表 t_bd_matfeaturevals

- **表名称：** 已选特征-多选基础资料表
- **表名：** t_bd_matfeaturevals

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [特征值 bd_featurevalue](../basedata_files/bd_featurevalue.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_matfeaturevals |  | fpkid |
| 2 | idx_bd_matfeatvals_valid |  | fbasedataid |
| 3 | idx_bd_matfeatvals_fid |  | fid |

---

## 物料-主表 t_bd_material

- **表名称：** 物料-主表
- **表名：** t_bd_material

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fgroupid | 物料分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 4 | flength | 长度 | numeric | 23 | 10 | √ | 0.0000000000 | 长度 |
| 5 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fgrossweight | 毛重 | numeric | 23 | 10 | √ | 0.0000000000 | 毛重 |
| 7 | fispurchasing | fispurchasing | bpchar | 1 |  | √ | '0' |  |
| 8 | fk_bj73_decimalfield | 产品系数 | numeric | 23 | 4 |  | null | 产品系数 |
| 9 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fnetweight | 净重 | numeric | 23 | 10 | √ | 0.0000000000 | 净重 |
| 11 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fisassets | fisassets | bpchar | 1 |  | √ | '0' |  |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fk_bj73_pricefield1 | 发制 | numeric | 23 | 10 |  | null | 发制 |
| 17 | fissales | fissales | bpchar | 1 |  | √ | '0' |  |
| 18 | fisasstattr | fisasstattr | bpchar | 1 |  | √ | '0' |  |
| 19 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 20 | fk_bj73_pricefield7 | 气 | numeric | 23 | 10 |  | null | 气 |
| 21 | fk_bj73_pricefield6 | 电 | numeric | 23 | 10 |  | null | 电 |
| 22 | fk_bj73_pricefield5 | 水 | numeric | 23 | 10 |  | null | 水 |
| 23 | fk_bj73_pricefield4 | 外包 | numeric | 23 | 10 |  | null | 外包 |
| 24 | fk_bj73_pricefield3 | 内包 | numeric | 23 | 10 |  | null | 内包 |
| 25 | fk_bj73_pricefield2 | 改刀 | numeric | 23 | 10 |  | null | 改刀 |
| 26 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fdescription | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |
| 28 | fhelpcode | 助记码 | varchar | 80 |  | √ | ' ' | 助记码 |
| 29 | fvolumnunit | 容积单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 30 | flengthunit | 尺寸单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fsimplepinyin | 简拼 | varchar | 255 |  | √ | ' ' | 简拼 |
| 32 | fweightunit | 重量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 33 | fk_bj73_name | fk_bj73_name | varchar | 255 |  | √ | ' ' |  |
| 34 | farea | 面积 | numeric | 23 | 10 | √ | 0 | 面积 |
| 35 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 36 | funitconvertdir | 换算方向 | varchar | 10 |  | √ | ' ' | 换算方向,枚举: A :正向换算 B :逆向换算 |
| 37 | fofferingcode | Offering | int8 | 64 |  | √ | 0 | [产品目录 bd_productsummary](../basedata_files/bd_productsummary.md) |
| 38 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 39 | foldnumber | 旧物料编码 | varchar | 80 |  | √ | ' ' | 旧物料编码 |
| 40 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 41 | fk_bj73_textfield6 | OA过滤 | varchar | 50 |  | √ | ' ' | OA过滤 |
| 42 | flogo | 图片 | varchar | 255 |  | √ | ' ' | 图片 |
| 43 | fk_bj73_textfield7 | 统计大类 | varchar | 50 |  | √ | ' ' | 统计大类 |
| 44 | fmodel | 规格型号 | varchar | 512 |  |  | ' ' | 规格型号 |
| 45 | fk_bj73_textfield4 | 产品细类 | varchar | 50 |  | √ | ' ' | 产品细类 |
| 46 | fk_bj73_textfield5 | 包装 | varchar | 50 |  | √ | ' ' | 包装 |
| 47 | fk_bj73_qtyfield3 | 固形物重量 | numeric | 23 | 10 |  | null | 固形物重量 |
| 48 | fk_bj73_qtyfield1 | 加水重量 | numeric | 23 | 10 |  | null | 加水重量 |
| 49 | fk_bj73_textfield8 | 统计分类 | varchar | 50 |  | √ | ' ' | 统计分类 |
| 50 | fk_bj73_qtyfield | 箱贴重量 | numeric | 23 | 10 |  | null | 箱贴重量 |
| 51 | fk_bj73_qtyfield2 | 实装重量 | numeric | 23 | 10 |  | null | 实装重量 |
| 52 | fk_bj73_textfield9 | 渠道 | varchar | 50 |  | √ | ' ' | 渠道 |
| 53 | fisplan | fisplan | bpchar | 1 |  | √ | '0' |  |
| 54 | fk_bj73_textfield12 | 收入科目 | varchar | 50 |  | √ | ' ' | 收入科目 |
| 55 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 56 | fk_bj73_textfield11 | 科目明细 | varchar | 50 |  | √ | ' ' | 科目明细 |
| 57 | fk_bj73_textfield14 | 零售价格 | varchar | 50 |  | √ | ' ' | 零售价格 |
| 58 | fsuite | 套件 | bpchar | 1 |  | √ | '0' | 套件 |
| 59 | fk_bj73_textfield13 | 重量系数 | varchar | 50 |  | √ | ' ' | 重量系数 |
| 60 | fk_bj73_textfield2 | 分类 | varchar | 50 |  | √ | ' ' | 分类 |
| 61 | fk_bj73_textfield3 | 产品大类 | varchar | 50 |  | √ | ' ' | 产品大类 |
| 62 | ferpclsid | ferpclsid | varchar | 30 |  | √ | '10040' |  |
| 63 | fk_bj73_textfield10 | fk_bj73_textfield10 | varchar | 255 |  |  | null |  |
| 64 | fk_bj73_textfield1 | 厂号等级 | varchar | 50 |  | √ | ' ' | 厂号等级 |
| 65 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 66 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 67 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 68 | fk_bj73_textfield16 | 战略分类 | varchar | 50 |  | √ | ' ' | 战略分类 |
| 69 | fk_bj73_textfield15 | 成本科目 | varchar | 50 |  | √ | ' ' | 成本科目 |
| 70 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 71 | fk_bj73_textfield17 | 规格等级 | varchar | 50 |  | √ | ' ' | 规格等级 |
| 72 | ftaxrateid | 默认税率(%)（废弃） | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 73 | fenableuserid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 74 | fissubcontract | fissubcontract | bpchar | 1 |  | √ | '0' |  |
| 75 | fapprovedate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 76 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 77 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 78 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 79 | fvolume | 容积 | numeric | 23 | 10 | √ | 0.0000000000 | 容积 |
| 80 | fismanufacture | fismanufacture | bpchar | 1 |  | √ | '0' |  |
| 81 | fenabledate | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 82 | fwidth | 宽度 | numeric | 23 | 10 | √ | 0.0000000000 | 宽度 |
| 83 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 84 | fisinventory | fisinventory | bpchar | 1 |  | √ | '0' |  |
| 85 | fareaunit | 面积单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 86 | fadminorgid | fadminorgid | int8 | 64 |  | √ | 0 |  |
| 87 | fk_bj73_textfield | 箱贴名称 | varchar | 50 |  | √ | ' ' | 箱贴名称 |
| 88 | fk_bj73_pricefield | 前处理 | numeric | 23 | 10 |  | null | 前处理 |
| 89 | fheight | 高度 | numeric | 23 | 10 | √ | 0.0000000000 | 高度 |
| 90 | fauxptyunit2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_materialsrcid |  | fsourcedataid |
| 2 | idx_t_bd_material_number |  | fnumber |
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
| 3 | fmodel | 规格型号 | varchar | 512 |  |  | ' ' | 规格型号 |
| 4 | fk_bj73_name | fk_bj73_name | varchar | 255 |  | √ | ' ' |  |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fdescription | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

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
| 3 | fenableproduct | fenableproduct | bpchar | 1 |  | √ | '0' |  |
| 4 | fenabletrustee | 可受托(废弃) | bpchar | 1 |  | √ | '0' | 可受托(废弃) |
| 5 | fisenablematerialversion | 启用版本管理 | bpchar | 1 |  | √ | '0' | 启用版本管理 |
| 6 | fenablevmi | fenablevmi | bpchar | 1 |  | √ | '0' |  |
| 7 | fmatchbeforebomid | 源BOMID | int8 | 64 |  | √ | 0 | 源BOMID |
| 8 | fenablepur | fenablepur | bpchar | 1 |  | √ | '0' |  |
| 9 | fisversionaffectinv | 影响库存 | bpchar | 1 |  | √ | '0' | 影响库存 |
| 10 | fplmmaterialid | PLM物料ID | int8 | 64 |  | √ | 0 | PLM物料ID |
| 11 | fenableasset | fenableasset | bpchar | 1 |  | √ | '0' |  |
| 12 | fenableconsign | fenableconsign | bpchar | 1 |  | √ | '0' |  |
| 13 | fserialunit | 序列号计量单位(废弃) | varchar | 10 |  | √ | ' ' | 序列号计量单位(废弃),枚举: 1 :天 2 :月 3 :年 |
| 14 | falertleadtime | 寿命预警提前期(废弃) | int8 | 64 |  | √ | 0 | 寿命预警提前期(废弃) |
| 15 | ffarmproducts | 农产品 | bpchar | 1 |  | √ | '0' | 农产品 |
| 16 | fsparepart | 备件(废弃) | bpchar | 1 |  | √ | '0' | 备件(废弃) |
| 17 | flifetime | 寿命期(废弃) | int8 | 64 |  | √ | 0 | 寿命期(废弃) |
| 18 | fisdisposable | 品类物料(废弃) | bpchar | 1 |  | √ | '0' | 品类物料(废弃) |
| 19 | fk_bj73_textfield21 | 包材编码 | varchar | 50 |  | √ | ' ' | 包材编码 |
| 20 | fenablesersatinf | 序列号启用附属信息(废弃) | bpchar | 1 |  | √ | '0' | 序列号启用附属信息(废弃) |
| 21 | fk_bj73_textfield20 | 贮存保质期 | varchar | 50 |  | √ | ' ' | 贮存保质期 |
| 22 | fenableoutsource | fenableoutsource | bpchar | 1 |  | √ | '0' |  |
| 23 | fconfigproperties | fconfigproperties | varchar | 10 |  | √ | ' ' |  |
| 24 | fmatchbeforebomver | 源BOM编码 | varchar | 255 |  | √ | ' ' | 源BOM编码 |
| 25 | fenablesale | fenablesale | bpchar | 1 |  | √ | '0' |  |
| 26 | fenablelotsatinf | 批号启用附属信息(废弃) | bpchar | 1 |  | √ | '0' | 批号启用附属信息(废弃) |
| 27 | fversionruleid | 版本编码规则 | int8 | 64 |  | √ | 0 | [版本序列 bd_versionseq](../basedata_files/bd_versionseq.md) |
| 28 | fserialmu | 序列号计量单位(废弃) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 29 | fisoutputrequest | 仅出货必录序列号(废弃) | bpchar | 1 |  | √ | '0' | 仅出货必录序列号(废弃) |
| 30 | fhazardous | 物料危险性(废弃) | varchar | 30 |  | √ | ' ' | 物料危险性(废弃),枚举: 1 :有毒 2 :易燃 3 :易爆 |
| 31 | fenablematerialversion | fenablematerialversion | bpchar | 1 |  | √ | '0' |  |
| 32 | fsuite | fsuite | bpchar | 1 |  | √ | '0' |  |
| 33 | fisversionaffectplan | 影响计划 | bpchar | 1 |  | √ | '0' | 影响计划 |
| 34 | fsource | 来源方式 | bpchar | 1 |  | √ | '' | 来源方式,枚举: 1 :手动新增 2 :引入 3 :PLM传入 4 :API传入 |
| 35 | fk_bj73_textfield10 | 存货大类 | varchar | 50 |  | √ | ' ' | 存货大类 |
| 36 | fk_bj73_textfield19 | 默认贮存方式 | varchar | 50 |  | √ | ' ' | 默认贮存方式 |
| 37 | fenablelot | 启用批号管理(废弃) | bpchar | 1 |  | √ | '0' | 启用批号管理(废弃) |
| 38 | fk_bj73_textfield18 | 销售参考价 | varchar | 50 |  | √ | ' ' | 销售参考价 |
| 39 | fcompletetag | 整机标识(废弃) | bpchar | 1 |  | √ | '0' | 整机标识(废弃) |
| 40 | fmatchbeforematid | 源可配置产品ID | int8 | 64 |  | √ | 0 | 源可配置产品ID |
| 41 | fenablelifemgr | 启用寿命管理(废弃) | bpchar | 1 |  | √ | '0' | 启用寿命管理(废弃) |
| 42 | fshelflife | 在架寿命期(废弃) | int8 | 64 |  | √ | 0 | 在架寿命期(废弃) |
| 43 | fisuseauxpty | 启用辅助属性 | bpchar | 1 |  | √ | '0' | 启用辅助属性 |
| 44 | fmaterialtype | fmaterialtype | varchar | 10 |  | √ | ' ' |  |
| 45 | fenableserial | 启用序列号管理(废弃) | bpchar | 1 |  | √ | '0' | 启用序列号管理(废弃) |
| 46 | fmaterialform | 物料形态(废弃) | varchar | 10 |  | √ | ' ' | 物料形态(废弃),枚举: 1 :液体 2 :固体 3 :气体 |
| 47 | fenableinv | fenableinv | bpchar | 1 |  | √ | '0' |  |
| 48 | flotsatinfoscheme | 批号附属信息方案(废弃) | varchar | 10 |  | √ | ' ' | 批号附属信息方案(废弃),枚举: |
| 49 | fsersatinfoscheme | 序列号附属信息方案(废弃) | varchar | 10 |  | √ | ' ' | 序列号附属信息方案(废弃),枚举: |
| 50 | fdeductiblerate | 可抵扣率(%) | numeric | 23 | 10 | √ | 0 | 可抵扣率(%) |
| 51 | fmatchbeforematnum | 源可配置产品 | varchar | 255 |  | √ | ' ' | 源可配置产品 |

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
