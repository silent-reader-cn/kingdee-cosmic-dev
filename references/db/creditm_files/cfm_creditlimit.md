# 授信合同-cfm_creditlimit

## 授信类别-多选基础资料表 t_cfm_creditlimit_mult_t

- **表名称：** 授信类别-多选基础资料表
- **表名：** t_cfm_creditlimit_mult_t

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
| 1 | pk_t_cfm_creditlimit_mult_t |  | fpkid |
| 2 | t_cfm_credit_mult_eid |  | fentryid |

---

## 源单ID列表-多选基础资料表 t_cfm_creditlimit_merge

- **表名称：** 源单ID列表-多选基础资料表
- **表名：** t_cfm_creditlimit_merge

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_creditlimit_merge_id |  | fid |
| 2 | t_cfm_creditlimit_merge_pkey |  | fpkid |

---

## 授信合同-多语言表 t_cfm_creditlimit_l

- **表名称：** 授信合同-多语言表
- **表名：** t_cfm_creditlimit_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fcomment | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 80 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_creditlimit_l_id |  | fid,flocaleid |
| 2 | t_cfm_creditlimit_l_pkey |  | fpkid |

---

## 混合共享分录-子表 t_cfm_creditlimit_mult

- **表名称：** 混合共享分录-子表
- **表名：** t_cfm_creditlimit_mult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | favaramt | 可用额度 | numeric | 23 | 10 | √ | 0 | 可用额度 |
| 3 | ftotalamt | 限定额度 | numeric | 23 | 10 | √ | 0 | 限定额度 |
| 4 | fuseamt | 已用额度 | numeric | 23 | 10 | √ | 0 | 已用额度 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpreamt | 预占额度 | numeric | 23 | 10 | √ | 0 | 预占额度 |
| 7 | forgin | 原分录 | bpchar | 1 |  | √ | '0' | 原分录 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tlimit_detail_mult_id |  | fid |
| 2 | pk_t_cfm_creditlimit_mult |  | fentryid |

---

## 类别共享分录-子表 t_cfm_creditlimit_type

- **表名称：** 类别共享分录-子表
- **表名：** t_cfm_creditlimit_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | favaramt | 可用额度 | numeric | 23 | 10 | √ | 0 | 可用额度 |
| 3 | ftotalamt | 分配额度 | numeric | 23 | 10 | √ | 0 | 分配额度 |
| 4 | fuseamt | 已用额度 | numeric | 23 | 10 | √ | 0 | 已用额度 |
| 5 | fsingleamt | 限定额度 | numeric | 23 | 10 | √ | 0 | 限定额度 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 8 | fpreamt | 预占额度 | numeric | 23 | 10 | √ | 0 | 预占额度 |
| 9 | forgin | 原分录 | bpchar | 1 |  | √ | '0' | 原分录 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tlimit_detail_type_id |  | fid |
| 2 | pk_t_cfm_creditlimit_type |  | fentryid |

---

## 授信合同-使用范围表 t_cfm_creditlimit_u

- **表名称：** 授信合同-使用范围表
- **表名：** t_cfm_creditlimit_u

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
| 1 | idx_t_cfm_creditlimit_u_uo |  | fuseorgid |
| 2 | pk_t_cfm_creditlimit_u |  | fdataid,fuseorgid |

---

## 授信合同-使用范围位图表 t_cfm_creditlimit_m

- **表名称：** 授信合同-使用范围位图表
- **表名：** t_cfm_creditlimit_m

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
| 1 | pk_t_cfm_creditlimit_m |  | forgid |

---

## 关联子实体-子表 t_cfm_creditlimit_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cfm_creditlimit_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_creditlimit_lk_pkey |  | fpkid |
| 2 | idx_cfm_creditlimit_lk_fk |  | fid |

---

## 资金组织-多选基础资料表 t_cfm_creditlimit_detai_c

- **表名称：** 资金组织-多选基础资料表
- **表名：** t_cfm_creditlimit_detai_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_creditlimit_detai_c_fid |  | fentryid |
| 2 | pk_t_cfm_creditlimit_detai_c |  | fpkid |

---

## 授信类别-多选基础资料表 t_cfm_creditlimit_detai_d

- **表名称：** 授信类别-多选基础资料表
- **表名：** t_cfm_creditlimit_detai_d

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
| 1 | pk_t_cfm_creditlimit_detai_d |  | fpkid |
| 2 | idx_tlimit_detai_d_fid |  | fentryid |

---

## 授信合同-主表 t_cfm_creditlimit

