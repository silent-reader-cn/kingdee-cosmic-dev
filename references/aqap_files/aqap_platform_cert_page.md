# 银行证书管理-aqap_platform_cert_page

## 银行证书管理-多语言表 t_aqap_platform_cert_page_l

- **表名称：** 银行证书管理-多语言表
- **表名：** t_aqap_platform_cert_page_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_platform_cert_page_l_pkey |  | fpkid |
| 2 | idx_aqap_pcp_l_0 |  | fid,flocaleid |

---

## 银行证书管理-主表 t_aqap_platform_cert_page

- **表名称：** 银行证书管理-主表
- **表名：** t_aqap_platform_cert_page

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fpublic_key | 银行公钥文件 | varchar | 50 |  | √ | ' ' | 银行公钥文件 |
| 5 | fprivate_key_secret | fprivate_key_secret | varchar | 50 |  | √ | ' ' |  |
| 6 | fprivate_key | 私钥文件 | varchar | 50 |  | √ | ' ' | 私钥文件 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fbank_version | 银行版本 | int8 | 64 |  |  | null | 银行启用管理 aqap_bank |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 12 | fk_ebc_textfield | fk_ebc_textfield | varchar | 50 |  | √ | ' ' |  |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_platform_cert_page_pkey |  | fid |
