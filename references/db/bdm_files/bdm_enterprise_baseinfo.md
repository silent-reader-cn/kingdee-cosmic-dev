# 企业基础信息-bdm_enterprise_baseinfo

## 企业基础信息-主表 t_bdm_enterprise_baseinfo

- **表名称：** 企业基础信息-主表
- **表名：** t_bdm_enterprise_baseinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdevissuer | fdevissuer | varchar | 50 |  | √ | ' ' |  |
| 3 | fdzptbm | 托管接口方法 | varchar | 100 |  | √ | ' ' | 托管接口方法 |
| 4 | ftax_username | 电子发票服务平台账号 | varchar | 50 |  | √ | ' ' | 电子发票服务平台账号 |
| 5 | fdevpwd | UKey密码 | varchar | 100 |  | √ | ' ' | UKey密码 |
| 6 | fdevissuerid | fdevissuerid | int8 | 64 |  | √ | 0 |  |
| 7 | fcertissuetime | 证书发行时间 | timestamp | 0 |  |  | null | 证书发行时间 |
| 8 | fcurrenttime | 当前时钟 | timestamp | 0 |  |  | null | 当前时钟 |
| 9 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fzcm | 托管平台注册码 | varchar | 100 |  | √ | ' ' | 托管平台注册码 |
| 11 | fdevno | UKey编码 | varchar | 50 |  | √ | ' ' | UKey编码 |
| 12 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | fcertstatus | 证书状态 | varchar | 30 |  | √ | ' ' | 证书状态,枚举: 1 :待发行 2 :已发行 3 :已过期 4 :已注销 |
| 14 | fstatus | 状态 | varchar | 60 |  | √ | ' ' | 状态,枚举: 1 :启用 2 :停用 |
| 15 | fpublicperson | 法人名称 | varchar | 100 |  | √ | ' ' | 法人名称 |
| 16 | fauthcode | 托管纳税人授权码 | varchar | 100 |  | √ | ' ' | 托管纳税人授权码 |
| 17 | fhostmanagetype | 托管类型（托管方） | varchar | 100 |  | √ | ' ' | 托管类型（托管方）,枚举: 1 :上海航信 2 :深圳航信 3 :河北航信 4 :贵州航信 6 :51航信 7 :阿里百旺 |
| 18 | fcastatus | CA证书状态 | varchar | 10 |  | √ | ' ' | CA证书状态,枚举: 0 :未申请 1 :已申请 |
| 19 | finvoiceaddr | 地址电话 | varchar | 100 |  | √ | ' ' | 地址电话 |
| 20 | fcertissuer | fcertissuer | varchar | 50 |  | √ | ' ' |  |
| 21 | fvirtualdevid | 唯一标识 | varchar | 40 |  | √ | ' ' | 唯一标识 |
| 22 | ftaxpassword_enp | ftaxpassword_enp | varchar | 300 |  | √ | ' ' |  |
| 23 | fqzaddress | 托管接口地址 | varchar | 100 |  | √ | ' ' | 托管接口地址 |
| 24 | fcertexpiretime | 证书有效期 | timestamp | 0 |  |  | null | 证书有效期 |
| 25 | fcastarttime | ca有效开始时间 | timestamp | 0 |  |  | null | ca有效开始时间 |
| 26 | fisallele | 是否有传到基础部门标记为全电 | varchar | 10 |  | √ | '0' | 是否有传到基础部门标记为全电,枚举: 0 :未标记为全电 1 :已标记为全电 |
| 27 | fcertissuerid | fcertissuerid | int8 | 64 |  | √ | 0 |  |
| 28 | fname | 企业名称 | varchar | 200 |  | √ | ' ' | 企业名称 |
| 29 | ftax_username_enp | ftax_username_enp | varchar | 500 |  | √ | ' ' |  |
| 30 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 31 | fqzservicename | 托管接口方法 | varchar | 100 |  | √ | ' ' | 托管接口方法 |
| 32 | finvoicetypes | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 026 :增值税电子普通发票 028 :增值税电子专用发票 |
| 33 | fdevissuetime | 虚拟设备发行时间 | timestamp | 0 |  |  | null | 虚拟设备发行时间 |
| 34 | fcaendtime | ca有效结束日期 | timestamp | 0 |  |  | null | ca有效结束日期 |
| 35 | fregistertime | 登记时间 | timestamp | 0 |  |  | null | 登记时间 |
| 36 | fbusinesslicenseurl | 营业执照存储地址 | varchar | 300 |  | √ | ' ' | 营业执照存储地址 |
| 37 | fenablepdfinvoice | 是否盘开电票 | varchar | 10 |  | √ | ' ' | 是否盘开电票,枚举: 0 :否 1 :是 |
| 38 | fopenuserbank | 开户行及电话 | varchar | 100 |  | √ | ' ' | 开户行及电话 |
| 39 | fauthtype | 认证类型 | varchar | 2 |  | √ | ' ' | 认证类型,枚举: 2 :软证书认证 4 :新电子发票服务平台 |
| 40 | fisvoucher | 电子凭证会计数据试点企业 | varchar | 2 |  | √ | ' ' | 电子凭证会计数据试点企业,枚举: 1 :是 2 :否 |
| 41 | ftaxpassword | 电子发票服务平台密码 | varchar | 50 |  | √ | ' ' | 电子发票服务平台密码 |
| 42 | fnumber | 企业税号 | varchar | 50 |  | √ | ' ' | 企业税号 |
| 43 | fprovince | fprovince | varchar | 30 |  | √ | ' ' |  |
| 44 | fauthorizestatus | 认证状态 | varchar | 10 |  | √ | ' ' | 认证状态,枚举: 0 :未认证 1 :认证成功 2 :认证失败 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_enterprise_baseinfo |  | fdevno |
| 2 | pk_bdm_enterprise_baseinfo |  | fid |
| 3 | idx_bdm_ep_baseinfo_taxno |  | fnumber,fvirtualdevid |
