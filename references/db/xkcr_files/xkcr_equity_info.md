# 初始权益信息-xkcr_equity_info

## 初始权益信息-主表 t_xkcr_equity

- **表名称：** 初始权益信息-主表
- **表名：** t_xkcr_equity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | finvestedcompany | 被投资公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcompany | 投资公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_equity_company |  | fcompany,finvestedcompany |
| 2 | pk_xkcr_equity |  | fid |

---

## 单据体-子表 t_xkcr_equity_detail

- **表名称：** 单据体-子表
- **表名：** t_xkcr_equity_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | frptitem | 报表项目编码 | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |
| 4 | fchangeddate | 变动日期 | timestamp | 0 |  |  | null | 变动日期 |
| 5 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fitemdatatype | 项目数据类型编码 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbd_rptitemdatatype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_equity_detail |  | fentryid |
| 2 | idx_xkcr_equity_detail_fid |  | fid |
