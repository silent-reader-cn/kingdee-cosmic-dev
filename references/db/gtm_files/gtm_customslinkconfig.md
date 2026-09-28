# 集成参数配置-gtm_customslinkconfig

## 集成参数配置-多语言表 t_gtm_customslinkcfg_l

- **表名称：** 集成参数配置-多语言表
- **表名：** t_gtm_customslinkcfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_customslinkcfg_l |  | fpkid |
| 2 | idx_gtm_customslinkcfg_l_id |  | fid,flocaleid |

---

## 接口配置-子表 t_gtm_customslinkcfgpath

- **表名称：** 接口配置-子表
- **表名：** t_gtm_customslinkcfgpath

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fservicecode | 服务代码 | varchar | 255 |  | √ | ' ' | 服务代码 |
| 3 | fservicepath | 接口地址 | varchar | 255 |  | √ | ' ' | 接口地址 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fservicetype | 接口类型 | varchar | 50 |  | √ | ' ' | 接口类型,枚举: 1 :赋号 2 :数据直连 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_customslinkcfgpath |  | fentryid |
| 2 | idx_gtm_customslinkcfgpath_id |  | fid |

---

## 海关配置-多语言表 t_gtm_customslinkcfgety_l

- **表名称：** 海关配置-多语言表
- **表名：** t_gtm_customslinkcfgety_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fcustomsagentname | 单位名称 | varchar | 512 |  | √ | ' ' | 单位名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtm_customslinkcfgety_l_d |  | fentryid,flocaleid |
| 2 | pk_gtm_customslinkcfgety_l |  | fpkid |

---

## 海关配置-子表 t_gtm_customslinkcfgety

- **表名称：** 海关配置-子表
- **表名：** t_gtm_customslinkcfgety

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustomsagentcode | 单位代码 | varchar | 255 |  | √ | ' ' | 单位代码 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fcustomsaccount | 海关账号 | varchar | 255 |  | √ | ' ' | 海关账号 |
| 5 | fcertificate | IC卡证书号 | varchar | 255 |  | √ | ' ' | IC卡证书号 |
| 6 | ficcode | IC卡号 | varchar | 255 |  | √ | ' ' | IC卡号 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fcustomsagentname | 单位名称 | varchar | 512 |  | √ | ' ' | 单位名称 |
| 10 | fdeclno | 报关员号 | varchar | 255 |  | √ | ' ' | 报关员号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtm_customslinkcfgety_id |  | fid |
| 2 | pk_gtm_customslinkcfgety |  | fentryid |

---

## 集成参数配置-主表 t_gtm_customslinkcfg

- **表名称：** 集成参数配置-主表
- **表名：** t_gtm_customslinkcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsender | 发送方代码 | varchar | 255 |  | √ | ' ' | 发送方代码 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fservicepassword | 加密密码 | varchar | 50 |  | √ | ' ' | 加密密码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fsericepublickey | 公钥 | varchar | 512 |  | √ | ' ' | 公钥 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fserviceaddress | 服务地址 | varchar | 512 |  | √ | ' ' | 服务地址 |
| 11 | fsericeprivatekey | 私钥 | varchar | 512 |  | √ | ' ' | 私钥 |
| 12 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 18 | fauthorization | 授权码 | varchar | 255 |  | √ | ' ' | 授权码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_customslinkcfg |  | fid |
