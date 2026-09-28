# 第三方应用接入配置-invsm_app_access_config

## 第三方应用接入配置-主表 t_invsm_bus_sys_config

- **表名称：** 第三方应用接入配置-主表
- **表名：** t_invsm_bus_sys_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 业务系统名称 | varchar | 50 |  | √ | ' ' | 业务系统名称 |
| 4 | faesvector | AES向量 | varchar | 16 |  | √ | ' ' | AES向量 |
| 5 | fcallbackurlthr | 回调接口地址3 | varchar | 200 |  | √ | ' ' | 回调接口地址3 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | faespwds | AES密钥 | varchar | 16 |  | √ | ' ' | AES密钥 |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fencryptiontype | 数据加密策略 | varchar | 30 |  | √ | ' ' | 数据加密策略,枚举: 0 :AES+BASE64 1 :BASE64 |
| 11 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fcallbackurltwo | 回调接口地址2 | varchar | 200 |  | √ | ' ' | 回调接口地址2 |
| 13 | fcallbackurl | 回调接口地址1 | varchar | 200 |  | √ | ' ' | 回调接口地址1 |
| 14 | fisvalid | 启用禁用标识 | varchar | 30 |  | √ | ' ' | 启用禁用标识,枚举: 0 :禁用 1 :启用 |
| 15 | fcode | 业务系统编码 | varchar | 20 |  | √ | ' ' | 业务系统编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invsm_bus_sys_config |  | fcode |
| 2 | pk_invsm_bus_sys_config |  | fid |
