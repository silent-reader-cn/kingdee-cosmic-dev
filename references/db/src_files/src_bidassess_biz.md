# 评标结果(后台元数据)-src_bidassess_biz

## 评标结果(后台元数据)-主表 t_src_comparesum

- **表名称：** 评标结果(后台元数据)-主表
- **表名：** t_src_comparesum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | frank | 排名 | int8 | 64 |  | √ | 0 | 排名 |
| 3 | fothscore | 商务综合得分 | numeric | 23 | 10 | √ | 0 | 商务综合得分 |
| 4 | fpkggroupid | 标段分组 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 5 | fbizamount | 商务价格 | numeric | 23 | 10 | √ | 0 | 商务价格 |
| 6 | fbasetype | 评标类型 | bpchar | 1 |  | √ | ' ' | 评标类型,枚举: 1 :技术标 2 :商务标 3 :商务综合 |
| 7 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 8 | fresult | 推荐结果 | bpchar | 1 |  | √ | ' ' | 推荐结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐/门槛未达标 7 :资审/评标不合格 9 :预中标 0 :流标 |
| 9 | fsuppliercode | 供应商代码 | varchar | 100 |  | √ | ' ' | 供应商代码 |
| 10 | fpurlistid | 标的 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 11 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 12 | floctaxamount | 含税金额合计 | numeric | 23 | 10 | √ | 0 | 含税金额合计 |
| 13 | fbizscore | 商务标得分 | numeric | 23 | 10 | √ | 0 | 商务标得分 |
| 14 | favgvalue | 平均值 | numeric | 23 | 10 | √ | 0 | 平均值 |
| 15 | fbasevalue | 基准值 | numeric | 19 | 6 | √ | 0 | 基准值 |
| 16 | fmaxvalue | 最大值 | numeric | 23 | 10 | √ | 0 | 最大值 |
| 17 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 18 | fsumscore | 总得分 | numeric | 23 | 10 | √ | 0 | 总得分 |
| 19 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 20 | findextypeid | 指标类型 | int8 | 64 |  | √ | 0 | [指标类型 src_indexclass](../src_files/src_indexclass.md) |
| 21 | fminvalue | 最小值 | numeric | 23 | 10 | √ | 0 | 最小值 |
| 22 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 23 | ftecscore | 技术标得分 | numeric | 23 | 10 | √ | 0 | 技术标得分 |
| 24 | flocamount | 未税金额合计 | numeric | 23 | 10 | √ | 0 | 未税金额合计 |
| 25 | fpurlistid0 | 原始的采购清单ID | int8 | 64 |  | √ | 0 | 原始的采购清单ID |
| 26 | fsupplierip | 供应商IP | varchar | 100 |  | √ | ' ' | 供应商IP |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fmaterialname | 标的名称 | varchar | 255 |  | √ | ' ' | 标的名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_comparesum_fpurlistid |  | fpurlistid |
| 2 | idx_src_comparesum_fid |  | fid |
| 3 | idx_src_comparesum_fsupplierid |  | fsupplierid |
| 4 | idx_src_comparesum_fparentid |  | fparentid |
| 5 | idx_src_comparesum_fpackageid |  | fpackageid |
| 6 | pk_src_comparesum |  | fentryid |
| 7 | idx_src_comparesum_fpkggroupid |  | fpkggroupid |
