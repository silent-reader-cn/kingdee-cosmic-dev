# 成本核算对象f7-sco_costobjectf7

## 成本核算对象f7-主表 t_sco_costobject

- **表名称：** 成本核算对象f7-主表
- **表名：** t_sco_costobject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foriginype | 来源类型 | varchar | 30 |  | √ | ' ' | 来源类型,枚举: MANUAL :手工录入 API :API EXCEL :列表导入 RULE :规则导入 |
| 3 | fcostobjectruleid | 成本核算对象规则 | int8 | 64 |  | √ | 0 | [成本核算对象规则 cad_costobjectrule](../aca_files/cad_costobjectrule.md) |
| 4 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fproductionline | 生产线 | int8 | 64 |  | √ | 0 | [生产线 arm_linecapacity](../arm_files/arm_linecapacity.md) |
| 6 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fproductgroupid | 产品组 | int8 | 64 |  | √ | 0 | [产品组 sco_productweight](../sco_files/sco_productweight.md) |
| 9 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :未结算 B :已结算 |
| 11 | flocation | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 12 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 13 | fbonded | 保税 | bpchar | 1 |  |  | '0' | 保税 |
| 14 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 15 | fisrework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 16 | fstorageorgunit | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fbiztype | 成本计算方法 | varchar | 30 |  | √ | ' ' | 成本计算方法,枚举: RO :工单成本 SO :分批法 PZ :品种法 FL :分类法 SW :服务工单 RE :重复制造 SP :服务项目 |
| 18 | fweight | 分配权重 | numeric | 23 | 10 | √ | 0 | 分配权重 |
| 19 | fisoutsource | 委外 | bpchar | 1 |  | √ | '0' | 委外 |
| 20 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 21 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 22 | fproducenum | 生产编号 | varchar | 30 |  | √ | ' ' | 生产编号 |
| 23 | flot | 批号 | varchar | 255 |  | √ | ' ' | 批号 |
| 24 | fbomversionid | 物料版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 25 | fbillno | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 26 | fsrcbillnumber | 源单单号 | varchar | 255 |  | √ | ' ' | 源单单号 |
| 27 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 28 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 29 | fmainproobjid | 主产品成本核算对象 | int8 | 64 |  | √ | 0 | 主产品成本核算对象 |
| 30 | fperiodid | fperiodid | int8 | 64 |  | √ | 0 |  |
| 31 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :提交 C :审核 |
| 32 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 33 | fprojectnumberid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 34 | fsrcbillrow | 源单行号 | int8 | 64 |  | √ | 0 | 源单行号 |
| 35 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 36 | fprobillid | 生产工单分录ID | int8 | 64 |  | √ | 0 | 生产工单分录ID |
| 37 | fproducttype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 38 | fisdevproduce | 研发试制 | bpchar | 1 |  |  | '0' | 研发试制 |
| 39 | fowner | 货主 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fwarehouse | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 41 | frule | 核算规则 | varchar | 30 |  | √ | ' ' | 核算规则,枚举: SN :源单单号+源单行号 PN :产品+生产编号 CP :产品 RULE_SW :源单单号+源单行号+项目号 RULE_SP :项目号 CU :自定义 RE :生产线+产品+物料版本+辅助属性 |
| 42 | fsotype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: PB :工单/委外工单 SB :生产编号 SOTYPE_SW :检修工单 SOTYPE_SP :项目 |
| 43 | fcollconfigid | fcollconfigid | int8 | 64 |  | √ | 0 |  |
| 44 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 45 | fpno | fpno | int8 | 64 |  | √ | 0 |  |
| 46 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 47 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 48 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_costobject2 |  | fbillno |
| 2 | index_sco_costobject |  | forgid,fcostcenterid,fmaterialid,fprobillid |
| 3 | pk_sco_costobject |  | fid |

---

## 成本核算对象f7-多语言表 t_sco_costobject_l

- **表名称：** 成本核算对象f7-多语言表
- **表名：** t_sco_costobject_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_costobject_l |  | fpkid |
| 2 | index_sco_costobject_l |  | fid,flocaleid |
