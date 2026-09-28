# 质量变更审批-srm_qualitycfm

## 质量变更审批-分表 t_pur_quality_a

- **表名称：** 质量变更审批-分表
- **表名：** t_pur_quality_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 4 | forigin | forigin | bpchar | 1 |  | √ | ' ' |  |
| 5 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 6 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 7 | fcfmopinion | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 8 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 9 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 10 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 11 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_quality_a_ftime |  | fcreatetime |
| 2 | t_pur_quality_a_pkey |  | fid |

---

## 质量变更审批-主表 t_pur_quality

- **表名称：** 质量变更审批-主表
- **表名：** t_pur_quality

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fsubject | 变更主题 | varchar | 255 |  | √ | ' ' | 变更主题 |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 5 | fmaterialid | fmaterialid | int8 | 64 |  | √ | 0 |  |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 9 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 10 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 11 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 12 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :同意 C :驳回 |
| 13 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 14 | fchgtypeid | fchgtypeid | int8 | 64 |  | √ | 0 |  |
| 15 | fcategoryid | fcategoryid | int8 | 64 |  | √ | 0 |  |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_quality_pkey |  | fid |
| 2 | idx_pur_quality_fbilldate |  | fbilldate |
| 3 | idx_pur_quality_fbillno |  | fbillno |
