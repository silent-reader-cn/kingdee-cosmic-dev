# 证书预警监控-aqap_bd_cert

## 证书预警监控-多语言表 t_aqap_bd_cert_l

- **表名称：** 证书预警监控-多语言表
- **表名：** t_aqap_bd_cert_l

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
| 1 | t_aqap_bd_cert_l_pkey |  | fpkid |
| 2 | idx_aqap_bd_cert_l_0 |  | fid,flocaleid |

---

## 证书预警监控-主表 t_aqap_bd_cert

- **表名称：** 证书预警监控-主表
- **表名：** t_aqap_bd_cert

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | ffile_name | 文件名称 | varchar | 255 |  | √ | ' ' | 文件名称 |
| 3 | fcert_source | 证书来源 | varchar | 50 |  | √ | ' ' | 证书来源,枚举: 0 :系统上传 1 :手动新增 |
| 4 | fbank_version_id | 银行版本编号 | varchar | 50 |  | √ | ' ' | 银行版本编号 |
| 5 | fbank_config_value | 证书字段值 | varchar | 255 |  | √ | ' ' | 证书字段值 |
| 6 | fexpire_time | 过期时间 | timestamp | 0 |  |  | null | 过期时间 |
| 7 | falert_day | 预警天数 | int8 | 64 |  |  | null | 预警天数 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcustom_id | 租户编号 | varchar | 50 |  | √ | ' ' | 租户编号 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 13 | fmobiles | 手机号 | varchar | 255 |  | √ | ' ' | 手机号 |
| 14 | fdownload_path | 上传后返回的path | varchar | 500 |  | √ | ' ' | 上传后返回的path |
| 15 | frow_num | 行号(用来控制状态颜色) | varchar | 50 |  | √ | ' ' | 行号(用来控制状态颜色) |
| 16 | fcert_password | 证书密码 | varchar | 50 |  | √ | ' ' | 证书密码 |
| 17 | fis_alert | 是否预警 | varchar | 50 |  | √ | ' ' | 是否预警,枚举: true :是 false :否 |
| 18 | forganization | 公司组织 | varchar | 50 |  | √ | ' ' | 公司组织 |
| 19 | fremark | 补充说明 | varchar | 500 |  | √ | ' ' | 补充说明 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fbank_config_name | 证书字段名称 | varchar | 50 |  | √ | ' ' | 证书字段名称 |
| 23 | fbank_config_id | 证书字段标识 | varchar | 100 |  | √ | ' ' | 证书字段标识 |
| 24 | fbank_login_id | 前置机编号 | varchar | 50 |  | √ | ' ' | 前置机编号 |
| 25 | falert_type | 预警方式 | varchar | 50 |  | √ | ' ' | 预警方式,枚举: 手机短信 :手机短信 |
| 26 | ftype | 证书类型（内部使用，不做展示） | varchar | 50 |  | √ | ' ' | 证书类型（内部使用，不做展示）,枚举: CA_CER :CA证书 PLATEFORM_CER :银行证书 BANKLOGIN_CER :前置机证书 ACNT_CER :账号证书 PROXY_CER :网络代理证书 OTHER_CER :第三方证书 |
| 27 | fcert_type | 证书类型 | varchar | 50 |  | √ | ' ' | 证书类型,枚举: 1 :银企服务连接证书 2 :开放银行证书 9 :国内银行证书 3 :支付宝证书 4 :微信证书 5 :外资银行证书 6 :网络代理证书 7 :银行前置机证书 8 :其他证书 |
| 28 | fcert_status | 证书状态 | varchar | 50 |  | √ | ' ' | 证书状态,枚举: 1 :已过期 2 :未过期 |
| 29 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | facnt_no | 银行账号 | varchar | 50 |  | √ | ' ' | 银行账号 |
| 31 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 32 | fbank_config_value_tag | 证书字段值_详情 | text | 0 |  |  | null | 证书字段值_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_bd_cert_pkey |  | fid |
