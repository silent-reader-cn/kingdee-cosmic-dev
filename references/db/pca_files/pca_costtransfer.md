# 项目成本结转单-pca_costtransfer

## 成本要素明细-子表 t_pca_costtrf_pro_ele

- **表名称：** 成本要素明细-子表
- **表名：** t_pca_costtrf_pro_ele

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fconvsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 2 | feletrfamount | 本次结转成本 | numeric | 23 | 10 | √ | 0 | 本次结转成本 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fconvelementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

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

## 项目成本结转单-主表 t_pca_costtrf

- **表名称：** 项目成本结转单-主表
- **表名：** t_pca_costtrf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fcostaccountid | 项目核算主体 | int8 | 64 |  | √ | 0 | 项目核算主体 pca_costaccount |
| 11 | fbookdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 12 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 13 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

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

---

## 项目明细-子表 t_pca_costtrf_pro

- **表名称：** 项目明细-子表
- **表名：** t_pca_costtrf_pro

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectprocess | 完工进度(%) | numeric | 23 | 2 | √ | 0 | 完工进度(%) |
| 3 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbalanceid | 项目成本余额表id | int8 | 64 |  | √ | 0 | 项目成本余额表id |
| 7 | ftrfamount | 本次结转成本 | numeric | 23 | 10 | √ | 0 | 本次结转成本 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_costtrf_pro |  | fentryid |
| 2 | idx_pca_costtrf_pro_balance |  | fbalanceid |
| 3 | idx_pca_costtrf_pro_fid |  | fid,fseq |
| 4 | idx_pca_costtrf_pro_project |  | fprojectid |
