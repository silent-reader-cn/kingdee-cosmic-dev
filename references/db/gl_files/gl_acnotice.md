# 往来通知单-gl_acnotice

## 往来通知单-主表 t_gl_acnotice

- **表名称：** 往来通知单-主表
- **表名：** t_gl_acnotice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsourceid | fsourceid | int8 | 64 |  | √ | 0 |  |
| 4 | famount | 原币金额 | numeric | 19 | 6 | √ | 0.000000 | 原币金额 |
| 5 | fpeerorgid | 对方公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fentrydc | 方向 | varchar | 2 |  | √ | '1' | 方向,枚举: 1 :借 -1 :贷 |
| 8 | fvoucherentryid | 凭证分录 | int8 | 64 |  | √ | 0 | 凭证分录 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 11 | fbillno | 通知单单号 | varchar | 100 |  | √ | ' ' | 通知单单号 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fvoucherid | 凭证ID | int8 | 64 |  | √ | 0 | 凭证ID |
| 14 | faccountbookstypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 15 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :审核 |
| 16 | fassgrp | 核算维度 | varchar | 255 |  | √ | ' ' | 核算维度 |
| 17 | fcheckerid | 勾稽人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fsendorgid | 发送方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fsendbookid | 发送方账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 22 | fcheckout | 解除结账校验 | bpchar | 1 |  | √ | '0' | 解除结账校验,枚举: 0 :否 1 :是 |
| 23 | freceivebookid | 接收方账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 24 | freceiveorgid | 接收方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | flocamount | 本位币金额 | numeric | 19 | 6 | √ | 0.000000 | 本位币金额 |
| 26 | fpeerdesc | 对方凭证摘要 | varchar | 2000 |  | √ | ' ' | 对方凭证摘要 |
| 27 | fcreatime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | flocalcurid | 本位币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | fdesc | 摘要 | varchar | 1020 |  | √ | ' ' | 摘要 |
| 30 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fpeerentryid | fpeerentryid | int8 | 64 |  | √ | 0 |  |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 34 | fnoticetype | 通知单类型 | bpchar | 1 |  | √ | '1' | 通知单类型,枚举: 1 :发送 0 :接收 |
| 35 | fcheckstatus | 勾稽 | bpchar | 1 |  | √ | '0' | 勾稽,枚举: 0 :未勾稽 1 :勾稽 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_acnotice_pkey |  | fid |
| 2 | idx_gl_acnotice |  | forgid,faccountbookstypeid,fbookeddate |
| 3 | idx_gl_acnotice_account |  | faccountid,forgid,faccountbookstypeid,fnoticetype,fbookeddate |
| 4 | idx_gl_acnotice_vchid |  | fvoucherid |
| 5 | idx_gl_acnotice_status |  | fcheckstatus,forgid,faccountbookstypeid |
| 6 | idx_gl_acnotice_vchentryid |  | fvoucherentryid |
