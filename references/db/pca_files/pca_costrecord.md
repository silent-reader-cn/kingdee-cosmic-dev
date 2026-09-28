# 项目成本核算单-pca_costrecord

## 业务单据明细信息-子表 t_pca_costrec_bill

- **表名称：** 业务单据明细信息-子表
- **表名：** t_pca_costrec_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | fbigintfield | fbigintfield | int8 | 64 |  | √ | 0 |  |
| 4 | fsrcbillid | 来源单据(体)内码 | int8 | 64 |  | √ | 0 | 来源单据(体)内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | ftotalcost | 总成本 | numeric | 23 | 10 | √ | 0 | 总成本 |
| 8 | faccountviewid | 会计科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 9 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 10 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fprice | 单位成本 | numeric | 23 | 10 | √ | 0 | 单位成本 |
| 12 | fsrcbilldate | fsrcbilldate | timestamp | 0 |  |  | null |  |
| 13 | fsrcbillentryseq | 来源单据体序号 | int4 | 32 |  | √ | 0 | 来源单据体序号 |
| 14 | fchangedcosttype | 项目成本变动类型 | varchar | 50 |  | √ | ' ' | 项目成本变动类型,枚举: 0 :减 1 :增 2 :不影响 |
| 15 | fprojecttotalcost | 项目总成本 | numeric | 23 | 10 | √ | 0 | 项目总成本 |
| 16 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 19 | fcommonmatcost | 通用料成本 | numeric | 23 | 10 | √ | 0 | 通用料成本 |
| 20 | facctviewbaltype | 科目余额类型 | varchar | 50 |  | √ | ' ' | 科目余额类型,枚举: 1 :实际损益发生额 |

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

## 成本要素明细-子表 t_pca_costrec_bill_ele

- **表名称：** 成本要素明细-子表
- **表名：** t_pca_costrec_bill_ele

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fiscommonmatcost | 是否通用料成本 | bpchar | 1 |  | √ | '0' | 是否通用料成本 |
| 2 | fconvsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | feleprojecttotalcost | 项目总成本 | numeric | 23 | 10 | √ | 0 | 项目总成本 |
| 4 | feleprice | 单位成本 | numeric | 23 | 10 | √ | 0 | 单位成本 |
| 5 | feletotalcost | 总成本 | numeric | 23 | 10 | √ | 0 | 总成本 |
| 6 | felecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 7 | feleqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | fconvelementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 12 | felebaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

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

## 项目成本核算单-主表 t_pca_costrec

- **表名称：** 项目成本核算单-主表
- **表名：** t_pca_costrec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsrcbillid | 来源主单据内码 | int8 | 64 |  | √ | 0 | 来源主单据内码 |
| 7 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcollplanid | 成本来源设置 | int8 | 64 |  | √ | 0 | 成本来源设置 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fsrcbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fsrcsystype | 来源业务系统 | varchar | 50 |  | √ | ' ' | 来源业务系统,枚举: 1 :总账 2 :费用报销 3 :存货核算 4 :实际成本核算 5 :应付 |
| 14 | fcostaccountid | 项目核算主体 | int8 | 64 |  | √ | 0 | 项目核算主体 pca_costaccount |
| 15 | fprojectgroupid | 项目分类 | int8 | 64 |  | √ | 0 | 项目分类 bd_projectkind |
| 16 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 项目成本核算对象 pca_costobject |
| 17 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fsrcbilltypeid | 业务单据类型 | varchar | 255 |  | √ | ' ' | 主实体对象 bos_entityobject |

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
