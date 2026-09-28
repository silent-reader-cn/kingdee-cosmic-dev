# 研发费用核算单-rdem_costrecord

## 成本要素明细-子表 t_pca_costrec_bill_ele

- **表名称：** 成本要素明细-子表
- **表名：** t_pca_costrec_bill_ele

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fconvsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 2 | feleprice | 单位成本 | numeric | 23 | 10 | √ | 0 | 单位成本 |
| 3 | feletotalcost | 总成本 | numeric | 23 | 10 | √ | 0 | 总成本 |
| 4 | felecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | feleqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fiscommonmatcost | 是否通用料成本 | bpchar | 1 |  | √ | '0' | 是否通用料成本 |
| 8 | feleprojecttotalcost | 项目总成本 | numeric | 23 | 10 | √ | 0 | 项目总成本 |
| 9 | feleorigamount | 原始金额 | numeric | 23 | 10 | √ | 0 | 原始金额 |
| 10 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 11 | fconvelementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 13 | felebaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_costrec_bill_ele |  | fdetailid |
| 2 | idx_pca_costrec_bill_ele_fentryid |  | fentryid |

---

## 业务明细关联信息-子表 t_pca_costrec_bill_rel

- **表名称：** 业务明细关联信息-子表
- **表名：** t_pca_costrec_bill_rel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 3 | frelbillid | 业务单据id | int8 | 64 |  | √ | 0 | 业务单据id |
| 4 | frelbillentryid | 业务单据体id | int8 | 64 |  | √ | 0 | 业务单据体id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | frelbillentryseq | 业务单据体序号 | int4 | 32 |  | √ | 0 | 业务单据体序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_costrec_bill_rel_fentryid |  | fentryid |
| 2 | pk_pca_costrec_bill_rel |  | fdetailid |

---

## 业务单据明细信息-子表 t_pca_costrec_bill

- **表名称：** 业务单据明细信息-子表
- **表名：** t_pca_costrec_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | fbigintfield | fbigintfield | int8 | 64 |  | √ | 0 |  |
| 4 | fassgrpid | 核算维度值 | int8 | 64 |  | √ | 0 | null 002 |
| 5 | fsrcbillid | 来源单据(体)内码 | int8 | 64 |  | √ | 0 | 来源单据(体)内码 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | ftotalcost | 总成本 | numeric | 23 | 10 | √ | 0 | 总成本 |
| 9 | faccountviewid | 会计科目 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 10 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 11 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fprice | 单位成本 | numeric | 23 | 10 | √ | 0 | 单位成本 |
| 13 | fsrcbilldate | fsrcbilldate | timestamp | 0 |  |  | null |  |
| 14 | fsrcbillentryseq | 来源单据体序号 | int4 | 32 |  | √ | 0 | 来源单据体序号 |
| 15 | fchangedcosttype | 项目成本变动类型 | varchar | 50 |  | √ | ' ' | 项目成本变动类型,枚举: 0 :减 1 :增 2 :不影响 |
| 16 | fprojecttotalcost | 项目总成本 | numeric | 23 | 10 | √ | 0 | 项目总成本 |
| 17 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 18 | forigamount | 原始金额 | numeric | 23 | 10 | √ | 0 | 原始金额 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 21 | fcommonmatcost | 通用料成本 | numeric | 23 | 10 | √ | 0 | 通用料成本 |
| 22 | facctviewbaltype | 金额类型 | varchar | 50 |  | √ | ' ' | 金额类型,枚举: 1 :实际损益发生额 2 :借方 3 :贷方 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_costrec_bill_fid |  | fid,fseq |
| 2 | pk_pca_costrec_bill |  | fentryid |
| 3 | idx_pca_costrec_bill_accountview |  | faccountviewid |

---

## 研发费用核算单-主表 t_pca_costrec

- **表名称：** 研发费用核算单-主表
- **表名：** t_pca_costrec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fcollplanid | 成本来源设置 | int8 | 64 |  | √ | 0 | 成本来源设置 |
| 3 | fsrcbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 4 | fsrcsrcmasterid | 来源单据的源单内码 | int8 | 64 |  | √ | 0 | 来源单据的源单内码 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fsysbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fsrcsystype | 来源业务系统 | varchar | 50 |  | √ | ' ' | 来源业务系统,枚举: 1 :总账 2 :费用核算 3 :存货核算 4 :实际成本核算 5 :应付款管理 6 :自定义 7 :异构系统 8 :研发费用管理 |
| 9 | fcostaccountid | 项目核算主体 | int8 | 64 |  | √ | 0 | [项目核算主体 pca_costaccount](../pca_files/pca_costaccount.md) |
| 10 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 13 | fbillprojectid | PLM项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 14 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fsrcbillid | 来源主单据内码 | int8 | 64 |  | √ | 0 | 来源主单据内码 |
| 17 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 19 | facacostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 20 | fbillprojecttaskid | PLM项目任务 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 21 | fadminorgid | 部门 | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 22 | fprojectgroupid | 项目分类 | int8 | 64 |  | √ | 0 | [项目分类 bd_projectkind](../basedata_files/bd_projectkind.md) |
| 23 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [项目成本核算对象 pca_costobject](../pca_files/pca_costobject.md) |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fsrcbilltypeid | 业务单据类型 | varchar | 255 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_costrec_bno |  | fbillno |
| 2 | idx_pca_costrec_costobject |  | fcostaccountid,fperiodid,fcostobjectid |
| 3 | pk_pca_costrec |  | fid |
| 4 | idx_pca_costrec_calorg |  | fcalorgid |