- **表名称：** 授信合同-主表
- **表名：** t_cfm_creditlimit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopenorgid | fopenorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fcredittypeid | 授信类别 | int8 | 64 |  | √ | 0 | [授信类别 cfm_credittype](../creditm_files/cfm_credittype.md) |
| 4 | forgid | 受信组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fenddate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 9 | fcreditlimitagreeid | 框架协议号 | int8 | 64 |  | √ | 0 | [授信框架协议 cfm_creditlimitagree](../creditm_files/cfm_creditlimitagree.md) |
| 10 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 11 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fuseamt | 已用额度 | numeric | 19 | 6 | √ | 0.000000 | 已用额度 |
| 13 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 14 | fguartype | 担保方式 | varchar | 80 |  | √ | ' ' | 担保方式,枚举: ensure :保证担保 mortgage :抵押担保 pledge :质押担保 credit :信用/无担保 other :其他 |
| 15 | fguaranteeorgid | 担保组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fismergesrc | 是否为续授信源单 | bpchar | 1 |  | √ | '0' | 是否为续授信源单 |
| 17 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 19 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 20 | fdisttype | 分配类型（废弃）） | varchar | 50 |  | √ | ' ' | 分配类型（废弃））,枚举: total :总额共享 share :金额分享 |
| 21 | fenable | 使用状态 | varchar | 50 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 23 | fbankid | 授信机构 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 24 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fcompanyid | fcompanyid | int8 | 64 |  | √ | 0 |  |
| 27 | fforexquoteid | 外汇报价 | int8 | 64 |  | √ | 0 | [外汇报价 md_forexquote_f7](../md_files/md_forexquote_f7.md) |
| 28 | fcreditprop | 授信性质 | varchar | 50 |  | √ | ' ' | 授信性质,枚举: circle :循环 fix :非循环 |
| 29 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 30 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 32 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 33 | fisgrouplimit | 集团授信 | bpchar | 1 |  | √ | '0' | 集团授信 |
| 34 | fcurravaamt | 当前可占用金额 | numeric | 19 | 6 | √ | 0.000000 | 当前可占用金额 |
| 35 | fbanktype | 授信机构类别 | varchar | 30 |  | √ | 'bd_finorginfo' | 授信机构类别,枚举: bd_finorginfo :机构授信 bos_org :内部授信 |
| 36 | favaramt | 可用额度 | numeric | 19 | 6 | √ | 0.000000 | 可用额度 |
| 37 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fisclose | 关闭 | bpchar | 1 |  | √ | '0' | 关闭 |
| 40 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 41 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 42 | fpreuseamt | 预占额度 | numeric | 23 | 10 | √ | 0 | 预占额度 |
| 43 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 44 | fcontractno | 授信协议号 | varchar | 255 |  | √ | ' ' | 授信协议号 |
| 45 | fismergenew | 是否为续授信新单 | bpchar | 1 |  | √ | '0' | 是否为续授信新单 |
| 46 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 47 | ftotalamt | 总授信额度 | numeric | 19 | 6 | √ | 0.000000 | 总授信额度 |
| 48 | fismergesrcclose | 续授信源单是否关闭 | bpchar | 1 |  | √ | '0' | 续授信源单是否关闭 |
| 49 | forgsharetype | 组织共享方式 | varchar | 30 |  | √ | 'appointshare' | 组织共享方式,枚举: downshare :向下共享 appointshare :指定共享 |
| 50 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_creditlimit_no |  | fnumber |
| 2 | idx_t_cfm_creditlimit_master |  | fmasterid |
| 3 | idx_cfm_creditlimit_agreeno |  | fcreditlimitagreeid |
| 4 | idx_cfm_creditlimit_org |  | forgid |
| 5 | idx_t_cfm_creditlimit_createorg |  | fcreateorgid |
| 6 | t_cfm_creditlimit_pkey |  | fid |

---

## 组织共享分录-子表 t_cfm_creditlimit_org

- **表名称：** 组织共享分录-子表
- **表名：** t_cfm_creditlimit_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | favaramt | 可用额度 | numeric | 23 | 10 | √ | 0 | 可用额度 |
| 3 | ftotalamt | 分配额度 | numeric | 23 | 10 | √ | 0 | 分配额度 |
| 4 | fuseamt | 已用额度 | numeric | 23 | 10 | √ | 0 | 已用额度 |
| 5 | fsingleamt | 限定额度 | numeric | 23 | 10 | √ | 0 | 限定额度 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 8 | fpreamt | 预占额度 | numeric | 23 | 10 | √ | 0 | 预占额度 |
| 9 | forgin | 原分录 | bpchar | 1 |  | √ | '0' | 原分录 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tlimit_detail_org_id |  | fid |
| 2 | pk_t_cfm_creditlimit_org |  | fentryid |

---

## 资金组织-多选基础资料表 t_cfm_creditlimit_mult_o

- **表名称：** 资金组织-多选基础资料表
- **表名：** t_cfm_creditlimit_mult_o

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_creditlimit_mult_o |  | fpkid |
| 2 | t_cfm_credit_mult_o_eid |  | fentryid |
