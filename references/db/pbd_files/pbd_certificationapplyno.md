# 供应商认证申请编号-pbd_certificationapplyno

## 供应商认证申请编号-主表 t_pur_certifiapply

- **表名称：** 供应商认证申请编号-主表
- **表名：** t_pur_certifiapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fbillstatus | 数据状态 | varchar | 80 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 7 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 8 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 10 | fopergroupid | fopergroupid | int8 | 64 |  | √ | 0 |  |
| 11 | fprojectname | 项目名称 | varchar | 512 |  | √ | ' ' | 项目名称 |
| 12 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 13 | fhaveissue | fhaveissue | bpchar | 1 |  | √ | ' ' |  |
| 14 | fbiztypeid | fbiztypeid | int8 | 64 |  | √ | 0 |  |
| 15 | fnextauditor | fnextauditor | varchar | 100 |  | √ | ' ' |  |
| 16 | fbillno | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 17 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 18 | fcertificationbackground | fcertificationbackground | text | 0 |  |  | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_certifiapply |  | fid |
| 2 | idx_pur_certifiapply |  | fbillno,forgid |
