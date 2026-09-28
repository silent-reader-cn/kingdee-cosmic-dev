# 标段金额汇总(后台元数据)-src_pkgamount_meta

## 标段金额汇总(后台元数据)-主表 t_src_pkgamount

- **表名称：** 标段金额汇总(后台元数据)-主表
- **表名：** t_src_pkgamount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | frank | 首轮排名 | int8 | 64 |  | √ | 0 | 首轮排名 |
| 3 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 4 | fentrystatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :待报价 B :已报价 C :已开标 D :已关闭 |
| 5 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 6 | fresult | 定标结果 | varchar | 30 |  | √ | ' ' | 定标结果,枚举: 1 :中标 2 :候选 3 :落标 5 :培养 |
| 7 | fsysresult | 推荐结果 | varchar | 30 |  | √ | ' ' | 推荐结果,枚举: 1 :中标 2 :候选 3 :落标 5 :培养 |
| 8 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 9 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 10 | fpkgamount | 标段未税金额 | numeric | 23 | 10 | √ | 0 | 标段未税金额 |
| 11 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 12 | fpkgtaxamount | 标段含税金额 | numeric | 23 | 10 | √ | 0 | 标段含税金额 |
| 13 | fturns | 轮次 | varchar | 2 |  | √ | ' ' | 轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) |
| 14 | forderratio | 份额(%) | numeric | 23 | 10 | √ | 0 | 份额(%) |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_pkgamount |  | fentryid |
| 2 | idx_src_pkgamount_fid |  | fid |
