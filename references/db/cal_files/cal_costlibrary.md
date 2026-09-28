# 物料成本库-cal_costlibrary

## 单据体-子表 t_cal_costlibraryentry

- **表名称：** 单据体-子表
- **表名：** t_cal_costlibraryentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubbeginunitcost | 期初加权价(废弃) | numeric | 23 | 10 | √ | 0 | 期初加权价(废弃) |
| 3 | fsubbegincost | 期初加权总价(废弃) | numeric | 23 | 10 | √ | 0 | 期初加权总价(废弃) |
| 4 | fsubunitcost | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 5 | fcostsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 6 | fsubendunitcost | 期末加权价(废弃) | numeric | 23 | 10 | √ | 0 | 期末加权价(废弃) |
| 7 | fsubcost | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fcostelementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 11 | fsubendcost | 期末加权总价(废弃) | numeric | 23 | 10 | √ | 0 | 期末加权总价(废弃) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cal_costlibraryentry |  | fentryid |
| 2 | idx_cal_costlibrarye_id |  | fid |

---

## 物料成本库-主表 t_cal_costlibrary

- **表名称：** 物料成本库-主表
- **表名：** t_cal_costlibrary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fendunitdate | 期末加权价更新时间(废弃) | timestamp | 0 |  |  | null | 期末加权价更新时间(废弃) |
| 3 | fcaldimensionid | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 cal_bd_caldimension](../cal_files/cal_bd_caldimension.md) |
| 4 | fbegincost | 期初加权总价(废弃) | numeric | 23 | 10 | √ | 0 | 期初加权总价(废弃) |
| 5 | fdimwarehouseid | 仓库(核算维度) | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 6 | fbeginunitdate | 期初加权价更新时间(废弃) | timestamp | 0 |  |  | null | 期初加权价更新时间(废弃) |
| 7 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 10 | fdevcost | 研发费用 | bpchar | 1 |  | √ | '0' | 研发费用,枚举: 1 :是 0 :否 |
| 11 | fissystem | 系统生成 | bpchar | 1 |  | √ | '0' | 系统生成 |
| 12 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 13 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 14 | flot | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 15 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 17 | fassistpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 18 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 19 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 20 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 21 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 22 | fwarehouseid | 仓库(划分依据) | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 23 | fdividebasisid | 划分依据 | int8 | 64 |  | √ | 0 | [划分依据 cal_bd_dividebasis](../cal_files/cal_bd_dividebasis.md) |
| 24 | faccsysid | 核算体系 | int8 | 64 |  | √ | 0 | [核算体系 xkbd_accountingsys](../fibd_files/xkbd_accountingsys.md) |
| 25 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fcaldimensionvalue | 核算维度值(后台) | varchar | 100 |  | √ | ' ' | 核算维度值(后台) |
| 27 | fendqty | 期末加权数量(废弃) | numeric | 23 | 10 | √ | 0 | 期末加权数量(废弃) |
| 28 | fcosttypeid | 成本价类型 | int8 | 64 |  | √ | 0 | [成本价类型 cal_costlibrarytype](../cal_files/cal_costlibrarytype.md) |
| 29 | fenable | 使用状态 | bpchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | funitdate | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 31 | fdimlocationid | 仓位(核算维度) | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 32 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 33 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | [核算范围 cal_bd_calrange](../cal_files/cal_bd_calrange.md) |
| 34 | fstatus | 数据状态 | bpchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 35 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 37 | fdividebasisvalue | 划分依据值(后台) | varchar | 100 |  | √ | ' ' | 划分依据值(后台) |
| 38 | fbeginqty | 期初加权数量(废弃) | numeric | 23 | 10 | √ | 0 | 期初加权数量(废弃) |
| 39 | fstorageorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fisweightedavg | 加权平均价生成 | bpchar | 1 |  | √ | '0' | 加权平均价生成 |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 43 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 44 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 45 | fendunitcost | 期末加权价(废弃) | numeric | 23 | 10 | √ | 0 | 期末加权价(废弃) |
| 46 | fbeginunitcost | 期初加权价(废弃) | numeric | 23 | 10 | √ | 0 | 期初加权价(废弃) |
| 47 | funitcost | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 48 | fendcost | 期末加权总价(废弃) | numeric | 23 | 10 | √ | 0 | 期末加权总价(废弃) |
| 49 | fcalpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 cal_bd_calpolicy](../cal_files/cal_bd_calpolicy.md) |
| 50 | flocationid | 仓位(划分依据) | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 51 | fmaterialcategoryid | 存货类别 | int8 | 64 |  | √ | 0 | [存货类别 bd_materialcategory](../basedata_files/bd_materialcategory.md) |
| 52 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 53 | fcost | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cal_costlibrary |  | fid |
| 2 | idx_cal_costlibrary_mat |  | fmaterialid |
| 3 | idx_cal_costlibrary_caldime |  | fcaldimensionid |
