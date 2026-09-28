# 市场费用申请单基础资料-ocmem_marketcost_applybd

## 市场费用申请单基础资料-主表 t_ocmem_mcost_apply

- **表名称：** 市场费用申请单基础资料-主表
- **表名：** t_ocmem_mcost_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexpenseprojectid | fexpenseprojectid | int8 | 64 |  | √ | 0 |  |
| 3 | fsumlinklocalborwamount | fsumlinklocalborwamount | numeric | 23 | 10 | √ | 0 |  |
| 4 | ftotalamount | ftotalamount | numeric | 23 | 10 | √ | 0 |  |
| 5 | fsumlinkborwamount | fsumlinkborwamount | numeric | 23 | 10 | √ | 0 |  |
| 6 | fcostdeptid | fcostdeptid | int8 | 64 |  | √ | 0 |  |
| 7 | fagencyid | fagencyid | int8 | 64 |  | √ | 0 |  |
| 8 | factivitytypeid | factivitytypeid | int8 | 64 |  | √ | 0 |  |
| 9 | fsupervisestatus | fsupervisestatus | bpchar | 1 |  | √ | 'A' |  |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fsumaccreimamont | fsumaccreimamont | numeric | 23 | 10 | √ | 0 |  |
| 12 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0 |  |
| 13 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 14 | fsumlalinkamtapproved | fsumlalinkamtapproved | numeric | 23 | 10 | √ | 0 |  |
| 15 | fexpensetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 16 | fmonthid | fmonthid | int8 | 64 |  | √ | 0 |  |
| 17 | fexratetableid | fexratetableid | int8 | 64 |  | √ | 0 |  |
| 18 | fsumlinkreimamont | fsumlinkreimamont | numeric | 23 | 10 | √ | 0 |  |
| 19 | fbillno | 申请单编号 | varchar | 100 |  | √ | ' ' | 申请单编号 |
| 20 | flocaltotalamtunapproved | flocaltotalamtunapproved | numeric | 23 | 10 | √ | 0 |  |
| 21 | fdeptid | 所属部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: |
| 23 | fpaymenthodid | fpaymenthodid | int8 | 64 |  | √ | 0 |  |
| 24 | fpayuserid | fpayuserid | int8 | 64 |  | √ | 0 |  |
| 25 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 26 | freason | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 27 | fbalancenumber | fbalancenumber | varchar | 100 |  | √ | ' ' |  |
| 28 | ftotalrefundamount | ftotalrefundamount | numeric | 23 | 10 | √ | 0 |  |
| 29 | flocalsumamount | flocalsumamount | numeric | 23 | 10 | √ | 0 |  |
| 30 | ftotalamtapproved | ftotalamtapproved | numeric | 23 | 10 | √ | 0 |  |
| 31 | faccounttypeid | faccounttypeid | int8 | 64 |  | √ | 0 |  |
| 32 | flocalsumlinkreimamt | flocalsumlinkreimamt | numeric | 23 | 10 | √ | 0 |  |
| 33 | fsettleorgid | fsettleorgid | int8 | 64 |  | √ | 0 |  |
| 34 | fbudget | fbudget | numeric | 23 | 10 | √ | 0 |  |
| 35 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 36 | fdimension | fdimension | bpchar | 1 |  | √ | ' ' |  |
| 37 | fcompanyid | fcompanyid | int8 | 64 |  | √ | 0 |  |
| 38 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | '2087111909521252352' |  |
| 39 | ftotalamtunapproved | ftotalamtunapproved | numeric | 23 | 10 | √ | 0 |  |
| 40 | factivityplanid | factivityplanid | int8 | 64 |  | √ | 0 |  |
| 41 | fbilldate | fbilldate | timestamp | 0 |  |  | null |  |
| 42 | flocalsumaccreimamt | flocalsumaccreimamt | numeric | 23 | 10 | √ | 0 |  |
| 43 | fsalesyearid | fsalesyearid | int8 | 64 |  | √ | 0 |  |
| 44 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 45 | fsumlinkamtapproved | fsumlinkamtapproved | numeric | 23 | 10 | √ | 0 |  |
| 46 | fprovinceid | fprovinceid | int8 | 64 |  | √ | 0 |  |
| 47 | forderchannelid | 客户 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 48 | fbudgetyearid | fbudgetyearid | int8 | 64 |  | √ | 0 |  |
| 49 | fshowreimbursebtn | fshowreimbursebtn | bpchar | 1 |  | √ | '0' |  |
| 50 | fcostcompanyid | fcostcompanyid | int8 | 64 |  | √ | 0 |  |
| 51 | ffreezedate | ffreezedate | timestamp | 0 |  |  | null |  |
| 52 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 53 | fsumaccborwamount | fsumaccborwamount | numeric | 23 | 10 | √ | 0 |  |
| 54 | fwarzoneid | fwarzoneid | int8 | 64 |  | √ | 0 |  |
| 55 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 56 | fbegindate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 57 | fparentexpenseid | fparentexpenseid | int8 | 64 |  | √ | 0 |  |
| 58 | fheadwriteoff | fheadwriteoff | bpchar | 1 |  | √ | ' ' |  |
| 59 | ffreezestatus | ffreezestatus | bpchar | 1 |  | √ | 'E' |  |
| 60 | fbasecurrencyid | fbasecurrencyid | int8 | 64 |  | √ | 0 |  |
| 61 | fexecstatus | fexecstatus | bpchar | 1 |  | √ | 'A' |  |
| 62 | fsalesmonthid | fsalesmonthid | int8 | 64 |  | √ | 0 |  |
| 63 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 64 | fsumacclocalborwamount | fsumacclocalborwamount | numeric | 23 | 10 | √ | 0 |  |
| 65 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 66 | freimburseway | freimburseway | bpchar | 1 |  | √ | 'A' |  |
| 67 | fclosereasonid | fclosereasonid | int8 | 64 |  | √ | 0 |  |
| 68 | flocalttamtapproved | flocalttamtapproved | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_mcost_apply |  | fid |
| 2 | idx_ocmem_mcost_fcust |  | forderchannelid |
| 3 | idx_ocmem_mcost_fbilldate |  | fbilldate |
| 4 | idx_ocmem_mcost_fdept |  | fdeptid |
| 5 | idx_ocmem_mcost_fbno |  | fbillno |
