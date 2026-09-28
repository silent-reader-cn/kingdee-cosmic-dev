# 法人企业-ccas_esenterprice

## 法人企业-主表 t_ccas_esenterprice

- **表名称：** 法人企业-主表
- **表名：** t_ccas_esenterprice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foldname | 名称(上次认证) | varchar | 255 |  | √ | ' ' | 名称(上次认证) |
| 3 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fcertifystatus | 企业认证状态 | varchar | 30 |  | √ | ' ' | 企业认证状态,枚举: A :待认证 B :已认证 C :认证中 D :认证失败 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fenterprice | 企业名称 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fesstatus | 印章状态 | varchar | 30 |  | √ | ' ' | 印章状态,枚举: A :待设置 B :已设置 C :设置中 D :设置失败 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fesserviceprovider | 集成服务 | int8 | 64 |  | √ | 0 | 集成服务配置 ccas_cisconfig |
| 12 | funiformsocialcreditcode | 统一社会信用代码(上次认证) | varchar | 255 |  | √ | ' ' | 统一社会信用代码(上次认证) |
| 13 | fserviceadmin | 服务管理员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 16 | fphone | fphone | varchar | 255 |  | √ | ' ' |  |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | factionstatus | 企业认证requestId | varchar | 255 |  | √ | ' ' | 企业认证requestId,枚举: 0 :提交基本信息 1 :基本信息审核通过 2 :基础信息审核失败 3 :授权书审核失败 7 :待授权（已认证） 8 :授权完成 |
| 19 | fqysaccesssecret | 契约锁授权秘钥 | varchar | 255 |  | √ | ' ' | 契约锁授权秘钥 |
| 20 | frepresentative | frepresentative | varchar | 255 |  | √ | ' ' |  |
| 21 | fqysappid | 契约锁AppID | varchar | 255 |  | √ | ' ' | 契约锁AppID |
| 22 | fprivilegemodules | 契约锁已授权模块 | varchar | 255 |  | √ | ' ' | 契约锁已授权模块 |
| 23 | fprivilegestatus | 企业授权状态 | varchar | 30 |  | √ | ' ' | 企业授权状态,枚举: A :待授权 B :已授权 C :授权中 D :授权失败 |
| 24 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fqysaccesstoken | 契约锁授权令牌 | varchar | 255 |  | √ | ' ' | 契约锁授权令牌 |
| 26 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 27 | fcompanyid | 契约锁企业ID | varchar | 255 |  | √ | ' ' | 契约锁企业ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ccas_esenterprice |  | fid |
| 2 | idx_t_ccas_esenterprice_fname |  | fname |

---

## 法人企业-多语言表 t_ccas_esenterprice_l

- **表名称：** 法人企业-多语言表
- **表名：** t_ccas_esenterprice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 40 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ccas_esenterprice_l |  | fpkid |
| 2 | idx_ccas_esenterprice_l_fid |  | fid,flocaleid |
