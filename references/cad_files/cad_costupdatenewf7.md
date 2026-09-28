# 更新申请单F7-cad_costupdatenewf7

## 更新申请单F7-主表 t_cad_costupdatenew

- **表名称：** 更新申请单F7-主表
- **表名：** t_cad_costupdatenew

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 3 | fresmatbyuseauxpt_tag | fresmatbyuseauxpt_tag | text | 0 |  |  | null |  |
| 4 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 5 | fupdatebillno | 更新编码 | varchar | 80 |  | √ | ' ' | 更新编码 |
| 6 | ftargetcosttype | 目标成本类型 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 7 | fresbynoref | fresbynoref | varchar | 2000 |  | √ | ' ' |  |
| 8 | fupdatestatus | fupdatestatus | varchar | 80 |  | √ | ' ' |  |
| 9 | fresmatbyuseauxpt | fresmatbyuseauxpt | varchar | 2000 |  | √ | ' ' |  |
| 10 | fbillno | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 11 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 12 | fperiodid | fperiodid | int8 | 64 |  | √ | 0 |  |
| 13 | fbillstatus | fbillstatus | varchar | 30 |  | √ | ' ' |  |
| 14 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 15 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 16 | fsrccosttype | 源成本类型 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 17 | fiscalccurlevel | fiscalccurlevel | bpchar | 1 |  | √ | '0' |  |
| 18 | fisspecifymaterial | fisspecifymaterial | bpchar | 1 |  | √ | '0' |  |
| 19 | fmatgrpstdid | fmatgrpstdid | int8 | 64 |  | √ | 0 |  |
| 20 | fupdatebillid | fupdatebillid | int8 | 64 |  | √ | 0 |  |
| 21 | fupdatetime | 长日期 | timestamp | 0 |  |  | null | 长日期 |
| 22 | feffecttime | feffecttime | timestamp | 0 |  |  | null |  |
| 23 | fresbynoref_tag | fresbynoref_tag | text | 0 |  |  | null |  |
| 24 | fisallupdate | fisallupdate | bpchar | 1 |  | √ | '0' |  |
| 25 | fsourcepage | fsourcepage | varchar | 50 |  | √ | ' ' |  |
| 26 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_costupdatenew_pkey |  | fid |
| 2 | index_cad_costupdatenew_df |  | fsrccosttype,ftargetcosttype |
