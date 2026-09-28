# 支付准入-fcs_payaccess

## 支付准入-主表 t_fcs_payaccess

- **表名称：** 支付准入-主表
- **表名：** t_fcs_payaccess

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 3 | fdestentityid | 目标单 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 4 | fispreset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 5 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 6 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fsrclkprop | 源单关联属性 | varchar | 50 |  | √ | ' ' | 源单关联属性,枚举: 1 :源单单头id 2 :源单分录id |
| 10 | fsrcentityid | 源单 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 11 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | ffilter | 数据过滤条件 | varchar | 255 |  | √ | ' ' | 数据过滤条件 |
| 13 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 14 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fiscustomentity | 自定义源单 | bpchar | 1 |  | √ | '0' | 自定义源单 |
| 16 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 19 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | ffilter_tag | 数据过滤条件_详情 | text | 0 |  |  | ' ' | 数据过滤条件_详情 |
| 21 | foperate | 注册操作 | varchar | 30 |  | √ | ' ' | 注册操作,枚举: save :保存 submit :提交 delete :删除 |
| 22 | fdestlkfield | 目标关联字段 | varchar | 50 |  | √ | ' ' | 目标关联字段 |
| 23 | fcustomsign | 自定义实体 | varchar | 255 |  | √ | ' ' | 自定义实体 |
| 24 | fisbotpadd | 源单通过BOTP生成目标单 | bpchar | 1 |  | √ | '0' | 源单通过BOTP生成目标单 |
| 25 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fdestlkpkfield | 目标单存储的源单唯一主键 | varchar | 50 |  | √ | ' ' | 目标单存储的源单唯一主键 |
| 27 | fnumber | 单据编码 | varchar | 80 |  | √ | ' ' | 单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fcs_payaccess_src |  | fsrcentityid,fenable |
| 2 | pk_t_fcs_payaccess |  | fid |
| 3 | idx_t_fcs_payaccess_dest |  | fisbotpadd,fenable,fdestentityid |

---

## 支付准入-多语言表 t_fcs_payaccess_l

- **表名称：** 支付准入-多语言表
- **表名：** t_fcs_payaccess_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fcs_payaccess_l |  | fid,flocaleid |
| 2 | pk_fcs_payaccess_l |  | fpkid |
