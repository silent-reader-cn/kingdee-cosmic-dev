# 物料组织公共信息-bd_materialcommon

## 物料组织公共信息-主表 t_bd_materialcommon

- **表名称：** 物料组织公共信息-主表
- **表名：** t_bd_materialcommon

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenableinspect | 质检信息 | bpchar | 1 |  | √ | '0' | 质检信息 |
| 3 | fgroupid | 存货类别 | int8 | 64 |  | √ | 0 | [存货类别 bd_materialcategory](../basedata_files/bd_materialcategory.md) |
| 4 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fenableproduct | 生产信息 | bpchar | 1 |  | √ | '0' | 生产信息 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fenabletrustee | 可受托（废弃） | bpchar | 1 |  | √ | '0' | 可受托（废弃） |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fenablevmi | 可VMI | bpchar | 1 |  | √ | '0' | 可VMI |
| 11 | fenableplan | 计划信息 | bpchar | 1 |  | √ | '0' | 计划信息 |
| 12 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 13 | fenablepur | 采购信息 | bpchar | 1 |  | √ | '0' | 采购信息 |
| 14 | fisversionaffectinv | fisversionaffectinv | bpchar | 1 |  | √ | '0' |  |
| 15 | fxkallocationtype | 公共信息分配类型 | varchar | 30 |  | √ | ' ' | 公共信息分配类型,枚举: 1 :个性化 2 :共享型 |
| 16 | fenableasset | 可资产（废弃） | bpchar | 1 |  | √ | '0' | 可资产（废弃） |
| 17 | fmatcreateorg | fmatcreateorg | varchar | 50 |  | √ | ' ' |  |
| 18 | fenableconsign | 可委托代销 | bpchar | 1 |  | √ | '0' | 可委托代销 |
| 19 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 20 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fmbdmasterid | 物料组织公共信息内码 | int8 | 64 |  | √ | 0 | 物料组织公共信息内码 |
| 22 | fenablebom | 可BOM | bpchar | 1 |  | √ | '0' | 可BOM |
| 23 | fisversionaffectprice | fisversionaffectprice | bpchar | 1 |  | √ | '0' |  |
| 24 | fenableoutsource | 可委外 | bpchar | 1 |  | √ | '0' | 可委外 |
| 25 | fenableself | 可自制 | bpchar | 1 |  | √ | '0' | 可自制 |
| 26 | fmaterialname2 | fmaterialname2 | varchar | 50 |  | √ | ' ' |  |
| 27 | fmaterialname3 | fmaterialname3 | varchar | 50 |  | √ | ' ' |  |
| 28 | fconfigproperties | 配置属性 | varchar | 10 |  | √ | ' ' | 配置属性,枚举: 1 : 2 :子项选配 3 :特征选配 |
| 29 | fmaterialname1 | fmaterialname1 | varchar | 50 |  | √ | ' ' |  |
| 30 | fenablesale | 销售信息 | bpchar | 1 |  | √ | '0' | 销售信息 |
| 31 | fenable | 公共信息使用状态 | varchar | 30 |  | √ | ' ' | 公共信息使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 33 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fmaterialname | fmaterialname | varchar | 50 |  | √ | ' ' |  |
| 36 | fmaterialid | 物料(冗余显示用_不支持逻辑处理) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 37 | fenablematerialversion | fenablematerialversion | bpchar | 1 |  | √ | '0' |  |
| 38 | fcontrolinv | 可库存 | bpchar | 1 |  | √ | '0' | 可库存 |
| 39 | fsuite | 套件（废弃） | bpchar | 1 |  | √ | '0' | 套件（废弃） |
| 40 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 41 | fisversionaffectplan | fisversionaffectplan | bpchar | 1 |  | √ | '0' |  |
| 42 | fsource | 来源方式 | bpchar | 1 |  | √ | '' | 来源方式,枚举: 1 :手动新增 2 :引入 3 :PLM传入 4 :API传入 |
| 43 | fstatus | 公共信息数据状态 | varchar | 30 |  | √ | ' ' | 公共信息数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 44 | fenableqtyctrl | 可发量控制 | bpchar | 1 |  | √ | '0' | 可发量控制 |
| 45 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fmasterid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 47 | fbondcontrol | 保税控制 | bpchar | 1 |  | √ | '0' | 保税控制,枚举: 0 :非保税 1 :保税 2 :不控制 |
| 48 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 49 | ftaxrateid | 默认税率(%) | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 50 | fatpcheck | ATP检查 | bpchar | 1 |  | √ | '0' | ATP检查,枚举: 0 : 1 :按物料独立需求 |
| 51 | fmaterialattr | 物料属性 | varchar | 10 |  | √ | '10040' | 物料属性,枚举: 10030 :自制 10040 :外购 10050 :委外 10020 :虚拟 10070 :特征件 |
| 52 | fcreateorgid | 公共信息创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 53 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 54 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 55 | fcontrolsale | 可销售 | bpchar | 1 |  | √ | '0' | 可销售 |
| 56 | fcontrolpur | 可采购 | bpchar | 1 |  | √ | '0' | 可采购 |
| 57 | fmaterialtype | 物料类型 | varchar | 10 |  | √ | ' ' | 物料类型,枚举: 1 :物资 7 :费用 8 :资产 9 :服务 3 :套件 2 :虚拟件 4 :可配置件 5 :特征件 |
| 58 | fctrlstrategy | 公共信息控制策略 | varchar | 30 |  | √ | ' ' | 公共信息控制策略,枚举: 2 :分配/局部共享 5 :全局共享 |
| 59 | fmatmodelnum | fmatmodelnum | varchar | 50 |  | √ | ' ' |  |
| 60 | fmatctrlstrategy | fmatctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 61 | fenableinv | 库存信息 | bpchar | 1 |  | √ | '0' | 库存信息 |
| 62 | fcontrolplan | 可计划 | bpchar | 1 |  | √ | '0' | 可计划 |
| 63 | fcontrolinspect | 可质检 | bpchar | 1 |  | √ | '0' | 可质检 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_materialcommon |  | fid |
| 2 | idx_t_bd_materialcommon_createorg |  | fcreateorgid |
| 3 | idx_t_bd_materialcommon_masterid |  | fmasterid |
| 4 | idx_t_bd_materialcommon_master |  | fmasterid |
| 5 | idx_t_bd_materialcommonsrcid |  | fsourcedataid |
| 6 | idx_t_bd_materialcommonbit |  | fbitindex |
| 7 | idx_t_bd_materialcommon_mbdmasterid |  | fmbdmasterid |

---

## 业务属性-多选基础资料表 t_bd_mtsserviceattribute

- **表名称：** 业务属性-多选基础资料表
- **表名：** t_bd_mtsserviceattribute

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务属性 bd_serviceattribute](../sbd_files/bd_serviceattribute.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_mtsserviceattribute_id |  | fid |
| 2 | pk_t_bd_mtsserviceattribute |  | fpkid |

---

## 物料组织公共信息-多语言表 t_bd_materialcommon_l

- **表名称：** 物料组织公共信息-多语言表
- **表名：** t_bd_materialcommon_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_materialcommon_l |  | fpkid |
| 2 | idx_bd_materialcommon_l_fid |  | fid,flocaleid |

---

## 物料组织公共信息-使用范围表 t_bd_materialcommon_u

- **表名称：** 物料组织公共信息-使用范围表
- **表名：** t_bd_materialcommon_u

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
| 1 | pk_t_bd_materialcommon_u |  | fdataid,fuseorgid |
| 2 | idx_t_bd_materialcommon_u_uo |  | fuseorgid |
