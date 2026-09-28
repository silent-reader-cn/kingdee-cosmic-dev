# 合同收款匹配记录-conm_scmatch

## 合同收款匹配记录-主表 t_conm_scmatch

- **表名称：** 合同收款匹配记录-主表
- **表名：** t_conm_scmatch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwfseq | 匹配批号 | varchar | 80 |  | √ | ' ' | 匹配批号 |
| 3 | fcreatorid | 匹配人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 匹配日期 | timestamp | 0 |  |  | null | 匹配日期 |
| 6 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fheadwfinfo | 匹配详情 | varchar | 512 |  |  | null | 匹配详情 |
| 8 | fwfnumber | 匹配编码 | varchar | 80 |  | √ | ' ' | 匹配编码 |
| 9 | fheadwfinfo_tag | 匹配详情_详情 | text | 0 |  |  | null | 匹配详情_详情 |
| 10 | fwriteofftypeid | 核销类别 | int8 | 64 |  | √ | 0 | 核销类别 msmod_writeofftype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_scmatch_wfseq |  | fwfseq |
| 2 | pk_t_conm_scmatch |  | fid |

---

## 单据体-子表 t_conm_scmatchentry

- **表名称：** 单据体-子表
- **表名：** t_conm_scmatchentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassbillid | 收款单ID | int8 | 64 |  | √ | 0 | 收款单ID |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | famount | 合同收款金额 | numeric | 23 | 10 | √ | 0 | 合同收款金额 |
| 5 | fassbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | fassamount | 收款单应收金额 | numeric | 23 | 10 | √ | 0 | 收款单应收金额 |
| 7 | fassbillno | 收款单号 | varchar | 80 |  | √ | ' ' | 收款单号 |
| 8 | fasscurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 9 | fassbilltype | 辅方单据 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 10 | fmainwfinfo_tag | 合同匹配详情_详情 | text | 0 |  |  | null | 合同匹配详情_详情 |
| 11 | fbillno | 销售合同编号 | varchar | 80 |  | √ | ' ' | 销售合同编号 |
| 12 | fqty | 合同本次匹配金额 | numeric | 23 | 10 | √ | 0 | 合同本次匹配金额 |
| 13 | fassbillentryid | 收款明细ID | int8 | 64 |  | √ | 0 | 收款明细ID |
| 14 | fmainwfinfo | 合同匹配详情 | varchar | 512 |  |  | null | 合同匹配详情 |
| 15 | fasswfinfo_tag | 收款单匹配详情_详情 | text | 0 |  |  | null | 收款单匹配详情_详情 |
| 16 | fassentryseq | fassentryseq | int8 | 64 |  | √ | 0 |  |
| 17 | fentryseq | 收款计划序号 | int8 | 64 |  | √ | 0 | 收款计划序号 |
| 18 | fbillentryid | 收款计划ID | int8 | 64 |  | √ | 0 | 收款计划ID |
| 19 | fbizdate | 签订日期 | timestamp | 0 |  |  | null | 签订日期 |
| 20 | fassqty | 收款单本次匹配金额 | numeric | 23 | 10 | √ | 0 | 收款单本次匹配金额 |
| 21 | fbillid | 销售合同ID | int8 | 64 |  | √ | 0 | 销售合同ID |
| 22 | fasswfinfo | 收款单匹配详情 | varchar | 512 |  |  | null | 收款单匹配详情 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 25 | fbilltype | 主方单据 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 26 | fcustomerid | 付款客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_scmatchentry_fid |  | fid |
| 2 | pk_t_conm_scmatchentry |  | fentryid |
| 3 | idx_conm_scmatchentry_fbillno |  | fbillno |
