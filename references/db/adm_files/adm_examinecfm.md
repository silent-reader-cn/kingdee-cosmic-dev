# 考核反馈-adm_examinecfm

## 考核反馈-分表 t_pur_examine_a

- **表名称：** 考核反馈-分表
- **表名：** t_pur_examine_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapproverid | fapproverid | int8 | 64 |  | √ | 0 |  |
| 3 | fapprovedate | fapprovedate | timestamp | 0 |  |  | null |  |
| 4 | fremark | fremark | varchar | 2000 |  | √ | ' ' |  |
| 5 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 6 | finvaliddate | finvaliddate | timestamp | 0 |  |  | null |  |
| 7 | fsrcbillno | fsrcbillno | varchar | 50 |  | √ | ' ' |  |
| 8 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 9 | fsrcbillid | fsrcbillid | varchar | 50 |  | √ | ' ' |  |
| 10 | fcfmopinion | 反馈意见 | varchar | 255 |  | √ | ' ' | 反馈意见 |
| 11 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 12 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 13 | fauditopinion | fauditopinion | varchar | 255 |  | √ | ' ' |  |
| 14 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 16 | forigin | forigin | bpchar | 1 |  | √ | ' ' |  |
| 17 | finvalidid | finvalidid | int8 | 64 |  | √ | 0 |  |
| 18 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 19 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 20 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_examine_a_ftime |  | fcreatetime |
| 2 | t_pur_examine_a_pkey |  | fid |

---

## 考核反馈-主表 t_pur_examine

- **表名称：** 考核反馈-主表
- **表名：** t_pur_examine

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 2000 |  | √ | ' ' |  |
| 3 | fexaminerid | fexaminerid | int8 | 64 |  | √ | 0 |  |
| 4 | fcurrid | fcurrid | int8 | 64 |  | √ | 0 |  |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fconfirmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待处理 B :打回 C :已确认 D :考核完成 |
| 8 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 10 | famount | famount | numeric | 19 | 6 | √ | 0.000000 |  |
| 11 | fdescription | fdescription | varchar | 510 |  |  | ' ' |  |
| 12 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 13 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 14 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 15 | fexamtypeid | fexamtypeid | int8 | 64 |  | √ | 0 |  |
| 16 | fcfmstatus | 反馈结果 | bpchar | 1 |  | √ | ' ' | 反馈结果,枚举: A :待反馈 B :同意 C :驳回 |
| 17 | fauditstatus | 考核结果 | bpchar | 1 |  | √ | ' ' | 考核结果,枚举: A :待处理 B :考核完成 C :作废 |
| 18 | fsrcbillname | fsrcbillname | varchar | 100 |  | √ | ' ' |  |
| 19 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_examine_pkey |  | fid |
| 2 | idx_pur_examine_fbillno |  | fbillno |
| 3 | idx_pur_examine_fbilldate |  | fbilldate |
