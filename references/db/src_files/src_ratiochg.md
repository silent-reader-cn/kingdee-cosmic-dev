# 定标份额变更-src_ratiochg

## 标的分录-子表 t_src_ratiochgentry

- **表名称：** 标的分录-子表
- **表名：** t_src_ratiochgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | 原单分录ID | varchar | 50 |  | √ | ' ' | 原单分录ID |
| 3 | fmaterialid | 标的编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fbizamount | 商务评分价格 | numeric | 23 | 10 | √ | 0 | 商务评分价格 |
| 5 | fentrystatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :待报价 B :已报价 C :已开标 D :已关闭 E :已定标 F :已签约 G :暂存 |
| 6 | frebate | 返点(%) | numeric | 23 | 10 | √ | 0 | 返点(%) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fbrand | 品牌 | varchar | 50 |  | √ | ' ' | 品牌 |
| 9 | fresult | 定标结果 | bpchar | 1 |  | √ | ' ' | 定标结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐/门槛未达标 7 :资审/评标不合格 |
| 10 | famount | 未税金额 | numeric | 23 | 10 | √ | 0 | 未税金额 |
| 11 | fpurlistid | 标的ID | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 12 | fbidmaterialid | 寻源标的 | int8 | 64 |  | √ | 0 | [标的档案 src_material](../src_files/src_material.md) |
| 13 | fmaterialnane | 标的名称 | varchar | 100 |  | √ | ' ' | 标的名称 |
| 14 | fcompkey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 15 | fturns | 轮次 | varchar | 2 |  | √ | ' ' | 轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) |
| 16 | fpackageid | 标段ID | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 17 | fdctamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 18 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 19 | fisnew | 是否供应商新增 | bpchar | 1 |  | √ | '0' | 是否供应商新增 |
| 20 | forderratio | 份额(%)(变更前) | numeric | 23 | 10 | √ | 0 | 份额(%)(变更前) |
| 21 | forderrationew | 份额(%)(变更后) | numeric | 23 | 10 | √ | 0 | 份额(%)(变更后) |
| 22 | fmaterialmodel | 规格型号 | varchar | 1024 |  | √ | ' ' | 规格型号 |
| 23 | fpercent | fpercent | numeric | 23 | 10 | √ | 0 |  |
| 24 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 25 | fdctrate | 折扣率(%) | numeric | 23 | 10 | √ | 0 | 折扣率(%) |
| 26 | fprojectid | 招标项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 27 | fpackagename | 标段 | varchar | 50 |  | √ | ' ' | 标段 |
| 28 | fdescription | 物料描述 | varchar | 1024 |  | √ | ' ' | 物料描述 |
| 29 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0 | 实际单价 |
| 30 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 31 | fdecrease | 降幅(%) | numeric | 23 | 10 | √ | 0 | 降幅(%) |
| 32 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 33 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | fbilltype | 单据类型 | bpchar | 1 |  | √ | ' ' | 单据类型,枚举: 1 :采购清单 2 :供应商报价单 3 :线上议价单 4 :线下议价单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_ratiochgentry_fid |  | fid |
| 2 | pk_src_ratiochgentry |  | fentryid |

---

## 定标份额变更-主表 t_src_ratiochg

- **表名称：** 定标份额变更-主表
- **表名：** t_src_ratiochg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 3 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :处理中 C :已处理 |
| 7 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 8 | fsumqty | 合计数量 | numeric | 23 | 10 | √ | 0 | 合计数量 |
| 9 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 10 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | [寻源项目变更F7 src_bidchangef7](../pds_files/src_bidchangef7.md) |
| 11 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 12 | fsumamount | 合计金额 | numeric | 23 | 10 | √ | 0 | 合计金额 |
| 13 | fsumtaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 14 | fsumtax | 合计税额 | numeric | 23 | 10 | √ | 0 | 合计税额 |
| 15 | fisadd | 是否允许供应商新增标的 | bpchar | 1 |  | √ | '0' | 是否允许供应商新增标的 |
| 16 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | ftaxtype | 计税类型 | varchar | 30 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 19 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 20 | fissrc | 是否采购端 | bpchar | 1 |  | √ | '0' | 是否采购端 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_ratiochg_entitykey |  | fentitykey |
| 2 | idx_src_ratiochg_parent |  | fparentid |
| 3 | pk_src_ratiochg |  | fid |
