# 商务得分(后台元数据)-src_manualscore_meta

## 商务得分(后台元数据)-主表 t_src_manualscore

- **表名称：** 商务得分(后台元数据)-主表
- **表名：** t_src_manualscore

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 3 | fbizamount | 商务价格 | numeric | 23 | 10 | √ | 0 | 商务价格 |
| 4 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 5 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 6 | fpurlistid | 标的名称 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fbizscore | 商务标得分 | numeric | 23 | 10 | √ | 0 | 商务标得分 |
| 9 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_manualscore_fid |  | fid |
| 2 | pk_src_manualscore |  | fentryid |
