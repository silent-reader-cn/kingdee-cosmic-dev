# 物料组织公共信息-bd_materialcommon

## 物料组织公共信息-主表 t_bd_materialcommon

- **表名称：** 物料组织公共信息-主表
- **表名：** t_bd_materialcommon

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenableinspect | 质检信息 | bpchar | 1 |  | √ | '0' | 质检信息 |
| 3 | fgroupid | 存货类别 | int8 | 64 |  | √ | 0 | 存货类别 bd_materialcategory |
| 4 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fenableproduct | 生产信息 | bpchar | 1 |  | √ | '0' | 生产信息 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fenabletrustee | 可受托 | bpchar | 1 |  | √ | '0' | 可受托 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fenablevmi | 可VMI | bpchar | 1 |  | √ | '0' | 可VMI |
| 11 | fenableplan | 计划信息 | bpchar | 1 |  | √ | '0' | 计划信息 |
| 12 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 13 | fenablepur | 采购信息 | bpchar | 1 |  | √ | '0' | 采购信息 |
| 14 | fisversionaffectinv | fisversionaffectinv | bpchar | 1 |  | √ | '0' |  |
| 15 | fxkallocationtype | 公共信息分配类型 | varchar | 30 |  | √ | ' ' | 公共信息分配类型,枚举: 1 :个性化 2 :共享型 |
| 16 | fenableasset | 可资产 | bpchar | 1 |  | √ | '0' | 可资产 |
| 17 | fenableconsign | 可委托代销 | bpchar | 1 |  | √ | '0' | 可委托代销 |
| 18 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 19 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fmbdmasterid | 物料组织公共信息内码 | int8 | 64 |  | √ | 0 | 物料组织公共信息内码 |
| 21 | fenablebom | 可BOM | bpchar | 1 |  | √ | '0' | 可BOM |
| 22 | fisversionaffectprice | fisversionaffectprice | bpchar | 1 |  | √ | '0' |  |
| 23 | fenableoutsource | 可委外 | bpchar | 1 |  | √ | '0' | 可委外 |
| 24 | fenableself | 可自制 | bpchar | 1 |  | √ | '0' | 可自制 |
| 25 | fconfigproperties | 配置属性 | varchar | 10 |  | √ | ' ' | 配置属性,枚举: 1 : 2 :子项选配 3 :特性选配 |
| 26 | fenablesale | 销售信息 | bpchar | 1 |  | √ | '0' | 销售信息 |
| 27 | fenable | 公共信息使用状态 | varchar | 30 |  | √ | ' ' | 公共信息使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 29 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fmaterialid | 物料(冗余显示用_不支持逻辑处理) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 32 | fenablematerialversion | fenablematerialversion | bpchar | 1 |  | √ | '0' |  |
| 33 | fcontrolinv | 可库存 | bpchar | 1 |  | √ | '0' | 可库存 |
| 34 | fsuite | 套件（废弃） | bpchar | 1 |  | √ | '0' | 套件（废弃） |
| 35 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 36 | fisversionaffectplan | fisversionaffectplan | bpchar | 1 |  | √ | '0' |  |
| 37 | fsource | 创建来源 | bpchar | 1 |  | √ | '' | 创建来源,枚举: 1 :手动新增 2 :引入 3 :PLM传入 4 :API传入 |
| 38 | fstatus | 公共信息数据状态 | varchar | 30 |  | √ | ' ' | 公共信息数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 39 | fenableqtyctrl | 可发量控制 | bpchar | 1 |  | √ | '0' | 可发量控制 |
| 40 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fmasterid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 42 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 43 | fmaterialattr | 物料属性 | varchar | 10 |  | √ | '10040' | 物料属性,枚举: 10030 :自制 10040 :外购 10050 :委外 10020 :虚拟 10070 :特征件 |
| 44 | fcreateorgid | 公共信息创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 46 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 47 | fcontrolsale | 可销售 | bpchar | 1 |  | √ | '0' | 可销售 |
| 48 | fcontrolpur | 可采购 | bpchar | 1 |  | √ | '0' | 可采购 |
| 49 | fmaterialtype | 物料类型 | varchar | 10 |  | √ | ' ' | 物料类型,枚举: 1 :物资 7 :费用 8 :资产 9 :服务 3 :套件 2 :虚拟件 4 :可配置件 5 :特征件 |
| 50 | fctrlstrategy | 公共信息控制策略 | varchar | 30 |  | √ | ' ' | 公共信息控制策略,枚举: 2 :分配/局部共享 5 :全局共享 |
| 51 | fenableinv | 库存信息 | bpchar | 1 |  | √ | '0' | 库存信息 |
| 52 | fcontrolplan | 可计划 | bpchar | 1 |  | √ | '0' | 可计划 |
| 53 | fcontrolinspect | 可质检 | bpchar | 1 |  | √ | '0' | 可质检 |

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
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务属性 bd_serviceattribute |
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
