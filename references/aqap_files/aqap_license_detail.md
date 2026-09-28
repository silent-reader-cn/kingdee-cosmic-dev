# 许可详情表-aqap_license_detail

## 许可详情表-主表 t_aqap_license_detail

- **表名称：** 许可详情表-主表
- **表名：** t_aqap_license_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fbank_version | 银行版本 | varchar | 50 |  | √ | null | 银行版本 |
| 3 | fmodifierid | 编辑人 | int8 | 64 |  |  | null | 编辑人 |
| 4 | fmodule_code | 模块简码 | varchar | 50 |  | √ | null | 模块简码 |
| 5 | fcustom_id | 租户号 | varchar | 50 |  | √ | ' ' | 租户号 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 创建人 |
| 7 | fmodule_name | 模块名称 | varchar | 50 |  | √ | ' ' | 模块名称 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fbank_login_id | 前置机编号 | varchar | 50 |  | √ | null | 前置机编号 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aqap_license_info_0 |  | fcustom_id |
| 2 | t_aqap_license_detail_pkey |  | fid |
| 3 | idx_aqap_license_detail_uk |  | fmodule_code,fbank_version,fcustom_id |
