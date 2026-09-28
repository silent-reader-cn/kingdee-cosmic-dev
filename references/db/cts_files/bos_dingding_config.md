# 钉钉配置-bos_dingding_config

## 钉钉配置-主表 t_bas_dingding

- **表名称：** 钉钉配置-主表
- **表名：** t_bas_dingding

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fagentid | 应用ID | varchar | 50 |  | √ | ' ' | 应用ID |
| 3 | fhost | 当前域名地址 | varchar | 128 |  | √ | ' ' | 当前域名地址 |
| 4 | fagentname | 应用名称 | varchar | 50 |  | √ | ' ' | 应用名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fwebformid | Web端应用主页 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fappsecret | 应用秘钥 | varchar | 100 |  | √ | ' ' | 应用秘钥 |
| 8 | fmobileformid | 移动端应用主页 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fappkey | 应用标识 | varchar | 100 |  | √ | ' ' | 应用标识 |
| 10 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 11 | fweburl | Web端URL | varchar | 600 |  | √ | ' ' | Web端URL |
| 12 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 13 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fconnstatus | 连接测试状态 | bpchar | 1 |  | √ | '0' | 连接测试状态,枚举: 0 :未测试 1 :正常 2 :异常 |
| 15 | ftrustedip | ftrustedip | varchar | 100 |  | √ | ' ' |  |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fiptime | fiptime | timestamp | 0 |  |  | null |  |
| 21 | fcorpid | 企业ID | varchar | 50 |  | √ | ' ' | 企业ID |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态 |
| 23 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 24 | fmobileurl | 移动端URL | varchar | 600 |  | √ | ' ' | 移动端URL |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_dingding_pkey |  | fid |
| 2 | idx_t_bas_dingding_appkey |  | fappkey |

---

## 钉钉配置-多语言表 t_bas_dingding_l

- **表名称：** 钉钉配置-多语言表
- **表名：** t_bas_dingding_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bas_dingding_l_fid |  | fid,flocaleid |
| 2 | t_bas_dingding_l_pkey |  | fpkid |
