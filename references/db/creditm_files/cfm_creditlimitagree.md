# 授信框架协议-cfm_creditlimitagree

## 授信框架协议-使用范围位图表 t_cfm_creditagree_m

- **表名称：** 授信框架协议-使用范围位图表
- **表名：** t_cfm_creditagree_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_creditagree_m |  | forgid |

---

## 授信框架协议-多语言表 t_cfm_creditagree_l

- **表名称：** 授信框架协议-多语言表
- **表名：** t_cfm_creditagree_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 80 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_creditagree_l |  | fpkid |
| 2 | idx_cfm_creditagree_l |  | fid,flocaleid |

---

## 授信类别-多选基础资料表 t_cfm_creditagree_type_c

- **表名称：** 授信类别-多选基础资料表
- **表名：** t_cfm_creditagree_type_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [授信类别 cfm_credittype](../creditm_files/cfm_credittype.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_creditagree_type_c |  | fpkid |
| 2 | idx_cfm_agree_type_c_fid |  | fentryid |

---

## 授信框架协议-使用范围表 t_cfm_creditagree_u

- **表名称：** 授信框架协议-使用范围表
- **表名：** t_cfm_creditagree_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_creditagree_u |  | fdataid,fuseorgid |
| 2 | idx_t_cfm_creditagree_u_uo |  | fuseorgid |

---

## 类别限额分录-子表 t_cfm_creditagree_type

- **表名称：** 类别限额分录-子表
- **表名：** t_cfm_creditagree_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fuseamount | 关联授信金额 | numeric | 19 | 6 | √ | 0 | 关联授信金额 |
| 4 | famount | 限定额度 | numeric | 19 | 6 | √ | 0 | 限定额度 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_agree_type_fid |  | fid |
| 2 | pk_t_cfm_creditagree_type |  | fentryid |

---

## 成员组织分录-子表 t_cfm_creditagree_org

- **表名称：** 成员组织分录-子表
- **表名：** t_cfm_creditagree_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_creditagree_org |  | fentryid |
| 2 | idx_cfm_agree_org_fid |  | fid |
| 3 | idx_cfm_agree_org |  | forgid |

---

## 授信框架协议-主表 t_cfm_creditagree

- **表名称：** 授信框架协议-主表
- **表名：** t_cfm_creditagree

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 牵头组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fcreditprop | 授信性质 | varchar | 80 |  | √ | ' ' | 授信性质,枚举: circle :循环 fix :固定 |
| 4 | famount | 框架协议金额 | numeric | 19 | 6 | √ | 0 | 框架协议金额 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fenddate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 13 | fnmae | fnmae | varchar | 255 |  | √ | ' ' |  |
| 14 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fcomment | 限制性条款说明 | varchar | 255 |  | √ | ' ' | 限制性条款说明 |
| 17 | fcreatetime | 制单日期 | timestamp | 0 |  |  | null | 制单日期 |
| 18 | fcreditamount | 关联授信金额 | numeric | 19 | 6 | √ | 0 | 关联授信金额 |
| 19 | fcontractno | 框架协议号 | varchar | 80 |  | √ | ' ' | 框架协议号 |
| 20 | fctrlstrategy | 控制策略 | varchar | 80 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 21 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fcomment_tag | 限制性条款说明_详情 | text | 0 |  |  | null | 限制性条款说明_详情 |
| 24 | fnumber | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 25 | fbankid | 牵头授信机构 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 26 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 27 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_creditagree_number |  | fnumber,fstatus,forgid |
| 2 | pk_t_cfm_creditagree |  | fid |
| 3 | idx_t_cfm_creditagree_master |  | fmasterid |
| 4 | idx_t_cfm_creditagree_createorg |  | fcreateorgid |
