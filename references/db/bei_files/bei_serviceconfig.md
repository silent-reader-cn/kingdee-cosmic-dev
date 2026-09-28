# 银企服务配置-bei_serviceconfig

## 银企服务配置-主表 t_bei_serviceconfig

- **表名称：** 银企服务配置-主表
- **表名：** t_bei_serviceconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopenorgid | 开户公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpubliccafile_tag | 公钥证书文件_详情 | text | 0 |  |  | null | 公钥证书文件_详情 |
| 4 | fcustomerca | CA私钥证书 | varchar | 250 |  | √ | ' ' | CA私钥证书 |
| 5 | fappsecret | Access Token加密认证密钥 | varchar | 500 |  | √ | ' ' | Access Token加密认证密钥 |
| 6 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 7 | fhufu | 部分CA证书 | varchar | 255 |  | √ | ' ' | 部分CA证书 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fappid | 开放平台认证系统编码 | varchar | 30 |  | √ | ' ' | 开放平台认证系统编码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcustomercode | fcustomercode | varchar | 250 |  | √ | ' ' |  |
| 13 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fusertype | 用户类型 | varchar | 50 |  |  | null | 用户类型,枚举: Mobile :手机 Email :邮箱 UserName :用户名 |
| 15 | fcustomerid2 | 客户ID号 | varchar | 80 |  | √ | ' ' | 客户ID号 |
| 16 | ftimeout | 响应超时时长 | int8 | 64 |  | √ | 0 | 响应超时时长 |
| 17 | fisrpc | fisrpc | bpchar | 1 |  | √ | '0' |  |
| 18 | fpubliccafile | 公钥证书文件 | varchar | 255 |  | √ | ' ' | 公钥证书文件 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 21 | fcomment | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fbatchdownaccountsnum | 批量下载余额分组每组账户数量 | int4 | 32 |  | √ | 1 | 批量下载余额分组每组账户数量 |
| 24 | fsecretlength | AES加密算法密钥长度 | varchar | 50 |  | √ | '256' | AES加密算法密钥长度,枚举: 256 :256位 128 :128位 |
| 25 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 26 | fbatchdownstrategy | 批量下载余额分组策略 | varchar | 50 |  | √ | 'groupbybankinterface' | 批量下载余额分组策略,枚举: groupbybankinterface :按银企接口+币别分组 |
| 27 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fconnectstatus | 是否连接 | bpchar | 1 |  | √ | '0' | 是否连接 |
| 29 | fprivatekey | CA私钥密码 | varchar | 200 |  |  | null | CA私钥密码 |
| 30 | fisopenapi | OpenApi调用 | bpchar | 1 |  | √ | '0' | OpenApi调用 |
| 31 | fcafile | CA证书文件 | varchar | 255 |  | √ | ' ' | CA证书文件 |
| 32 | fcustomerprivatekey | 客户私钥密码 | varchar | 80 |  | √ | ' ' | 客户私钥密码 |
| 33 | fisenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 34 | fserveraddress2 | 服务器地址2 | varchar | 80 |  | √ | ' ' | 服务器地址2 |
| 35 | fserveraddress | 服务器地址1 | varchar | 80 |  | √ | ' ' | 服务器地址1 |
| 36 | fisenable2 | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 37 | fpubliccaname | 系统公钥证书 | varchar | 50 |  |  | null | 系统公钥证书 |
| 38 | fuseraccount | 用户名 | varchar | 50 |  |  | null | 用户名 |
| 39 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 40 | fcafile_tag | CA证书文件_详情 | text | 0 |  |  | null | CA证书文件_详情 |
| 41 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 42 | fconnectstatus2 | 是否连接 | bpchar | 1 |  | √ | '0' | 是否连接 |
| 43 | fhufu_tag | 部分CA证书_详情 | text | 0 |  |  | null | 部分CA证书_详情 |
| 44 | faccountid | 数据中心ID | varchar | 80 |  | √ | ' ' | 数据中心ID |
| 45 | fcustomerid | 客户ID号 | varchar | 80 |  | √ | ' ' | 客户ID号 |
| 46 | fcompanyid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bei_serviceconfig_pkey |  | fid |
| 2 | idx_bei_serviceconfig |  | fnumber |

---

## 适用范围单据体-子表 t_bei_appscopeentity

- **表名称：** 适用范围单据体-子表
- **表名：** t_bei_appscopeentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | felastupdater | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | felastupdate | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 4 | febankcgno | 银行类别编码 | int8 | 64 |  | √ | 0 | [银行类别 bd_bankcgsetting](../basedata_files/bd_bankcgsetting.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bei_appscopeentity |  | fentryid |
| 2 | idx_febankcgno |  | febankcgno |

---

## 银企服务配置-多语言表 t_bei_serviceconfig_l

- **表名称：** 银企服务配置-多语言表
- **表名：** t_bei_serviceconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_serviceconfig_l |  | fid,flocaleid,fcomment |
| 2 | t_bei_serviceconfig_l_pkey |  | fpkid |
