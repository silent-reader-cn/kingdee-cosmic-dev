# 短信签名-bos_sms_signature

## 短信签名-主表 t_bas_sms_signature

- **表名称：** 短信签名-主表
- **表名：** t_bas_sms_signature

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsmsapp | 短信应用 | varchar | 50 |  | √ | ' ' | 短信应用 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 签名 | varchar | 50 |  | √ | ' ' | 签名 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | flocaleid | 语种 | int8 | 64 |  | √ | 0 | [语言种类 inte_language](../base_files/inte_language.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fsignid | 签名id | varchar | 50 |  | √ | ' ' | 签名id |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: 0 :待审核 1 :已审核 2 :审核不通过 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fapplyreason | 申请原因 | varchar | 255 |  | √ | ' ' | 申请原因 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 15 | fbusinesslicense | 上传企业营业执照、组织机构代码证书、社会信用代码证书之一 | varchar | 512 |  | √ | ' ' | 上传企业营业执照、组织机构代码证书、社会信用代码证书之一 |
| 16 | fprodinstcode | 产品实例码 | varchar | 50 |  | √ | ' ' | 产品实例码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_t_status |  | fstatus |
| 2 | pk_bas_sms_signature |  | fid |
