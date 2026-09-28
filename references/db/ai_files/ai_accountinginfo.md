# AI记账日志-ai_accountinginfo

## AI记账日志-主表 t_ai_accountinginfo

- **表名称：** AI记账日志-主表
- **表名：** t_ai_accountinginfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcbillnumber | 来源单据编码 | varchar | 2000 |  | √ | ' ' | 来源单据编码 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | faccountingmodel | AI记账模型 | int8 | 64 |  | √ | 0 | [AI记账模型 ai_accountingmodel](../ai_files/ai_accountingmodel.md) |
| 5 | fgptinput |  | varchar | 2000 |  | √ | ' ' |  |
| 6 | ftraceid | traceid | varchar | 32 |  | √ | ' ' | traceid |
| 7 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fsrcbillid | 来源单据id | varchar | 1000 |  | √ | ' ' | 来源单据id |
| 10 | fgptinput_tag | 详情 | text | 0 |  |  | null | 详情 |
| 11 | fgptoutput_tag | 详情 | text | 0 |  |  | null | 详情 |
| 12 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 13 | fsrcbill | 来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fgptoutput |  | varchar | 2000 |  | √ | ' ' |  |
| 17 | fparamname | AI大模型 | varchar | 100 |  | √ | ' ' | AI大模型 |
| 18 | fmodelname | AI大模型（废弃） | varchar | 50 |  | √ | ' ' | AI大模型（废弃）,枚举: 0 :通义plus |
| 19 | fperiod | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 20 | facctbook | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_accountinginfo |  | fsrcbill |
| 2 | pk_t_ai_accountinginfo |  | fid |
