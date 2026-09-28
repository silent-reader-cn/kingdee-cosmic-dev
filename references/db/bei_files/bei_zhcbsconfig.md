# 招行CBS连接配置-bei_zhcbsconfig

## 招行CBS连接配置-多语言表 t_bei_zhcbsconfig_l

- **表名称：** 招行CBS连接配置-多语言表
- **表名：** t_bei_zhcbsconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 256 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 256 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 256 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bei_zhcbsconfig_l_fid |  | fid |
| 2 | pk_t_bei_zhcbsconfig_l |  | fpkid |

---

## 招行CBS连接配置-主表 t_bei_zhcbsconfig

- **表名称：** 招行CBS连接配置-主表
- **表名：** t_bei_zhcbsconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 256 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fappsecret | 密码密钥 | varchar | 256 |  | √ | ' ' | 密码密钥 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fconnecttype | 连接平台 | bpchar | 1 |  | √ | ' ' | 连接平台,枚举: 1 :招行CBS8 |
| 7 | fnote | 备注 | varchar | 256 |  | √ | ' ' | 备注 |
| 8 | fxkprivatekey | 星空旗舰版私钥 | varchar | 512 |  | √ | ' ' | 星空旗舰版私钥 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fappid | 账号 | varchar | 256 |  | √ | ' ' | 账号 |
| 11 | fcbspathurl | CBS8文件公钥url | varchar | 256 |  | √ | ' ' | CBS8文件公钥url |
| 12 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fxkpublickey | 星空旗舰版公钥 | varchar | 256 |  | √ | ' ' | 星空旗舰版公钥 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcbspublickey | 招行CBS8公钥 | varchar | 256 |  | √ | ' ' | 招行CBS8公钥 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 256 |  | √ | ' ' | 编码 |
| 19 | fcbsfilename | CBS8公钥文件名 | varchar | 256 |  | √ | ' ' | CBS8公钥文件名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bei_zhcbsconfig_fnumber |  | fnumber |
| 2 | pk_t_bei_zhcbsconfig |  | fid |
