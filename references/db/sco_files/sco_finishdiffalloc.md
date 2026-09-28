# 完工产品差异分配单-sco_finishdiffalloc

## 完工产品差异分配单-主表 t_sco_finishdiffalloc

- **表名称：** 完工产品差异分配单-主表
- **表名：** t_sco_finishdiffalloc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | ftotalunabsoubdiff | 未吸收成本差异（合计） | numeric | 23 | 10 | √ | 0 | 未吸收成本差异（合计） |
| 4 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftotalamount | 金额（合计） | numeric | 23 | 10 | √ | 0 | 金额（合计） |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fqualitystatus | 质量状态 | varchar | 255 |  | √ | ' ' | 质量状态,枚举: A :合格品 B :不格品 C :待检品 D :报废品 |
| 9 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 11 | fsrcauditdate | 取价时间 | timestamp | 0 |  |  | null | 取价时间 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fdevcost | 研发费用 | bpchar | 1 |  | √ | '0' | 研发费用,枚举: 0 :否 1 :是 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fsourcebillentry | 来源单据单据体ID | int8 | 64 |  | √ | 0 | 来源单据单据体ID |
| 16 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 17 | fownertype | 入库货主类型 | varchar | 255 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 18 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fbatchid | 批号 | varchar | 255 |  | √ | ' ' | 批号 |
| 21 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 22 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 25 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 26 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 27 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 30 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 31 | ftotaldowndiff | 下阶差异（合计） | numeric | 23 | 10 | √ | 0 | 下阶差异（合计） |
| 32 | fsourcebill | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 33 | finvorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fowner | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 36 | fcompleteqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 37 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 38 | ffactbillno | 完工产量归集单据编号 | varchar | 255 |  | √ | ' ' | 完工产量归集单据编号 |
| 39 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 40 | fsrcbilltype | 源单类型 | varchar | 255 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 41 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象f7 sco_costobjectf7](../sco_files/sco_costobjectf7.md) |
| 42 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 43 | finvstatus | 入库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 46 | ftotalactualamt | 实际金额（合计） | numeric | 23 | 10 | √ | 0 | 实际金额（合计） |
| 47 | ftotalfinishdiff | 完工结算差异（合计） | numeric | 23 | 10 | √ | 0 | 完工结算差异（合计） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_finishdiffalloc |  | fid |
| 2 | idx_sco_finishdiffalloc_m0 |  | fbillno |

---

## 成本信息-子表 t_sco_finishdiffalloccost

- **表名称：** 成本信息-子表
- **表名：** t_sco_finishdiffalloccost

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fdowndiff | 下阶差异 | numeric | 23 | 10 | √ | 0 | 下阶差异 |
| 4 | ffinishdiff | 完工结算差异 | numeric | 23 | 10 | √ | 0 | 完工结算差异 |
| 5 | funabsoubdiff | 未吸收成本差异 | numeric | 23 | 10 | √ | 0 | 未吸收成本差异 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 8 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 9 | factualamt | 实际金额 | numeric | 23 | 10 | √ | 0 | 实际金额 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fstdprice | 标准单价 | numeric | 23 | 10 | √ | 0 | 标准单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_finishdiffalloccost |  | fentryid |
| 2 | idx_sco_finishdiffalloccost_fk |  | fid |
