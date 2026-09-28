# 宁波银行财资大管家服务配置-bei_nbconfig

## 宁波银行财资大管家服务配置-主表 t_bei_nbconfig

- **表名称：** 宁波银行财资大管家服务配置-主表
- **表名：** t_bei_nbconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 256 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fappsecret | 应用密钥 | varchar | 256 |  | √ | ' ' | 应用密钥 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fxkprivatekey | 星空旗舰版私钥 | varchar | 512 |  | √ | ' ' | 星空旗舰版私钥 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fappid | 账号 | varchar | 256 |  | √ | ' ' | 账号 |
| 9 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | flastsyntime | 最后同步时间 | timestamp | 0 |  |  | null | 最后同步时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fnbpublickey | 对接平台公钥 | varchar | 512 |  | √ | ' ' | 对接平台公钥 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 256 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bei_nbconfig_fnumber |  | fnumber |
| 2 | pk_t_bei_nbconfig |  | fid |

---

## 单位代码明细-子表 t_bei_nbconfig_entry

- **表名称：** 单位代码明细-子表
- **表名：** t_bei_nbconfig_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcorecode | 对应单位代码 | varchar | 256 |  | √ | ' ' | 对应单位代码 |
| 3 | fuorgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bei_nbconfig_entry |  | fentryid |
| 2 | idx_t_bei_nbe_fnumber |  | fuorgid |

---

## 宁波银行财资大管家服务配置-多语言表 t_bei_nbconfig_l

- **表名称：** 宁波银行财资大管家服务配置-多语言表
- **表名：** t_bei_nbconfig_l

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
| 1 | idx_t_bei_nbcon_l_fid |  | fid |
| 2 | pk_bei_nbconfig_l |  | fpkid |
