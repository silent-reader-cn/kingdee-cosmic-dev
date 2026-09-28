# 更新确认单-cad_costupdateestablished

## 更新确认单-主表 t_cad_costupestbish

- **表名称：** 更新确认单-主表
- **表名：** t_cad_costupestbish

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftargetcosttypeid | ftargetcosttypeid | int8 | 64 |  | √ | 0 |  |
| 3 | fstatus | 单据状态 | varchar | 20 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :生效 |
| 4 | fsrccosttypeid | 源成本类型 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 5 | fperiodid | 生效期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 6 | feffecttime | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 7 | fenable | 使用状态 | varchar | 20 |  | √ | ' ' | 使用状态,枚举: 1 :可用 0 :禁用 |
| 8 | fnumber | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 9 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_costupestbish |  | fsrccosttypeid,feffecttime |
| 2 | t_cad_costupestbish_pkey |  | fid |

---

## 成本更新-子表 t_cad_costupestbish_cost

- **表名称：** 成本更新-子表
- **表名：** t_cad_costupestbish_cost

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | foldprice | 原标准单价 | numeric | 23 | 10 | √ | 0.0000000000 | 原标准单价 |
| 4 | fnewprice | 更新后单价 | numeric | 23 | 10 | √ | 0.0000000000 | 更新后单价 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fresourcebak | 资源 | int8 | 64 |  | √ | 0 | [资源维护(废弃) mpdm_resources](../mpdm_files/mpdm_resources.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fauxprop | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 10 | fsrctype | 来源类型 | varchar | 30 |  | √ | ' ' | 来源类型,枚举: 1 :成本更新单 2 :相关影响 |
| 11 | fmatversionid | 物料版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 12 | fsubmaterialbak | 子项物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 13 | fsubmatversbak | 子物料版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 14 | fsubauxpropertybak | 子物料辅助属性 | int8 | 64 |  | √ | 0 | [辅助属性定义 bd_auxproperty](../sbd_files/bd_auxproperty.md) |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fdiffprice | 差异 | numeric | 23 | 10 | √ | 0.0000000000 | 差异 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cad_costupestbish_cost |  | fid |
| 2 | index_cad_costupestbish_ct |  | fid,fmaterialid,felementid,fsubelementid |
| 3 | t_cad_costupestbish_cost_pkey |  | fentryid |

---

## 库存成本单据体-子表 t_cad_costupestbish_stor

- **表名称：** 库存成本单据体-子表
- **表名：** t_cad_costupestbish_stor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 库存数量 | numeric | 23 | 10 | √ | 0.0000000000 | 库存数量 |
| 3 | fstorbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | foldcost | 原库存成本 | numeric | 23 | 10 | √ | 0.0000000000 | 原库存成本 |
| 6 | fstornewprice | 更新后单价 | numeric | 23 | 10 | √ | 0.0000000000 | 更新后单价 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 9 | fstormatverisoin | 物料版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 10 | fstorauxprop | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fstorsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 12 | fstoroldprice | 原标准单价 | numeric | 23 | 10 | √ | 0.0000000000 | 原标准单价 |
| 13 | fcostaccountid | 账簿 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 14 | faccountorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fdiffcost | 变更差异 | numeric | 23 | 10 | √ | 0.0000000000 | 变更差异 |
| 16 | fsotrelementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fnewcost | 更新后成本 | numeric | 23 | 10 | √ | 0.0000000000 | 更新后成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_costupestbish_st |  | fid,faccountorgid,fcostaccountid,fwarehouseid,fmaterialid |
| 2 | t_cad_costupestbish_stor_pkey |  | fentryid |
| 3 | idx_cad_costupestbish_stor |  | fid |

---

## 库存成本单账簿单据体-子表 t_cad_costupestbish_acct

- **表名称：** 库存成本单账簿单据体-子表
- **表名：** t_cad_costupestbish_acct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facctauxprop | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 3 | facctnewprice | 更新后单价 | numeric | 23 | 10 | √ | 0.0000000000 | 更新后单价 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | facctmatversionid | 物料版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 6 | facctsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 7 | facctbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | facctcostaccountid | 账簿 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 9 | facctnewcost | 更新后成本 | numeric | 23 | 10 | √ | 0.0000000000 | 更新后成本 |
| 10 | facctqty | 库存数量 | numeric | 23 | 10 | √ | 0.0000000000 | 库存数量 |
| 11 | facctaccountorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | facctdiffcost | 变更差异 | numeric | 23 | 10 | √ | 0.0000000000 | 变更差异 |
| 13 | facctmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 14 | facctelementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | facctoldprice | 原标准单价 | numeric | 23 | 10 | √ | 0.0000000000 | 原标准单价 |
| 17 | facctoldcost | 原库存成本 | numeric | 23 | 10 | √ | 0.0000000000 | 原库存成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cad_costupestbish_acct |  | fid |
| 2 | index_cad_costupestbish_at |  | facctaccountorgid,facctcostaccountid,facctmaterialid |
| 3 | t_cad_costupestbish_acct_pkey |  | fentryid |

---

## 生产成本单据体-子表 t_cad_costupestbish_prod

- **表名称：** 生产成本单据体-子表
- **表名：** t_cad_costupestbish_prod

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostcenterid | 成本中心编码 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 3 | fsubelementid | 成本子要素编码 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 4 | fperiodid | 核算期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | fresourceid | 资源 | int8 | 64 |  | √ | 0 | [资源维护(废弃) mpdm_resources](../mpdm_files/mpdm_resources.md) |
| 6 | forgid | 核算组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | felementid | 成本要素编码 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 9 | fcalcbasis | 计算依据 | varchar | 30 |  | √ | ' ' | 计算依据,枚举: 001 :资源工时 002 :物料 003 :批次 |
| 10 | fcostlevel | 资源阶层 | varchar | 30 |  | √ | ' ' | 资源阶层,枚举: 2 :本阶 3 :下阶 |
| 11 | fproductcost | 原生产成本 | numeric | 23 | 10 | √ | 0.0000000000 | 原生产成本 |
| 12 | fupdatediff | 更新差异 | numeric | 23 | 10 | √ | 0.0000000000 | 更新差异 |
| 13 | fcostaccountid | 成本主体编码 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 14 | fupdatedcost | 更新后成本 | numeric | 23 | 10 | √ | 0.0000000000 | 更新后成本 |
| 15 | fcostobjectid | 成本核算对象编码 | int8 | 64 |  | √ | 0 | [成本核算对象 cad_costobjectf7](../aca_files/cad_costobjectf7.md) |
| 16 | fproauxptyid | 子物料辅助属性 | int8 | 64 |  | √ | 0 | [辅助属性定义 bd_auxproperty](../sbd_files/bd_auxproperty.md) |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fprosubmaterialid | 子项物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 19 | fpromatversionid | 子物料版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_costupe_prod |  | forgid,fcostcenterid,fcostobjectid |
| 2 | idx_cad_costupestbish_prod |  | fid |
| 3 | t_cad_costupestbish_prod_pkey |  | fentryid |
