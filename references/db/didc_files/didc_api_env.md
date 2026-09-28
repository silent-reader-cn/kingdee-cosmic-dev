# API环境配置-didc_api_env

## 请求头-子表 t_didc_api_env_head

- **表名称：** 请求头-子表
- **表名：** t_didc_api_env_head

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fheadtype | 输入类型 | varchar | 50 |  | √ | ' ' | 输入类型,枚举: value :参数值 var :变量 plugin :插件 |
| 3 | fheadencryptmethod | 加密方式 | varchar | 50 |  | √ | ' ' | 加密方式,枚举: none :无 md5 :MD5 |
| 4 | fheadparamvalue | 参数值 | varchar | 255 |  | √ | ' ' | 参数值 |
| 5 | fheaddescription | 参数描述 | varchar | 255 |  | √ | ' ' | 参数描述 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fheadparamname | 参数名称 | varchar | 255 |  | √ | ' ' | 参数名称 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_didc_api_env_head |  | fentryid |
| 2 | idx_didc_api_env_head_fk |  | fid |

---

## API环境配置-多语言表 t_didc_api_env_l

- **表名称：** API环境配置-多语言表
- **表名：** t_didc_api_env_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | API环境名称 | varchar | 255 |  | √ | ' ' | API环境名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_api_env_l_0 |  | fid,flocaleid |
| 2 | pk_didc_api_env_l |  | fpkid |

---

## 请求体-子表 t_didc_api_env_body

- **表名称：** 请求体-子表
- **表名：** t_didc_api_env_body

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbodyparamvalue | 参数值 | varchar | 255 |  | √ | ' ' | 参数值 |
| 3 | fbodydescription | 参数描述 | varchar | 255 |  | √ | ' ' | 参数描述 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbodyparamname | 参数名称 | varchar | 255 |  | √ | ' ' | 参数名称 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fbodyencryptmethod | 加密方式 | varchar | 50 |  | √ | ' ' | 加密方式,枚举: none :无 md5 :MD5 |
| 8 | fcombofield | 输入类型 | varchar | 50 |  | √ | ' ' | 输入类型,枚举: value :参数值 var :变量 plugin :插件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_didc_api_env_body |  | fentryid |
| 2 | idx_didc_api_env_body_fk |  | fid |

---

## API环境配置-主表 t_didc_api_env

- **表名称：** API环境配置-主表
- **表名：** t_didc_api_env

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | API环境名称 | varchar | 255 |  | √ | ' ' | API环境名称 |
| 4 | fuser | 登录用户 | varchar | 50 |  | √ | ' ' | 登录用户 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fconnecttype | API环境类型 | varchar | 50 |  | √ | ' ' | API环境类型,枚举: K3CLOUD :星空企业版 K3CLOUD_AUTH :星空企业版(权限) OTHER :第三方系统 Flagship :星空旗舰版 |
| 7 | fpwd | 登录密码 | varchar | 100 |  | √ | ' ' | 登录密码 |
| 8 | fappid | 应用ID | varchar | 255 |  | √ | ' ' | 应用ID |
| 9 | fpwd_enp | fpwd_enp | text | 0 |  |  | null |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fdatacenter | 数据中心 | varchar | 50 |  | √ | ' ' | 数据中心 |
| 12 | fendpoint | 访问地址 | varchar | 512 |  | √ | ' ' | 访问地址 |
| 13 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcheckurl | 连接检查服务 | varchar | 255 |  | √ | ' ' | 连接检查服务 |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fenvid | 基础环境id | int8 | 64 |  |  | 0 | 基础环境id |
| 18 | fappsec | 应用秘钥 | varchar | 255 |  | √ | ' ' | 应用秘钥 |
| 19 | fissystem | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 20 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | API环境编码 | varchar | 30 |  | √ | ' ' | API环境编码 |
| 22 | ftimeout | 连接超时控制（秒) | int8 | 64 |  | √ | 0 | 连接超时控制（秒) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_didc_api_env |  | fid |
| 2 | idx_didc_api_env_m0 |  | fmasterid |
