# 上传凭证-tsate_sbpz_upload

## 上传凭证-主表 t_tsate_sbpz_admin

- **表名称：** 上传凭证-主表
- **表名：** t_tsate_sbpz_admin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 凭证名称 | varchar | 50 |  | √ | ' ' | 凭证名称 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbasedatasource | fbasedatasource | int8 | 64 |  | √ | 0 |  |
| 8 | fdeclaretype | fdeclaretype | varchar | 50 |  | √ | ' ' |  |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fskssqq | fskssqq | timestamp | 0 |  |  | null |  |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fskssqz | fskssqz | timestamp | 0 |  |  | null |  |
| 14 | fcreater | fcreater | int8 | 64 |  | √ | 0 |  |
| 15 | fisarchive | fisarchive | varchar | 50 |  | √ | '0' |  |
| 16 | fdatasource | fdatasource | varchar | 50 |  | √ | ' ' |  |
| 17 | fsbqj | 申报期间 | timestamp | 0 |  |  | null | 申报期间 |
| 18 | ftaxtype | ftaxtype | int8 | 64 |  | √ | 0 |  |
| 19 | fbillno | 凭证编号 | varchar | 30 |  | √ | ' ' | 凭证编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_sbpz_admin_fbillno |  | fbillno |
| 2 | pk_tsate_sbpz_admin |  | fid |
