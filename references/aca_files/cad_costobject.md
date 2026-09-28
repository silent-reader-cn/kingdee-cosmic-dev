# 成本核算对象-cad_costobject

## 成本核算对象-主表 t_cad_costobject

- **表名称：** 成本核算对象-主表
- **表名：** t_cad_costobject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foriginype | 来源类型 | varchar | 30 |  | √ | ' ' | 来源类型,枚举: MANUAL :手工录入 API :API EXCEL :列表引入 RULE :规则引入 CONFIG :按配置方案生成 |
| 3 | fcostobjectruleid | 成本核算对象规则 | int8 | 64 |  | √ | 0 | 成本核算对象规则 cad_costobjectrule |
| 4 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | forgid | 核算组织(废弃-230629多核算体系改造) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fproductgroupid | 产品组 | int8 | 64 |  | √ | 0 | 产品组 cad_productintogroup |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :未结算 B :已结算 |
| 10 | fconfiguredcodeid | 配置号（废弃） | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fisrework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 13 | fbiztype | 成本计算方法 | varchar | 30 |  | √ | ' ' | 成本计算方法,枚举: RO :工单成本 PZ :品种法 CU :生产线成本 |
| 14 | fweight | 分配权重 | numeric | 23 | 10 | √ | 0.0000000000 | 分配权重 |
| 15 | fisoutsource | 委外 | bpchar | 1 |  | √ | '0' | 委外 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 18 | fproducenum | 生产编号 | varchar | 50 |  | √ | ' ' | 生产编号 |
| 19 | fsettleaccounttime | 结算时间 | timestamp | 0 |  |  | null | 结算时间 |
| 20 | fbomversionid | 物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 21 | fbillno | 编码 | varchar | 510 |  | √ | ' ' | 编码 |
| 22 | fprdline | 生产线 | int8 | 64 |  | √ | 0 | 生产线 arm_linecapacity |
| 23 | fsrcbillnumber | 源单单号 | varchar | 255 |  | √ | ' ' | 源单单号 |
| 24 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fmainproobjid | 主产品成本核算对象 | int8 | 64 |  | √ | 0 | 主产品成本核算对象 |
| 27 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fprojectnumberid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 30 | fsrcbillrow | 源单行号 | int8 | 64 |  | √ | 0 | 源单行号 |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | fprobillid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 33 | fproducttype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 34 | frule | 核算规则 | varchar | 30 |  | √ | ' ' | 核算规则,枚举: SN :源单单号+源单行号 PN :产品+生产编号 CP :产品 RULE_SW :源单单号+源单行号+项目号 RULE_SP :项目号 RULE_CU :产品+生产线 |
| 35 | fsotype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: PB :工单/委外工单 SB :生产编号 SOTYPE_SW :检修工单 SOTYPE_SP :项目 SOTYPE_ARMIN :重复生产完工入库单 |
| 36 | fcollconfigid | 配置单 | int8 | 64 |  | √ | 0 | 成本归集配置单 cad_costcollectconfig |
| 37 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 38 | fpno | 系统生产流水号 | int8 | 64 |  | √ | 0 | 系统生产流水号 |
| 39 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 40 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cad_costobject2 |  | fbillno |
| 2 | idx_costobj_costc |  | fcostcenterid |
| 3 | idx_costobj_isoutsource |  | fisoutsource |
| 4 | idx_costobj_matpronum |  | fmaterialid |
| 5 | idx_costobj_contrack |  | ftracknumberid,fconfiguredcodeid |
| 6 | index_cad_costobject |  | forgid,fcostcenterid,fmaterialid,fprobillid |
| 7 | t_cad_costobject_pkey |  | fid |
| 8 | idx_costobj_srcidentry |  | fprobillid |

---

## 成本核算对象-多语言表 t_cad_costobject_l

- **表名称：** 成本核算对象-多语言表
- **表名：** t_cad_costobject_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 510 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_costobject_l |  | fid,flocaleid |
| 2 | t_cad_costobject_l_pkey |  | fpkid |

---

## 发生成本中心-多选基础资料表 t_cad_costobj_mpcc

- **表名称：** 发生成本中心-多选基础资料表
- **表名：** t_cad_costobj_mpcc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_costobj_mpcc |  | fpkid |
| 2 | index_uk_cad_costobj_mpcc |  | fid,fbasedataid |
