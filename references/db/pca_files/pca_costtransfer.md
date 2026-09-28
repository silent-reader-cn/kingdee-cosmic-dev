# 项目成本结转单-pca_costtransfer

## 成本要素明细-子表 t_pca_costtrf_pro_ele

- **表名称：** 成本要素明细-子表
- **表名：** t_pca_costtrf_pro_ele

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | feletrfbalance | 本次结转余额 | numeric | 23 | 10 | √ | 0 | 本次结转余额 |
| 2 | fconvsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fbaletotalamount | 总成本 | numeric | 23 | 10 | √ | 0 | 总成本 |
| 4 | feletrfamount | 本次结转成本 | numeric | 23 | 10 | √ | 0 | 本次结转成本 |
| 5 | feletotalamount | 可结转总成本 | numeric | 23 | 10 | √ | 0 | 可结转总成本 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | feletotaltrfamount | 已结转成本 | numeric | 23 | 10 | √ | 0 | 已结转成本 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fconvelementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 10 | feletotalnottrfamount | 未结转成本 | numeric | 23 | 10 | √ | 0 | 未结转成本 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_costtrf_pro_ele |  | fdetailid |
| 2 | idx_pca_costtrf_pro_ele_fentryid |  | fentryid,fseq |

---

## 项目明细-子表 t_pca_costtrf_pro

- **表名称：** 项目明细-子表
- **表名：** t_pca_costtrf_pro

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 3 | ftotalamount | 项目可结转总成本 | numeric | 23 | 10 | √ | 0 | 项目可结转总成本 |
| 4 | fpushamount | 本期下推金额 | numeric | 23 | 10 | √ | 0 | 本期下推金额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fprojectprocess | 完工进度(%) | numeric | 23 | 2 | √ | 0 | 完工进度(%) |
| 8 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fbaletotalamount | 项目总成本 | numeric | 23 | 10 | √ | 0 | 项目总成本 |
| 10 | ftotalnottrfamount | 未结转成本 | numeric | 23 | 10 | √ | 0 | 未结转成本 |
| 11 | fsrcbillsubid | 关联单据体内码 | int8 | 64 |  | √ | 0 | 关联单据体内码 |
| 12 | fbalanceid | 项目成本余额表id（可能被删） | int8 | 64 |  | √ | 0 | 项目成本余额表id（可能被删） |
| 13 | ftrfbalance | 本次结转余额 | numeric | 23 | 10 | √ | 0 | 本次结转余额 |
| 14 | ftrfamount | 本次结转成本 | numeric | 23 | 10 | √ | 0 | 本次结转成本 |
| 15 | fcostobjectid | 核算对象id | int8 | 64 |  | √ | 0 | 核算对象id |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | ftotaltrfamount | 已结转总成本 | numeric | 23 | 10 | √ | 0 | 已结转总成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_costtrf_pro_coid |  | fcostobjectid |
| 2 | pk_pca_costtrf_pro |  | fentryid |
| 3 | idx_pca_costtrf_pro_balance |  | fbalanceid |
| 4 | idx_pca_costtrf_pro_fid |  | fid,fseq |
| 5 | idx_pca_costtrf_pro_project |  | fprojectid |

---

## 项目成本结转单-主表 t_pca_costtrf

- **表名称：** 项目成本结转单-主表
- **表名：** t_pca_costtrf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 4 | fsrcbillno | 关联单据编码 | varchar | 255 |  | √ | ' ' | 关联单据编码 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsrcbillid | 关联单据内码 | int8 | 64 |  | √ | 0 | 关联单据内码 |
| 8 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | ftransfertype | 结转类型 | varchar | 50 |  | √ | ' ' | 结转类型,枚举: 1 :标准结转 2 :资产结转 |
| 13 | fsourcetype | 单据来源 | varchar | 50 |  | √ | ' ' | 单据来源,枚举: A :手工新增 B :项目收入成本结转单 |
| 14 | fcostaccountid | 项目核算主体 | int8 | 64 |  | √ | 0 | [项目核算主体 pca_costaccount](../pca_files/pca_costaccount.md) |
| 15 | fbookdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 16 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 17 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_costtrf_bno |  | fbillno |
| 2 | pk_pca_costtrf |  | fid |
| 3 | idx_pca_costrec_costaccount |  | fcostaccountid,fperiodid |
