# 材料耗用归集-sco_matusecollect

## 明细信息-子表 t_sco_matusecollectentry

- **表名称：** 明细信息-子表
- **表名：** t_sco_matusecollectentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproductnum | 生产编号 | varchar | 255 |  | √ | ' ' | 生产编号 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fproductgroupid | fproductgroupid | int8 | 64 |  | √ | 0 |  |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 8 | fbonded | 保税 | bpchar | 1 |  |  | '0' | 保税 |
| 9 | fisrework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 10 | fstorageorgunit | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fmatversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 12 | fdevcost | 研发费用 | bpchar | 1 |  |  | '0' | 研发费用,枚举: 0 :否 1 :是 |
| 13 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 14 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 15 | fkeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | [卷算维度数据表 sco_keycol](../sco_files/sco_keycol.md) |
| 16 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 17 | foutownertype | 出库货主类型 | varchar | 255 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 18 | fsourcebillentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 19 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 20 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 22 | foutowner | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 24 | foutinvstatus | 出库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 25 | fproductid | 产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 26 | flotcoderuleid | 批号 | varchar | 255 |  | √ | ' ' | 批号 |
| 27 | fcostobjectid | 所属成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象f7 sco_costobjectf7](../sco_files/sco_costobjectf7.md) |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fkeycol | 维度字段 | varchar | 50 |  | √ | ' ' | 维度字段 |
| 30 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_sco_matcollectentry_fid |  | fid |
| 2 | pk_sco_matusecollectentry |  | fentryid |
| 3 | index_sco_matcollectentry |  | fmaterialid,fcostobjectid |

---

## 材料耗用归集-主表 t_sco_matusecollect

- **表名称：** 材料耗用归集-主表
- **表名：** t_sco_matusecollect

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 核算组织(20240613版本多核算体系废弃) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sco :标准成本核算 aca :实际成本核算 |
| 10 | fsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: MANUALENTER :手工录入 TPLIMPORT :模板导入 APIINTERFACE :API导入 SYSIMPORT_PROGET :生产领料单 SYSIMPORT_PROBACK :生产退料单 SYSIMPORT_PROADD :生产补料单 SYSIMPORT_OUT :领料出库单 SYSIMPORT_IMMDCOMOUT :委外领料单 SYSIMPORT_IMMDCOMRETURN :委外退料单 SYSIMPORT_IMMDCOMFEED :委外补料单 CONFIG :按配置方案导入 |
| 11 | fsrcauditdate | 取价时间 | timestamp | 0 |  |  | null | 取价时间 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fbiztype | 业务类型（旧） | varchar | 30 |  | √ | ' ' | 业务类型（旧）,枚举: PRODUCTMATGET :生产领料 PRODUCTMATFALLBACK :生产领料退回 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 16 | fnsrcauditdate | 来源单据审核时间 | timestamp | 0 |  |  | null | 来源单据审核时间 |
| 17 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 18 | fcollconfigid | 配置单 | int8 | 64 |  | √ | 0 | [成本归集配置单 cad_costcollectconfig](../aca_files/cad_costcollectconfig.md) |
| 19 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 20 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 21 | fsrcbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 22 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_matusecollect |  | fid |
| 2 | index_sco_matusecollect |  | forgid,fbookdate,fmanuorgid |

---

## 材料耗用归集-多语言表 t_sco_matusecollect_l

- **表名称：** 材料耗用归集-多语言表
- **表名：** t_sco_matusecollect_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_sco_matusecollect_l |  | fid,flocaleid |
| 2 | pk_sco_matusecollect_l |  | fpkid |
