# 归档服务器配置-aef_serviceconfig

## 归档服务器配置-多语言表 t_aef_serviceconfig_l

- **表名称：** 归档服务器配置-多语言表
- **表名：** t_aef_serviceconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aef_serviceconfig_l |  | fid,flocaleid |
| 2 | t_aef_serviceconfig_l_pkey |  | fpkid |

---

## 归档服务器配置-主表 t_aef_serviceconfig

- **表名称：** 归档服务器配置-主表
- **表名：** t_aef_serviceconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fappsecret | 应用秘钥 | varchar | 50 |  | √ | ' ' | 应用秘钥 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fuser | 用户 | varchar | 50 |  | √ | ' ' | 用户 |
| 6 | fserviceip | 服务器地址 | varchar | 255 |  | √ | ' ' | 服务器地址 |
| 7 | ftenantid | 租户ID | varchar | 50 |  | √ | ' ' | 租户ID |
| 8 | fpassword | 秘钥 | varchar | 50 |  | √ | ' ' | 秘钥 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fpassword_enp | fpassword_enp | varchar | 300 |  | √ | ' ' |  |
| 11 | fappid | 应用ID | varchar | 50 |  | √ | ' ' | 应用ID |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fusername | 账户 | varchar | 30 |  | √ | ' ' | 账户 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fserviceport | 端口 | varchar | 5 |  | √ | ' ' | 端口 |
| 17 | frequestway | 请求方式 | bpchar | 1 |  | √ | '0' | 请求方式,枚举: 1 :http 2 :https |
| 18 | fuploadway | 上传方式 | varchar | 30 |  | √ | ' ' | 上传方式,枚举: 1 :道可维斯 2 :FTP 3 :发票云 4 :第三方档案系统 5 :星瀚归档云 |
| 19 | fappsecret_enp | fappsecret_enp | varchar | 300 |  | √ | ' ' |  |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 22 | faccountid | 数据中心ID | varchar | 50 |  | √ | ' ' | 数据中心ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aef_serviceconfig_pkey |  | fid |
| 2 | idx_aef_serviceconfig |  | fnumber |
