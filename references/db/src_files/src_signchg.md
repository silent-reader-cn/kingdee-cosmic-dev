# 签约供应商变更（废弃）-src_signchg

## 附件-附件表 t_src_signchg_fj

- **表名称：** 附件-附件表
- **表名：** t_src_signchg_fj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_signchg_did |  | fdetailid |
| 2 | idx_src_signchg_bid |  | fbasedataid |
| 3 | pk_src_signchg_fj |  | fpkid |

---

## 供应商分录-子表 t_src_signchgentry

- **表名称：** 供应商分录-子表
- **表名：** t_src_signchgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 中标含税金额 | numeric | 23 | 10 | √ | 0 | 中标含税金额 |
| 3 | fuparentid | 元数据ID | varchar | 50 |  | √ | ' ' | 元数据ID |
| 4 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | famount | 中标未税金额 | numeric | 23 | 10 | √ | 0 | 中标未税金额 |
| 7 | fcontractamount | 签约中标未税金额 | numeric | 23 | 10 | √ | 0 | 签约中标未税金额 |
| 8 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 9 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :正式供应商 |
| 10 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 11 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 12 | fcontracttaxamount | 签约中标含税金额 | numeric | 23 | 10 | √ | 0 | 签约中标含税金额 |
| 13 | forderratio | 未税占比(%) | numeric | 23 | 10 | √ | 0 | 未税占比(%) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | forderratio1 | 含税占比(%) | numeric | 23 | 10 | √ | 0 | 含税占比(%) |
| 16 | fcontracttype | 签约属性 | bpchar | 1 |  | √ | ' ' | 签约属性,枚举: 1 :2方 2 :3方 3 :4方 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_signchgentry_fid |  | fid |
| 2 | pk_src_signchgentry |  | fentryid |

---

## 签约供应商变更（废弃）-主表 t_src_signchg

- **表名称：** 签约供应商变更（废弃）-主表
- **表名：** t_src_signchg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fisproject | 按项目汇总(定标汇总) | bpchar | 1 |  | √ | '0' | 按项目汇总(定标汇总) |
| 5 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :处理中 C :已处理 |
| 6 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 7 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 8 | fiscategory | 按品类汇总 | bpchar | 1 |  | √ | '0' | 按品类汇总 |
| 9 | fsumamount | 预估含税采购金额 | numeric | 23 | 10 | √ | 0 | 预估含税采购金额 |
| 10 | fispackage | 按标段汇总 | bpchar | 1 |  | √ | '0' | 按标段汇总 |
| 11 | fisprice | 基于未税单价进行计算 | bpchar | 1 |  | √ | '0' | 基于未税单价进行计算 |
| 12 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 13 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_signchg |  | fid |
| 2 | idx_src_signchg_pid |  | fparentid |

---

## 签约分录-子表 t_src_signchgsign

- **表名称：** 签约分录-子表
- **表名：** t_src_signchgsign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsuppliertype | 供应商类别2 | varchar | 30 |  | √ | ' ' | 供应商类别2,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :正式供应商 |
| 2 | fsignrate | 分配比例(%) | numeric | 23 | 10 | √ | 0 | 分配比例(%) |
| 3 | fsignsupplierid | 签约供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 4 | fsignamount | 中标未税金额 | numeric | 23 | 10 | √ | 0 | 中标未税金额 |
| 5 | fsigntaxamount | 中标含税金额 | numeric | 23 | 10 | √ | 0 | 中标含税金额 |
| 6 | fcontractid | 签约合同号 | int8 | 64 |  | √ | 0 | 采购合同 pds_purcontract |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fentryparentid1 | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_signchgsign |  | fdetailid |
| 2 | idx_src_signchgsign_eid |  | fentryid |
