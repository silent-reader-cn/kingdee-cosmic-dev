# 寻源项目变更F7-src_bidchangef7

## 寻源项目变更F7-主表 t_src_bidchange

- **表名称：** 寻源项目变更F7-主表
- **表名：** t_src_bidchange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fbilldate | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 4 | fpurdeptid | fpurdeptid | int8 | 64 |  | √ | 0 |  |
| 5 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fapplyid | fapplyid | int8 | 64 |  | √ | 0 |  |
| 8 | fdemandid | fdemandid | int8 | 64 |  | √ | 0 |  |
| 9 | fpurgroupid | fpurgroupid | int8 | 64 |  | √ | 0 |  |
| 10 | fbiztypeid | fbiztypeid | int8 | 64 |  | √ | 0 |  |
| 11 | fpurdecision | fpurdecision | bpchar | 1 |  | √ | ' ' |  |
| 12 | fbillno | 变更单号 | varchar | 30 |  | √ | ' ' | 变更单号 |
| 13 | fremark | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 14 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 15 | ftemplateid | 变更类型 | int8 | 64 |  | √ | 0 | [组件模板配置 pds_tplconfig](../pds_files/pds_tplconfig.md) |
| 16 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [寻源项目 pds_projectf7](../pds_files/pds_projectf7.md) |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 21 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 22 | fdescription | 变更摘要 | varchar | 1020 |  | √ | ' ' | 变更摘要 |
| 23 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 24 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 25 | fisdemandpush | fisdemandpush | bpchar | 1 |  | √ | '0' |  |
| 26 | flevel | flevel | int8 | 64 |  | √ | 0 |  |
| 27 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 28 | fissuabnormal | fissuabnormal | bpchar | 1 |  | √ | '0' |  |
| 29 | fchangesource | fchangesource | bpchar | 1 |  | √ | '3' |  |
| 30 | fcurrentnode | fcurrentnode | int8 | 64 |  | √ | 0 |  |
| 31 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_bidchange_fprojectid |  | fprojectid |
| 2 | idx_src_bidchange_ftemplateid |  | ftemplateid |
| 3 | idx_src_bidchange_fparentid |  | fparentid |
| 4 | pk_src_bidchange |  | fid |
| 5 | idx_src_bidchange_fbillno |  | fbillno |
| 6 | idx_src_bidchange_fbilldate |  | fbilldate |
