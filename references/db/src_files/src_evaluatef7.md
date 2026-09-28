# 专家考评F7-src_evaluatef7

## 专家考评F7-主表 t_src_evaluate

- **表名称：** 专家考评F7-主表
- **表名：** t_src_evaluate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 发起组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :处理中 C :已处理 D :已终止 E :已废标 |
| 4 | fisevaluatepush | 是否已下达 | bpchar | 1 |  | √ | '0' | 是否已下达 |
| 5 | fsrctypeid | 寻源流程 | int8 | 64 |  | √ | 0 | [流程配置 pds_flowconfig](../pds_files/pds_flowconfig.md) |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fscoretype | 评分方式 | bpchar | 1 |  | √ | ' ' | 评分方式,枚举: 1 :线上评标 2 :线下评标 |
| 8 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 9 | fopentype | fopentype | bpchar | 1 |  | √ | ' ' |  |
| 10 | fdatefrom | 考评期间从 | timestamp | 0 |  |  | null | 考评期间从 |
| 11 | fishidesupplier | 评分时是否隐藏专家姓名 | bpchar | 1 |  | √ | '0' | 评分时是否隐藏专家姓名 |
| 12 | fbiztypeid | 考评类型 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 13 | fmanagetype | 管理方式 | bpchar | 1 |  | √ | ' ' | 管理方式,枚举: 1 :按项目 2 :按标段 3 :按标的 |
| 14 | fbillno | 考评单号 | varchar | 50 |  | √ | ' ' | 考评单号 |
| 15 | fbidname | 考评名称 | varchar | 300 |  | √ | ' ' | 考评名称 |
| 16 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 17 | fdateto | 考评期间至 | timestamp | 0 |  |  | null | 考评期间至 |
| 18 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 19 | fperiodid | 考评周期 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 20 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 21 | fischanged | fischanged | bpchar | 1 |  | √ | '1' |  |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :重新审核 |
| 23 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 26 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 27 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 28 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 29 | fsourcetypeid | fsourcetypeid | int8 | 64 |  | √ | 0 |  |
| 30 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_evaluate_number |  | fbillno |
| 2 | pk_src_evaluate |  | fid |
