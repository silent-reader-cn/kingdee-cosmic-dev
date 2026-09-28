# 盘点表F7-im_count_f7

## 盘点表F7-主表 t_im_invcountbill

- **表名称：** 盘点表F7-主表
- **表名：** t_im_invcountbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcounttype | fcounttype | varchar | 5 |  | √ | ' ' |  |
| 3 | fschemenumber | fschemenumber | varchar | 80 |  | √ | ' ' |  |
| 4 | foperatorid | foperatorid | int8 | 64 |  | √ | 0 |  |
| 5 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fschemeid | fschemeid | int8 | 64 |  | √ | 0 |  |
| 7 | ferrmsg_tag | ferrmsg_tag | text | 0 |  |  | null |  |
| 8 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 10 | fbackupcondition | fbackupcondition | varchar | 30 |  | √ | 'invacc' |  |
| 11 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 12 | faccessnode | faccessnode | varchar | 10 |  | √ | 'start' |  |
| 13 | fdefaultvalue | fdefaultvalue | varchar | 5 |  | √ | ' ' |  |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 16 | fdeptid | fdeptid | int8 | 64 |  | √ | 0 |  |
| 17 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcomment | fcomment | varchar | 512 |  | √ | ' ' |  |
| 19 | fchecker2ndid | fchecker2ndid | int8 | 64 |  | √ | 0 |  |
| 20 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 21 | foperatorgroupid | foperatorgroupid | int8 | 64 |  | √ | 0 |  |
| 22 | fcheckerid | fcheckerid | int8 | 64 |  | √ | 0 |  |
| 23 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 24 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 25 | fbillcretype | fbillcretype | bpchar | 1 |  | √ | '0' |  |
| 26 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 27 | fenablecheck | fenablecheck | bpchar | 1 |  | √ | '0' |  |
| 28 | fschemename | fschemename | varchar | 80 |  | √ | ' ' |  |
| 29 | ferrmsg | ferrmsg | varchar | 255 |  | √ | ' ' |  |
| 30 | fexcludeenddate | fexcludeenddate | bpchar | 1 |  | √ | '1' |  |
| 31 | fpushstatus | fpushstatus | varchar | 50 |  | √ | ' ' |  |
| 32 | finvaccdate | finvaccdate | timestamp | 0 |  |  | null |  |
| 33 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 34 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_invcountbill_org |  | forgid |
| 2 | t_im_invcountbill_pkey |  | fid |
| 3 | idx_im_invcountbill_billno |  | fbillno |
| 4 | idx_im_invcountbill_biztorgno |  | fbiztime,forgid,fbillno |
