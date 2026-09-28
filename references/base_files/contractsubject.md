# 合同主体-contractsubject

## 合同主体-主表 t_ec_contractsubject

- **表名称：** 合同主体-主表
- **表名：** t_ec_contractsubject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fresultcode | 认证结果 | varchar | 10 |  | √ | ' ' | 认证结果,枚举: 0 :认证失败 1 :认证成功 2 :待认证 3 :已提交待审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fphone | 手机号 | varchar | 36 |  | √ | ' ' | 手机号 |
| 5 | fresultdesc | 认证描述 | varchar | 255 |  | √ | ' ' | 认证描述 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ffiorgid | 合同主体 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 9 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 10 | fisauthed | 注册状态 | bpchar | 1 |  | √ | ' ' | 注册状态,枚举: 0 :注册失败 1 :注册成功 2 :待注册 |
| 11 | fauthurl | 认证地址 | varchar | 512 |  | √ | ' ' | 认证地址 |
| 12 | fappid | AppID | varchar | 100 |  | √ | ' ' | AppID |
| 13 | fsignatureid | 电子签章ID | varchar | 255 |  | √ | ' ' | 电子签章ID |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fstatus | 数据状态 | varchar | 15 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fsignprovider | 签章服务商 | varchar | 10 |  | √ | ' ' | 签章服务商,枚举: 1 :法大大 2 :上上签 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fuuid | uuid | varchar | 100 |  | √ | ' ' | uuid |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 36 |  | √ | ' ' | 编码 |
| 22 | fcompanyseal | 电子印章 | varchar | 255 |  | √ | ' ' | 电子印章 |
| 23 | fkdappid | 商户ID | varchar | 100 |  | √ | ' ' | 商户ID |
| 24 | fcompanyid | 企业ID | varchar | 100 |  | √ | ' ' | 企业ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ec_contractsubject_orgid |  | ffiorgid |
| 2 | pk_t_ec_contractsubject |  | fid |

---

## 合同主体-多语言表 t_ec_contractsubject_l

- **表名称：** 合同主体-多语言表
- **表名：** t_ec_contractsubject_l

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
| 1 | idx_t_ec_contractsubject_l_fid |  | fid,flocaleid |
| 2 | pk_t_ec_contractsubject_l |  | fpkid |
