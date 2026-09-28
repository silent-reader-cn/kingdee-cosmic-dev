# 开标任务-pds_bidopendetail

## 开标任务-主表 t_pds_bidopendetail

- **表名称：** 开标任务-主表
- **表名：** t_pds_bidopendetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 3 | fterminatedate | 终止时间 | timestamp | 0 |  |  | null | 终止时间 |
| 4 | fissend | 是否发送 | bpchar | 1 |  | √ | '0' | 是否发送 |
| 5 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 6 | fbidderid | 当前处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fbidopendate | 开标时间 | timestamp | 0 |  |  | null | 开标时间 |
| 8 | fopentype | 开标类型 | bpchar | 1 |  | √ | ' ' | 开标类型,枚举: 1 :开资审标 2 :开技术标/全部开标 3 :开商务标 |
| 9 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | 标段名称 pds_packagef7 |
| 10 | fisbidopen | 是否已开标 | bpchar | 1 |  | √ | '0' | 是否已开标 |
| 11 | fsenddate | 发送时间 | timestamp | 0 |  |  | null | 发送时间 |
| 12 | fentityid | 来源单据标识 | varchar | 50 |  | √ | ' ' | 来源单据标识 |
| 13 | fisterminate | 是否终止 | bpchar | 1 |  | √ | '0' | 是否终止 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_bidopendetail_bid |  | fbidderid |
| 2 | idx_pds_bidopendetail_sid |  | fsupplierid |
| 3 | idx_pds_bidopendetail_oid |  | fopentype |
| 4 | idx_pds_bidopendetail_pid |  | fprojectid |
| 5 | pk_pds_bidopendetail |  | fid |
| 6 | idx_pds_bidopendetail_pakid |  | fpackageid |
