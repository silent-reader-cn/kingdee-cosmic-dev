# 改善结果-adm_improveresult

## 改善结果-主表 t_pur_improve

- **表名称：** 改善结果-主表
- **表名：** t_pur_improve

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freplydate | freplydate | timestamp | 0 |  |  | null |  |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fconfirmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待处理 B :打回 C :改善中 D :改善提交 E :改善通过 F :改善驳回 |
| 5 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | fother | fother | varchar | 510 |  |  | ' ' |  |
| 7 | ffinishstatus | 改善结果 | bpchar | 1 |  | √ | ' ' | 改善结果,枚举: A :待处理 B :同意 C :驳回 |
| 8 | fauditstatus | 审批结果 | bpchar | 1 |  | √ | ' ' | 审批结果,枚举: A :待处理 B :审批通过 C :驳回终止 |
| 9 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 10 | fquality | fquality | varchar | 510 |  |  | ' ' |  |
| 11 | fsrcbillname | fsrcbillname | varchar | 80 |  | √ | ' ' |  |
| 12 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fremark | fremark | varchar | 2000 |  | √ | ' ' |  |
| 15 | fsubject | fsubject | varchar | 255 |  | √ | ' ' |  |
| 16 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 17 | fsupservice | 供应商改善回复（服务） | varchar | 510 |  |  | ' ' | 供应商改善回复（服务） |
| 18 | fexpectdate | fexpectdate | timestamp | 0 |  |  | null |  |
| 19 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 20 | fdescription | fdescription | varchar | 510 |  |  | ' ' |  |
| 21 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 22 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 23 | ffinishdate | 改善完成时间 | timestamp | 0 |  |  | null | 改善完成时间 |
| 24 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 25 | fsupquality | 供应商改善回复（品质） | varchar | 510 |  |  | ' ' | 供应商改善回复（品质） |
| 26 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :同意 C :驳回 |
| 27 | fservice | fservice | varchar | 510 |  |  | ' ' |  |
| 28 | flinkmanid | flinkmanid | int8 | 64 |  | √ | 0 |  |
| 29 | fimprovetypeid | fimprovetypeid | int8 | 64 |  | √ | 0 |  |
| 30 | fsupreply | 供应商改善回复 | varchar | 510 |  |  | ' ' | 供应商改善回复 |
| 31 | fsupother | 供应商改善回复（其他） | varchar | 510 |  |  | ' ' | 供应商改善回复（其他） |
| 32 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_improve_fbillno |  | fbillno |
| 2 | t_pur_improve_pkey |  | fid |
| 3 | idx_pur_improve_fbilldate |  | fbilldate |

---

## 改善结果-分表 t_pur_improve_a

- **表名称：** 改善结果-分表
- **表名：** t_pur_improve_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapproverid | fapproverid | int8 | 64 |  | √ | 0 |  |
| 3 | fapprovedate | fapprovedate | timestamp | 0 |  |  | null |  |
| 4 | fremark | fremark | varchar | 2000 |  | √ | ' ' |  |
| 5 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 6 | fhandledate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 7 | finvaliddate | finvaliddate | timestamp | 0 |  |  | null |  |
| 8 | fsrcbillno | fsrcbillno | varchar | 50 |  | √ | ' ' |  |
| 9 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 10 | fsrcbillid | fsrcbillid | varchar | 50 |  | √ | ' ' |  |
| 11 | fcfmopinion | fcfmopinion | varchar | 255 |  | √ | ' ' |  |
| 12 | fhandlerid | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 14 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 15 | fauditopinion | fauditopinion | varchar | 255 |  | √ | ' ' |  |
| 16 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 18 | forigin | forigin | bpchar | 1 |  | √ | ' ' |  |
| 19 | finvalidid | finvalidid | int8 | 64 |  | √ | 0 |  |
| 20 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 22 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_improve_a_ftime |  | fcreatetime |
| 2 | t_pur_improve_a_pkey |  | fid |
