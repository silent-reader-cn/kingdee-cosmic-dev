# 定标变更分析-src_decisionchgf7

## 定标变更分析-主表 t_src_decisionchgentry

- **表名称：** 定标变更分析-主表
- **表名：** t_src_decisionchgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpricenew | 未税单价(变更后) | numeric | 23 | 10 | √ | 0 | 未税单价(变更后) |
| 3 | ftaxrate | 税率(%)(变更前) | numeric | 23 | 10 | √ | 0 | 税率(%)(变更前) |
| 4 | fcfmqtynew | 定标数量(变更后) | numeric | 23 | 10 | √ | 0 | 定标数量(变更后) |
| 5 | frebate | frebate | numeric | 23 | 10 | √ | 0 |  |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | fresult | 定标结果(变更前) | varchar | 30 |  | √ | ' ' | 定标结果(变更前),枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐 9 :预中标 7 :资审不合格 |
| 8 | fcategorynewid | fcategorynewid | int8 | 64 |  | √ | 0 |  |
| 9 | fpurlistid | 标的ID | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 10 | ftaxitemnew | 税率(变更后) | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 11 | fcfmqty | 定标数量(变更前) | numeric | 23 | 10 | √ | 0 | 定标数量(变更前) |
| 12 | fmaterialnane | 标的名称 | varchar | 255 |  | √ | ' ' | 标的名称 |
| 13 | fdescriptionnew | fdescriptionnew | varchar | 1024 |  | √ | ' ' |  |
| 14 | fcompkey | fcompkey | varchar | 30 |  | √ | ' ' |  |
| 15 | ftaxpricenew | 含税单价(变更后) | numeric | 23 | 10 | √ | 0 | 含税单价(变更后) |
| 16 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 17 | fmaterialnanenew | fmaterialnanenew | varchar | 255 |  | √ | ' ' |  |
| 18 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 19 | fisnew | 是否修改 | bpchar | 1 |  | √ | '0' | 是否修改 |
| 20 | ftaxratenew | 税率(%)(变更后) | numeric | 23 | 10 | √ | 0 | 税率(%)(变更后) |
| 21 | fbaseunitid | fbaseunitid | int8 | 64 |  | √ | 0 |  |
| 22 | fmaterialmodel | 规格型号 | varchar | 1024 |  | √ | ' ' | 规格型号 |
| 23 | ftaxamount | 价税合计(变更前) | numeric | 23 | 10 | √ | 0 | 价税合计(变更前) |
| 24 | fqty | 数量(变更前) | numeric | 23 | 10 | √ | 0 | 数量(变更前) |
| 25 | fdctrate | fdctrate | numeric | 23 | 10 | √ | 0 |  |
| 26 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 27 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 28 | fpackagename | 标段名称 | varchar | 50 |  | √ | ' ' | 标段名称 |
| 29 | fdescription | 物料描述 | varchar | 1024 |  | √ | ' ' | 物料描述 |
| 30 | factprice | factprice | numeric | 23 | 10 | √ | 0 |  |
| 31 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 32 | fmaterialmodelnew | fmaterialmodelnew | varchar | 1024 |  | √ | ' ' |  |
| 33 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 bos_user :内部员工 src_supplier_tmp :临时供应商 bd_supplier :正式供应商 |
| 34 | ftax | ftax | numeric | 23 | 10 | √ | 0 |  |
| 35 | ftaxamountnew | 价税合计(变更后) | numeric | 23 | 10 | √ | 0 | 价税合计(变更后) |
| 36 | fqtynew | 数量(变更后) | numeric | 23 | 10 | √ | 0 | 数量(变更后) |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | frank | 排名 | int4 | 32 |  | √ | 0 | 排名 |
| 39 | fsrcentryid | fsrcentryid | varchar | 50 |  | √ | ' ' |  |
| 40 | fmaterialid | 标的编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 41 | fbizamount | fbizamount | numeric | 23 | 10 | √ | 0 |  |
| 42 | fentrystatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :待报价 B :已报价 C :已开标 D :已关闭 E :已定标 F :已签约 G :暂存 H :已弃标 I :已废标 J :已终止 |
| 43 | fbrand | fbrand | varchar | 50 |  | √ | ' ' |  |
| 44 | ftaxprice | 含税单价(变更前) | numeric | 23 | 10 | √ | 0 | 含税单价(变更前) |
| 45 | famount | 未税金额(变更前) | numeric | 23 | 10 | √ | 0 | 未税金额(变更前) |
| 46 | fprice | 未税单价(变更前) | numeric | 23 | 10 | √ | 0 | 未税单价(变更前) |
| 47 | fbidmaterialid | fbidmaterialid | int8 | 64 |  | √ | 0 |  |
| 48 | fturns | 轮次 | varchar | 2 |  | √ | ' ' | 轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) 7 :议价(6) 8 :议价(7) 9 :议价(8) 10 :议价(9) |
| 49 | fdctamount | fdctamount | numeric | 23 | 10 | √ | 0 |  |
| 50 | forderratio | 份额(%)(变更前) | numeric | 23 | 10 | √ | 0 | 份额(%)(变更前) |
| 51 | forderrationew | 份额(%)(变更后) | numeric | 23 | 10 | √ | 0 | 份额(%)(变更后) |
| 52 | fpercent | fpercent | numeric | 23 | 10 | √ | 0 |  |
| 53 | fmaterialnewid | fmaterialnewid | int8 | 64 |  | √ | 0 |  |
| 54 | fcurrency | 报价币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 55 | fdecrease | fdecrease | numeric | 23 | 10 | √ | 0 |  |
| 56 | ftaxitemid | 税率(变更前) | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 57 | fresultnew | 定标结果(变更后) | varchar | 30 |  | √ | ' ' | 定标结果(变更后),枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐 9 :预中标 7 :资审不合格 |
| 58 | famountnew | 未税金额(变更后) | numeric | 23 | 10 | √ | 0 | 未税金额(变更后) |
| 59 | funitnewid | funitnewid | int8 | 64 |  | √ | 0 |  |
| 60 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 61 | fbilltype | fbilltype | varchar | 30 |  | √ | ' ' |  |

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

## 定标变更分析-多语言表 t_src_decisionchgentry_l

- **表名称：** 定标变更分析-多语言表
- **表名：** t_src_decisionchgentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
