# 票据类型-cdm_billtype

## 关联结算方式-多选基础资料表 t_cdm_billtype_setttype

- **表名称：** 关联结算方式-多选基础资料表
- **表名：** t_cdm_billtype_setttype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cdm_billtype_setttype |  | fid |
| 2 | pk_t_cdm_billtype_setttype |  | fpkid |

---

## 票据类型-多语言表 t_cdm_billtype_l

- **表名称：** 票据类型-多语言表
- **表名：** t_cdm_billtype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fcomment | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_fbid_fid |  | fid,flocaleid |
| 2 | t_cdm_billtype_l_pkey |  | fpkid |

---

## 票据类型-主表 t_cdm_billtype

- **表名称：** 票据类型-主表
- **表名：** t_cdm_billtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fcomment | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fvaliditytime | 默认有效期 | int4 | 32 |  | √ | 0 | 默认有效期 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmaxamount | 最大开票金额 | numeric | 19 | 6 | √ | 0.000000 | 最大开票金额 |
| 8 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 9 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 10 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbillmedium | 票据介质 | varchar | 80 |  | √ | ' ' | 票据介质,枚举: 1 :纸票 2 :电票 |
| 12 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcredittype | 授信类别 | int8 | 64 |  | √ | 0 | 授信类别 cfm_credittype |
| 15 | fsettlementtypebd | fsettlementtypebd | int8 | 64 |  | √ | 0 |  |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fsettlementtype | 类别 | varchar | 30 |  | √ | ' ' | 类别,枚举: 1 :支票 2 :本票 5 :商业承兑汇票 6 :银行承兑汇票 |
| 19 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 22 | funit | 单位 | varchar | 30 |  | √ | ' ' | 单位,枚举: 1 :月 2 :天 |
| 23 | fvaliditytimedec | 有效期内容 | varchar | 80 |  | √ | ' ' | 有效期内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cdm_billtype_pkey |  | fid |
| 2 | idx_cdm_pb_fnumber |  | fnumber |
