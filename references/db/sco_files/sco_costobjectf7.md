# 成本核算对象-sco_costobjectf7

## 成本核算对象-主表 t_sco_costobject

- **表名称：** 成本核算对象-主表
- **表名：** t_sco_costobject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foriginype | 来源类型 | varchar | 30 |  | √ | ' ' | 来源类型,枚举: MANUAL :手工录入 API :API EXCEL :列表引入 RULE :规则引入 |
| 3 | fcostobjectruleid | 成本核算对象规则 | int8 | 64 |  | √ | 0 | 成本核算对象规则 cad_costobjectrule |
| 4 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fproductgroupid | 产品组 | int8 | 64 |  | √ | 0 | 产品组 sco_productintogroup |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fbizstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: A :未结算 B :已结算 |
| 10 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 11 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 12 | fisrework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 13 | fbiztype | 成本计算方法 | varchar | 30 |  | √ | ' ' | 成本计算方法,枚举: RO :工单成本 SO :分批法 PZ :品种法 FL :分类法 SW :服务工单 SP :服务项目 |
| 14 | fweight | 分配权重 | numeric | 23 | 10 | √ | 0 | 分配权重 |
| 15 | fisoutsource | 委外 | bpchar | 1 |  | √ | '0' | 委外 |
| 16 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 17 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 18 | fproducenum | 生产编号 | varchar | 30 |  | √ | ' ' | 生产编号 |
| 19 | flot | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 20 | fbomversionid | 物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 21 | fbillno | 成本核算对象编码 | varchar | 255 |  | √ | ' ' | 成本核算对象编码 |
| 22 | fsrcbillnumber | 源单单号 | varchar | 255 |  | √ | ' ' | 源单单号 |
| 23 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 24 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 25 | fmainproobjid | 主产品成本核算对象 | int8 | 64 |  | √ | 0 | 主产品成本核算对象 |
| 26 | fperiodid | fperiodid | int8 | 64 |  | √ | 0 |  |
| 27 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :提交 C :审核 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fprojectnumberid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 30 | fsrcbillrow | 源单行号 | int8 | 64 |  | √ | 0 | 源单行号 |
| 31 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 32 | fprobillid | 生产工单分录ID | int8 | 64 |  | √ | 0 | 生产工单分录ID |
| 33 | fproducttype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 34 | frule | 核算规则 | varchar | 30 |  | √ | ' ' | 核算规则,枚举: SN :源单单号+源单行号 PN :产品+生产编号 CP :产品 RULE_SW :源单单号+源单行号+项目号 RULE_SP :项目号 CU :自定义 |
| 35 | fsotype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: PB :工单/委外工单 SB :生产编号 SOTYPE_SW :检修工单 SOTYPE_SP :项目 |
| 36 | fcollconfigid | fcollconfigid | int8 | 64 |  | √ | 0 |  |
| 37 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 38 | fpno | fpno | int8 | 64 |  | √ | 0 |  |
| 39 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 40 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

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

## 成本核算对象-多语言表 t_sco_costobject_l

- **表名称：** 成本核算对象-多语言表
- **表名：** t_sco_costobject_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 3 | fname | 成本核算对象名称 | varchar | 255 |  | √ | ' ' | 成本核算对象名称 |
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
