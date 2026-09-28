# 中标金额汇总-src_decisionsum_sup

## 附件-附件表 t_src_decisionsumsign_fj1

- **表名称：** 附件-附件表
- **表名：** t_src_decisionsumsign_fj1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_decisumsign_fj1_did |  | fdetailid |
| 2 | idx_src_decisumsign_fj1_bid |  | fbasedataid |
| 3 | pk_src_decisionsumsign_fj1 |  | fpkid |

---

## 供应商分录-子表 t_src_decisionsumsup

- **表名称：** 供应商分录-子表
- **表名：** t_src_decisionsumsup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frank | 排名 | int8 | 64 |  | √ | 0 | 排名 |
| 3 | fmaxamount | 标杆未税金额 | numeric | 23 | 10 | √ | 0 | 标杆未税金额 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fresult | 是否中标 | varchar | 30 |  | √ | ' ' | 是否中标,枚举: 1 :中标 2 :未中标 3 :预中标 |
| 6 | famount | 中标未税金额 | numeric | 23 | 10 | √ | 0 | 中标未税金额 |
| 7 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 8 | fpreorderratio1 | 预定标含税占比(%) | numeric | 23 | 10 | √ | 0 | 预定标含税占比(%) |
| 9 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 10 | floctaxamount | 报价含税金额 | numeric | 23 | 10 | √ | 0 | 报价含税金额 |
| 11 | fpreorderratio | 预定标未税占比(%) | numeric | 23 | 10 | √ | 0 | 预定标未税占比(%) |
| 12 | forderratio | 中标未税占比(%) | numeric | 23 | 10 | √ | 0 | 中标未税占比(%) |
| 13 | fbudgetamount | fbudgetamount | numeric | 23 | 10 | √ | 0 |  |
| 14 | fpreamount | 预定标未税金额 | numeric | 23 | 10 | √ | 0 | 预定标未税金额 |
| 15 | ftaxamountrate | 含税价差率(%) | numeric | 23 | 10 | √ | 0 | 含税价差率(%) |
| 16 | fpretaxamount | 预定标含税金额 | numeric | 23 | 10 | √ | 0 | 预定标含税金额 |
| 17 | fcontracttype | 签约属性 | bpchar | 1 |  | √ | ' ' | 签约属性,枚举: 1 :2方 2 :3方 3 :4方 |
| 18 | ftaxamount | 中标含税金额 | numeric | 23 | 10 | √ | 0 | 中标含税金额 |
| 19 | famountrate | 未税价差率(%) | numeric | 23 | 10 | √ | 0 | 未税价差率(%) |
| 20 | fphone | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 21 | fmaxtaxamount | 标杆含税金额 | numeric | 23 | 10 | √ | 0 | 标杆含税金额 |
| 22 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 23 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 24 | femail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 25 | fbidcount | 中标标的数 | int4 | 32 |  | √ | 0 | 中标标的数 |
| 26 | fcontractamount | 签约中标未税金额 | numeric | 23 | 10 | √ | 0 | 签约中标未税金额 |
| 27 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 28 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 bos_user :内部员工 src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 29 | flocamount | 报价未税金额 | numeric | 23 | 10 | √ | 0 | 报价未税金额 |
| 30 | ftaxamountdiff | 含税价差 | numeric | 23 | 10 | √ | 0 | 含税价差 |
| 31 | fcontracttaxamount | 签约中标含税金额 | numeric | 23 | 10 | √ | 0 | 签约中标含税金额 |
| 32 | famountdiff | 未税价差 | numeric | 23 | 10 | √ | 0 | 未税价差 |
| 33 | flinkman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | forderratio1 | 中标含税占比(%) | numeric | 23 | 10 | √ | 0 | 中标含税占比(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_decisionsumsup_fcid |  | fcategoryid |
| 2 | idx_src_decisionsumsup_fsup |  | fsupplierid |
| 3 | idx_src_decisionsumsup_fpro |  | fprojectid |
| 4 | idx_src_decisionsumsup_fpid |  | fparentid |
| 5 | idx_src_decisionsumsup_fid |  | fid |
| 6 | pk_src_decisionsumsup |  | fentryid |
| 7 | idx_src_decisionsumsup_fpag |  | fpackageid |

---

## 签约分录-子表 t_src_decisionsumsign

- **表名称：** 签约分录-子表
- **表名：** t_src_decisionsumsign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsuppliertype | 供应商类别2 | varchar | 30 |  | √ | ' ' | 供应商类别2,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :正式供应商 |
| 2 | fsignrate | 分配比例(%) | numeric | 23 | 10 | √ | 0 | 分配比例(%) |
| 3 | fsignamount | 中标未税金额 | numeric | 23 | 10 | √ | 0 | 中标未税金额 |
| 4 | fsigntaxamount | 中标含税金额 | numeric | 23 | 10 | √ | 0 | 中标含税金额 |
| 5 | fcontractid | 签约合同号 | int8 | 64 |  | √ | 0 | [采购合同 pds_purcontract](../pds_files/pds_purcontract.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_decisionsumsign_fcid |  | fcontractid |
| 2 | idx_src_decisionsumsign_fsup |  | fsupplierid |
| 3 | idx_src_decisionsumsign_feid |  | fentryid |
| 4 | pk_src_decisionsumsign |  | fdetailid |

---

## 中标金额汇总-主表 t_src_decisionwin

- **表名称：** 中标金额汇总-主表
- **表名：** t_src_decisionwin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 3 | fisproject | 按项目汇总(定标汇总) | bpchar | 1 |  | √ | '0' | 按项目汇总(定标汇总) |
| 4 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 5 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 6 | forigin | 发起方 | varchar | 30 |  | √ | ' ' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 7 | fiscategory | 按品类汇总 | bpchar | 1 |  | √ | '0' | 按品类汇总 |
| 8 | fispackage | 按标段汇总 | bpchar | 1 |  | √ | '0' | 按标段汇总 |
| 9 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 10 | fisprice | 基于未税单价进行计算 | bpchar | 1 |  | √ | '0' | 基于未税单价进行计算 |
| 11 | fisallsupplier | 是否包含未中标供应商 | bpchar | 1 |  | √ | '0' | 是否包含未中标供应商 |
| 12 | fbudgetamount | 预估采购总金额(未税) | numeric | 23 | 10 | √ | 0 | 预估采购总金额(未税) |
| 13 | fsumtype | 计算方式 | varchar | 30 |  | √ | '1' | 计算方式,枚举: 1 :按标的份额(数量)计算 2 :手工录入供应商中标金额 |
| 14 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_decisionwin |  | fid |
| 2 | idx_src_decisionwin_fpid |  | fparentid |
