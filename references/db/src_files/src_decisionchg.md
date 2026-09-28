# 定标结果和份额变更-src_decisionchg

## 标的分录-子表 t_src_decisionchgentry

- **表名称：** 标的分录-子表
- **表名：** t_src_decisionchgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpricenew | 未税单价(变更后) | numeric | 23 | 10 | √ | 0 | 未税单价(变更后) |
| 3 | ftaxrate | 税率(%)(变更前) | numeric | 23 | 10 | √ | 0 | 税率(%)(变更前) |
| 4 | fcfmqtynew | 定标数量(变更后) | numeric | 23 | 10 | √ | 0 | 定标数量(变更后) |
| 5 | frebate | 返点(%) | numeric | 23 | 10 | √ | 0 | 返点(%) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fresult | 定标结果(变更前) | varchar | 30 |  | √ | ' ' | 定标结果(变更前),枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐 7 :资审不合格 0 :流标 |
| 8 | fcategorynewid | 品类(变更后) | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 9 | fpurlistid | 标的ID | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 10 | ftaxitemnew | 税率(变更后) | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 11 | fcfmqty | 定标数量(变更前) | numeric | 23 | 10 | √ | 0 | 定标数量(变更前) |
| 12 | fmaterialnane | 标的名称(变更前) | varchar | 255 |  | √ | ' ' | 标的名称(变更前) |
| 13 | fdescriptionnew | 物料描述(变更后) | varchar | 1024 |  | √ | ' ' | 物料描述(变更后) |
| 14 | fcompkey | 组件标识 | varchar | 30 |  | √ | ' ' | 组件标识 |
| 15 | ftaxpricenew | 含税单价(变更后) | numeric | 23 | 10 | √ | 0 | 含税单价(变更后) |
| 16 | fpackageid | 标段ID | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 17 | fmaterialnanenew | 标的名称(变更后) | varchar | 255 |  | √ | ' ' | 标的名称(变更后) |
| 18 | fcategoryid | 品类(变更前) | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 19 | fisnew | 是否修改 | bpchar | 1 |  | √ | '0' | 是否修改 |
| 20 | ftaxratenew | 税率(%)(变更后) | numeric | 23 | 10 | √ | 0 | 税率(%)(变更后) |
| 21 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fmaterialmodel | 规格型号(变更前) | varchar | 1024 |  | √ | ' ' | 规格型号(变更前) |
| 23 | ftaxamount | 价税合计(变更前) | numeric | 23 | 10 | √ | 0 | 价税合计(变更前) |
| 24 | fqty | 数量(变更前) | numeric | 23 | 10 | √ | 0 | 数量(变更前) |
| 25 | fdctrate | 折扣率(%) | numeric | 23 | 10 | √ | 0 | 折扣率(%) |
| 26 | fprojectid | 寻源项目ID | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 27 | funitid | 计量单位(变更前) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 28 | fpackagename | 标段 | varchar | 50 |  | √ | ' ' | 标段 |
| 29 | fdescription | 物料描述(变更前) | varchar | 1024 |  | √ | ' ' | 物料描述(变更前) |
| 30 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0 | 实际单价 |
| 31 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 32 | fmaterialmodelnew | 规格型号(变更后) | varchar | 1024 |  | √ | ' ' | 规格型号(变更后) |
| 33 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 34 | ftax | ftax | numeric | 23 | 10 | √ | 0 |  |
| 35 | ftaxamountnew | 价税合计(变更后) | numeric | 23 | 10 | √ | 0 | 价税合计(变更后) |
| 36 | fqtynew | 数量(变更后) | numeric | 23 | 10 | √ | 0 | 数量(变更后) |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | frank | 排名 | int4 | 32 |  | √ | 0 | 排名 |
| 39 | fsrcentryid | 源单分录ID | varchar | 50 |  | √ | ' ' | 源单分录ID |
| 40 | fmaterialid | 标的编码(变更前) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 41 | fbizamount | 商务评分价格 | numeric | 23 | 10 | √ | 0 | 商务评分价格 |
| 42 | fentrystatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :待报价 B :已报价 C :已开标 D :已关闭 E :已定标 F :已签约 G :暂存 |
| 43 | fbrand | 品牌 | varchar | 50 |  | √ | ' ' | 品牌 |
| 44 | ftaxprice | 含税单价(变更前) | numeric | 23 | 10 | √ | 0 | 含税单价(变更前) |
| 45 | famount | 未税金额(变更前) | numeric | 23 | 10 | √ | 0 | 未税金额(变更前) |
| 46 | fprice | 未税单价(变更前) | numeric | 23 | 10 | √ | 0 | 未税单价(变更前) |
| 47 | fbidmaterialid | 寻源标的 | int8 | 64 |  | √ | 0 | 标的档案 src_material |
| 48 | fturns | 轮次 | varchar | 2 |  | √ | ' ' | 轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) |
| 49 | fdctamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 50 | forderratio | 份额(%)(变更前) | numeric | 23 | 10 | √ | 0 | 份额(%)(变更前) |
| 51 | forderrationew | 份额(%)(变更后) | numeric | 23 | 10 | √ | 0 | 份额(%)(变更后) |
| 52 | fpercent | fpercent | numeric | 23 | 10 | √ | 0 |  |
| 53 | fmaterialnewid | 标的编码(变更后) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 54 | fcurrency | 报价币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 55 | fdecrease | 降幅(%) | numeric | 23 | 10 | √ | 0 | 降幅(%) |
| 56 | ftaxitemid | 税率(变更前) | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 57 | fresultnew | 定标结果(变更后) | varchar | 30 |  | √ | ' ' | 定标结果(变更后),枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐 7 :资审不合格 0 :流标 |
| 58 | famountnew | 未税金额(变更后) | numeric | 23 | 10 | √ | 0 | 未税金额(变更后) |
| 59 | funitnewid | 计量单位(变更后) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 60 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 61 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: 1 :采购清单 2 :供应商报价单 3 :线上议价单 4 :线下议价单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_decisionchgentry_fid |  | fsupplierid |
| 2 | pk_src_decisionchgentry |  | fentryid |

---

## 定标结果和份额变更-主表 t_src_decisionchg

- **表名称：** 定标结果和份额变更-主表
- **表名：** t_src_decisionchg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 3 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :处理中 C :已处理 |
| 7 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 8 | fsumqty | 合计数量 | numeric | 23 | 10 | √ | 0 | 合计数量 |
| 9 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 10 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | 寻源项目变更F7 src_bidchangef7 |
| 11 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 12 | fsumamount | 合计金额 | numeric | 23 | 10 | √ | 0 | 合计金额 |
| 13 | fsumtaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 14 | fsumtax | 合计税额 | numeric | 23 | 10 | √ | 0 | 合计税额 |
| 15 | fisadd | 是否允许供应商新增标的 | bpchar | 1 |  | √ | '0' | 是否允许供应商新增标的 |
| 16 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 18 | ftaxtype | ftaxtype | bpchar | 1 |  | √ | ' ' |  |
| 19 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 20 | fissrc | 是否采购端 | bpchar | 1 |  | √ | '0' | 是否采购端 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_decisionchg |  | fid |
| 2 | idx_src_decisionchg_fbillno |  | fbillno |
