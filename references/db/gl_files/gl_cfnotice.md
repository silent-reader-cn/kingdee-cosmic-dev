# 现金流量通知单-gl_cfnotice

## 现金流量通知单-主表 t_gl_cfnotice

- **表名称：** 现金流量通知单-主表
- **表名：** t_gl_cfnotice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsourceid | fsourceid | int8 | 64 |  | √ | 0 |  |
| 4 | famount | 主表项目金额 | numeric | 19 | 6 | √ | 0.000000 | 主表项目金额 |
| 5 | fpeerorgid | 对方公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fentrydc | 方向 | bpchar | 1 |  | √ | 'i' | 方向,枚举: i :现金流入 o :现金流出 b :流入流出 |
| 8 | fvoucherentryid | 凭证分录 | int8 | 64 |  | √ | 0 | 凭证分录 |
| 9 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbillno | 通知单单号 | varchar | 100 |  | √ | ' ' | 通知单单号 |
| 12 | fvoucherid | 凭证ID | int8 | 64 |  | √ | 0 | 凭证ID |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fmaincfitemid | 主表项目 | int8 | 64 |  | √ | 0 | 现金流量项目 gl_cashflowitem |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fcheckerid | 勾稽人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fsendorgid | 发送方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fsendbookid | 发送方账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fbookstypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 22 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 23 | fcheckout | 解除结账校验 | bpchar | 1 |  | √ | '0' | 解除结账校验,枚举: 0 :否 1 :是 |
| 24 | freceivebookid | 接收方账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 25 | freceiveorgid | 接收方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fdesc | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 27 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 28 | fpeerentryid | fpeerentryid | int8 | 64 |  | √ | 0 |  |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 31 | fnoticetype | 通知单类型 | bpchar | 1 |  | √ | '0' | 通知单类型,枚举: 1 :发送 0 :接收 |
| 32 | fcheckstatus | 勾稽 | bpchar | 1 |  | √ | '0' | 勾稽,枚举: 0 :未勾稽 1 :勾稽 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_cfnotice_status |  | fcheckstatus,forgid,fbookstypeid |
| 2 | idx_gl_cfnotice_vchentryid |  | fvoucherentryid |
| 3 | idx_gl_cfnotice_vchid |  | fvoucherid |
| 4 | t_gl_cfnotice_pkey |  | fid |
| 5 | idx_gl_cfnotice |  | forgid,fbookstypeid,fbookeddate |
