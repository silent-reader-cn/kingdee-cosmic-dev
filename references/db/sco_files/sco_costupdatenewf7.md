# 更新申请单F7-sco_costupdatenewf7

## 更新申请单F7-主表 t_sco_costupdatenew

- **表名称：** 更新申请单F7-主表
- **表名：** t_sco_costupdatenew

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 3 | fresmatbyuseauxpt_tag | fresmatbyuseauxpt_tag | text | 0 |  |  | null |  |
| 4 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 5 | fupdatebillno | 更新编码 | varchar | 80 |  | √ | ' ' | 更新编码 |
| 6 | ftargetcosttype | 目标标准成本方案 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 7 | fresbynoref | fresbynoref | varchar | 2000 |  | √ | ' ' |  |
| 8 | fupdatestatus | 更新状态 | varchar | 30 |  | √ | ' ' | 更新状态,枚举: N :未完成 Y :已完成 |
| 9 | fresmatbyuseauxpt | fresmatbyuseauxpt | varchar | 2000 |  | √ | ' ' |  |
| 10 | fbillno | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 11 | fupdatecheckpass | fupdatecheckpass | bpchar | 1 |  | √ | '0' |  |
| 12 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 13 | fperiodid | fperiodid | int8 | 64 |  | √ | 0 |  |
| 14 | fbillstatus | fbillstatus | varchar | 30 |  | √ | ' ' |  |
| 15 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 16 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 17 | fsrccosttype | 源标准成本方案 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 18 | fisquickupdate | fisquickupdate | bpchar | 1 |  | √ | '0' |  |
| 19 | fiscalccurlevel | fiscalccurlevel | bpchar | 1 |  | √ | '0' |  |
| 20 | fisspecifymaterial | fisspecifymaterial | bpchar | 1 |  | √ | '0' |  |
| 21 | fmatgrpstdid | fmatgrpstdid | int8 | 64 |  | √ | 0 |  |
| 22 | fupdatebillid | fupdatebillid | int8 | 64 |  | √ | 0 |  |
| 23 | fupdatetime | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 24 | feffecttime | feffecttime | timestamp | 0 |  |  | null |  |
| 25 | fresbynoref_tag | fresbynoref_tag | text | 0 |  |  | null |  |
| 26 | fisallupdate | fisallupdate | bpchar | 1 |  | √ | '0' |  |
| 27 | fsourcepage | fsourcepage | varchar | 50 |  | √ | ' ' |  |
| 28 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_costupdatenew |  | fid |
| 2 | index_sco_costupdatenew_df |  | fsrccosttype,ftargetcosttype |
