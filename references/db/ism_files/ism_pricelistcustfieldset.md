# 结算价目表自定义维度配置-ism_pricelistcustfieldset

## 结算价目表自定义维度配置-多语言表 t_ism_custfieldset_l

- **表名称：** 结算价目表自定义维度配置-多语言表
- **表名：** t_ism_custfieldset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ism_custfieldset_l |  | fid |
| 2 | pk_ism_custfieldset_l |  | fpkid |

---

## 结算价目表自定义维度配置-主表 t_ism_custfieldset

- **表名称：** 结算价目表自定义维度配置-主表
- **表名：** t_ism_custfieldset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizfieldname | 结算价目表字段名称 | varchar | 100 |  | √ | ' ' | 结算价目表字段名称 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fsettype | 类型 | varchar | 20 |  | √ | ' ' | 类型,枚举: 1 :价目表匹配 |
| 6 | fsettlefieldname | 结算清单字段名称 | varchar | 100 |  | √ | ' ' | 结算清单字段名称 |
| 7 | fbizfieldkey | 结算价目表字段标识 | varchar | 100 |  | √ | ' ' | 结算价目表字段标识 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fbill | 业务单据对象 | varchar | 50 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 10 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 11 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fsettlefieldkey | 结算清单字段标识 | varchar | 100 |  | √ | ' ' | 结算清单字段标识 |
| 13 | fispreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置,枚举: 1 :是 0 :否 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_custfieldset |  | fid |
| 2 | idx_ism_custfieldset |  | fsettlefieldkey |
