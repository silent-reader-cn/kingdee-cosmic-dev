# 材料耗用归集-aca_matusecollect

## 明细信息-子表 t_sca_matusecollectentry

- **表名称：** 明细信息-子表
- **表名：** t_sca_matusecollectentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 3 | fproplanid | 工序计划号 | int8 | 64 |  | √ | 0 | [工序计划F7 sfc_processplan_f7](../sfc_files/sfc_processplan_f7.md) |
| 4 | fproductnum | 生产编号 | varchar | 255 |  | √ | ' ' | 生产编号 |
| 5 | fsourcebillentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 6 | fprojectid | 项目名称 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 7 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | fproductgroupid | 产品组 | int8 | 64 |  | √ | 0 | [产品组 cad_productintogroup](../aca_files/cad_productintogroup.md) |
| 9 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 12 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 13 | fproplanentryid | 工序计划分录内码 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 14 | fisrework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 15 | fmatversionid | 物料版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 16 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 17 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 18 | fproductid | 产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 19 | flotcoderuleid | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 20 | fkeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | [卷算维度数据表 cad_keycol](../cad_files/cad_keycol.md) |
| 21 | fcostobjectid | 所属成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象 cad_costobjectf7](../aca_files/cad_costobjectf7.md) |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 23 | fkeycol | 维度字段 | varchar | 200 |  | √ | ' ' | 维度字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_matusecollectentry_pkey |  | fentryid |
| 2 | idx_matuseentry_coobb |  | fcostobjectid |
| 3 | idx_cad_matusecollect_fkeycol |  | fkeycol |
| 4 | index_sca_matcollectentry |  | fmaterialid,fcostobjectid |
| 5 | index_sca_matcollectentry_fid |  | fid |

---

## 材料耗用归集-主表 t_sca_matusecollect

- **表名称：** 材料耗用归集-主表
- **表名：** t_sca_matusecollect

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fappnum | 所属应用 | varchar | 100 |  | √ | ' ' | 所属应用,枚举: sca :标准成本核算 aca :实际成本核算 |
| 10 | fsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: MANUALENTER :手工录入 TPLIMPORT :模板引入 APIINTERFACE :API引入 SYSIMPORT_PROGET :生产领料单 SYSIMPORT_PROBACK :生产退料单 SYSIMPORT_PROADD :生产补料单 SYSIMPORT_OUT :领料出库单 SYSIMPORT_IMMDCOMOUT :委外领料单 SYSIMPORT_IMMDCOMRETURN :委外退料单 SYSIMPORT_IMMDCOMFEED :委外补料单 CONFIG :按配置方案引入 |
| 11 | fsrcauditdate | 取价时间 | timestamp | 0 |  |  | null | 取价时间 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fbiztype | 业务类型（旧） | varchar | 30 |  | √ | ' ' | 业务类型（旧）,枚举: PRODUCTMATGET :生产领料 PRODUCTMATFALLBACK :生产领料退回 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 16 | fnsrcauditdate | 来源单据审核日期 | timestamp | 0 |  |  | null | 来源单据审核日期 |
| 17 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 18 | fcollconfigid | 配置单 | int8 | 64 |  | √ | 0 | [成本归集配置单 cad_costcollectconfig](../aca_files/cad_costcollectconfig.md) |
| 19 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 20 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 21 | fsrcbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 22 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_matuse_costc |  | fcostcenterid |
| 2 | idx_matuse_srcid |  | fsourcebillid |
| 3 | t_sca_matusecollect_pkey |  | fid |
| 4 | idx_matuse_billno |  | fbillno |
| 5 | index_sca_matusecollect |  | forgid,fcostcenterid |

---

## 材料耗用归集-多语言表 t_sca_matusecollect_l

- **表名称：** 材料耗用归集-多语言表
- **表名：** t_sca_matusecollect_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_matusecollect_l_pkey |  | fpkid |
| 2 | index_sca_matusecollect_l |  | fid,flocaleid |
