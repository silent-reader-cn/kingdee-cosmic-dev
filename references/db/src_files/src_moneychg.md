# 定标金额变更-src_moneychg

## 签约分录-子表 t_src_moneychgsign

- **表名称：** 签约分录-子表
- **表名：** t_src_moneychgsign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsuppliertype | 供应商类别2 | varchar | 30 |  | √ | ' ' | 供应商类别2,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :正式供应商 |
| 2 | fsignrate | 分配比例(%) | numeric | 23 | 10 | √ | 0 | 分配比例(%) |
| 3 | fsignsupplierid | 签约供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 4 | fsignamount | 中标未税金额 | numeric | 23 | 10 | √ | 0 | 中标未税金额 |
| 5 | fsigntaxamount | 中标含税金额 | numeric | 23 | 10 | √ | 0 | 中标含税金额 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_moneychgsign_eid |  | fentryid |
| 2 | pk_src_moneychgsign |  | fdetailid |

---

## 供应商分录-子表 t_src_moneychgentry

- **表名称：** 供应商分录-子表
- **表名：** t_src_moneychgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 中标含税金额(原) | numeric | 23 | 10 | √ | 0 | 中标含税金额(原) |
| 3 | fuparentid | 元数据ID | varchar | 50 |  | √ | ' ' | 元数据ID |
| 4 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 5 | ftaxamount1 | 中标含税金额(新) | numeric | 23 | 10 | √ | 0 | 中标含税金额(新) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | famount | 中标未税金额(原) | numeric | 23 | 10 | √ | 0 | 中标未税金额(原) |
| 8 | fcontractamount | 签约中标未税金额 | numeric | 23 | 10 | √ | 0 | 签约中标未税金额 |
| 9 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 10 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 11 | famount1 | 中标未税金额(新) | numeric | 23 | 10 | √ | 0 | 中标未税金额(新) |
| 12 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 13 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 14 | fcontracttaxamount | 签约中标含税金额 | numeric | 23 | 10 | √ | 0 | 签约中标含税金额 |
| 15 | forderratio | 未税占比(%) | numeric | 23 | 10 | √ | 0 | 未税占比(%) |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | forderratio1 | 含税占比(%) | numeric | 23 | 10 | √ | 0 | 含税占比(%) |
| 18 | fcontracttype | 签约属性 | bpchar | 1 |  | √ | ' ' | 签约属性,枚举: 1 :2方 2 :3方 3 :4方 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_moneychgentry_fid |  | fid |
| 2 | pk_src_moneychgentry |  | fentryid |

---

## 定标金额变更-主表 t_src_moneychg

- **表名称：** 定标金额变更-主表
- **表名：** t_src_moneychg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 3 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fisproject | 按项目汇总(定标汇总) | bpchar | 1 |  | √ | '0' | 按项目汇总(定标汇总) |
| 6 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :处理中 C :已处理 |
| 8 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 9 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 10 | fiscategory | 按品类汇总 | bpchar | 1 |  | √ | '0' | 按品类汇总 |
| 11 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | [寻源项目变更F7 src_bidchangef7](../pds_files/src_bidchangef7.md) |
| 12 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 13 | fsumamount | 预估含税采购金额 | numeric | 23 | 10 | √ | 0 | 预估含税采购金额 |
| 14 | fispackage | 按标段汇总 | bpchar | 1 |  | √ | '0' | 按标段汇总 |
| 15 | fisprice | 基于未税单价进行计算 | bpchar | 1 |  | √ | '0' | 基于未税单价进行计算 |
| 16 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_moneychg |  | fid |
| 2 | idx_src_moneychg_fpid |  | fparentid |
