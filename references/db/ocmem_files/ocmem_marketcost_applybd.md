# 市场费用申请单基础资料-ocmem_marketcost_applybd

## 市场费用申请单基础资料-主表 t_ocmem_mcost_apply

- **表名称：** 市场费用申请单基础资料-主表
- **表名：** t_ocmem_mcost_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexpenseprojectid | fexpenseprojectid | int8 | 64 |  | √ | 0 |  |
| 3 | ftotalamtunapproved | ftotalamtunapproved | numeric | 23 | 10 | √ | 0 |  |
| 4 | ftotalamount | ftotalamount | numeric | 23 | 10 | √ | 0 |  |
| 5 | fcostdeptid | fcostdeptid | int8 | 64 |  | √ | 0 |  |
| 6 | fagencyid | fagencyid | int8 | 64 |  | √ | 0 |  |
| 7 | factivityplanid | factivityplanid | int8 | 64 |  | √ | 0 |  |
| 8 | factivitytypeid | factivitytypeid | int8 | 64 |  | √ | 0 |  |
| 9 | fbilldate | fbilldate | timestamp | 0 |  |  | null |  |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fsalesyearid | fsalesyearid | int8 | 64 |  | √ | 0 |  |
| 12 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 13 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 14 | fprovinceid | fprovinceid | int8 | 64 |  | √ | 0 |  |
| 15 | forderchannelid | 客户 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 16 | fexpensetypeid | 费用类型 | int8 | 64 |  | √ | 0 | 营销费用类型 ocdbd_expensetype |
| 17 | fbudgetyearid | fbudgetyearid | int8 | 64 |  | √ | 0 |  |
| 18 | fmonthid | fmonthid | int8 | 64 |  | √ | 0 |  |
| 19 | fshowreimbursebtn | fshowreimbursebtn | bpchar | 1 |  | √ | '0' |  |
| 20 | fcostcompanyid | fcostcompanyid | int8 | 64 |  | √ | 0 |  |
| 21 | fbillno | 申请单编号 | varchar | 100 |  | √ | ' ' | 申请单编号 |
| 22 | ffreezedate | ffreezedate | timestamp | 0 |  |  | null |  |
| 23 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 24 | fdeptid | 所属部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fwarzoneid | fwarzoneid | int8 | 64 |  | √ | 0 |  |
| 26 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: |
| 27 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 28 | fbegindate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 29 | fparentexpenseid | fparentexpenseid | int8 | 64 |  | √ | 0 |  |
| 30 | fpaymenthodid | fpaymenthodid | int8 | 64 |  | √ | 0 |  |
| 31 | fpayuserid | fpayuserid | int8 | 64 |  | √ | 0 |  |
| 32 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 33 | freason | freason | varchar | 1000 |  | √ | ' ' |  |
| 34 | fheadwriteoff | fheadwriteoff | bpchar | 1 |  | √ | ' ' |  |
| 35 | ffreezestatus | ffreezestatus | bpchar | 1 |  | √ | 'E' |  |
| 36 | fbalancenumber | fbalancenumber | varchar | 100 |  | √ | ' ' |  |
| 37 | ftotalrefundamount | ftotalrefundamount | numeric | 23 | 10 | √ | 0 |  |
| 38 | fexecstatus | fexecstatus | bpchar | 1 |  | √ | 'A' |  |
| 39 | ftotalamtapproved | ftotalamtapproved | numeric | 23 | 10 | √ | 0 |  |
| 40 | fsalesmonthid | fsalesmonthid | int8 | 64 |  | √ | 0 |  |
| 41 | faccounttypeid | faccounttypeid | int8 | 64 |  | √ | 0 |  |
| 42 | fsettleorgid | fsettleorgid | int8 | 64 |  | √ | 0 |  |
| 43 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 44 | fbudget | fbudget | numeric | 23 | 10 | √ | 0 |  |
| 45 | freimburseway | freimburseway | bpchar | 1 |  | √ | 'A' |  |
| 46 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 47 | fdimension | fdimension | bpchar | 1 |  | √ | ' ' |  |
| 48 | fcompanyid | fcompanyid | int8 | 64 |  | √ | 0 |  |

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
