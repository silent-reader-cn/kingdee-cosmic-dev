# 外部计息对象-ifm_extintobject

## 外部计息对象-多语言表 t_ifm_intobject_l

- **表名称：** 外部计息对象-多语言表
- **表名：** t_ifm_intobject_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 内部账户名称 | varchar | 80 |  | √ | ' ' | 内部账户名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ifm_intobject_l |  | fpkid |
| 2 | idx_ifm_obj_l_id |  | fid,flocaleid |

---

## 单据体-子表 t_ifm_intobject_entry

- **表名称：** 单据体-子表
- **表名：** t_ifm_intobject_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdetail | 明细 | varchar | 255 |  | √ | ' ' | 明细 |
| 3 | fselect |  | bpchar | 1 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | 明细ID | int8 | 64 |  | √ | 0 | 明细ID |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fasstactitemid | 核算项目类型 | int8 | 64 |  | √ | 0 | 核算维度 bd_asstacttype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_intobject_entry_fid |  | fid |
| 2 | pk_ifm_intobject_entry |  | fentryid |

---

## 外部计息对象-主表 t_ifm_intobject

- **表名称：** 外部计息对象-主表
- **表名：** t_ifm_intobject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fintfreeamt | 存款免息额 | numeric | 23 | 10 | √ | 0 | 存款免息额 |
| 3 | finterestratedays | finterestratedays | varchar | 30 |  | √ | '360 ' |  |
| 4 | finteresttype | 利率生效方式 | varchar | 30 |  | √ | ' ' | 利率生效方式,枚举: subsection :分段利率 enabledate :启用日前利率 thisdrawdate :计息开始日利率 |
| 5 | freferrateid | 存款利率 | int8 | 64 |  | √ | 0 | 利率 ifm_product |
| 6 | forgid | 内部账户申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fiscaloverint | 计算透支利息 | bpchar | 1 |  | √ | '0' | 计算透支利息 |
| 8 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 9 | fstartintdate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 10 | fbosorg | 结算中心组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | finneracctid | finneracctid | int8 | 64 |  | √ | 0 |  |
| 12 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fbiztype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: Internal :内部计息对象 external :外部计息对象 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | frelateitem | 关联核算项目 | bpchar | 1 |  | √ | ' ' | 关联核算项目 |
| 18 | foverpoints | foverpoints | int8 | 64 |  | √ | 0 |  |
| 19 | finitaccum | 初始积数 | numeric | 23 | 10 | √ | 0 | 初始积数 |
| 20 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | foverpoint | 透支利率（BP） | numeric | 23 | 10 | √ | 0 | 透支利率（BP） |
| 22 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fname | 内部账户名称 | varchar | 80 |  | √ | ' ' | 内部账户名称 |
| 24 | fintinneracctid | 利息计入账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 25 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 28 | fintobjectid | 内部账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 29 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fintsettleschemeid | 结息方案 | int8 | 64 |  | √ | 0 | 结息方案 cfm_inscheme |
| 31 | foversign | 透支利率浮动基点（BP） | varchar | 30 |  | √ | ' ' | 透支利率浮动基点（BP）,枚举: add :上浮 subtract :下浮 |
| 32 | fsettlecenterid | 结算中心 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 33 | flastintdate | 上次结息日 | timestamp | 0 |  |  | null | 上次结息日 |
| 34 | finterestway | 计息方式 | varchar | 30 |  | √ | ' ' | 计息方式,枚举: standard :标准 progression :累进 |
| 35 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 36 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: bd_accountbanks :内部账户 |
| 37 | faccountorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 39 | fintobjectaccount | 内部账户账号 | varchar | 80 |  | √ | ' ' | 内部账户账号 |
| 40 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 41 | fintthreshold | 计息起点 | int8 | 64 |  | √ | 0 | 计息起点 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_intobject_finneracctid |  | finneracctid |
| 2 | pk_t_ifm_intobject |  | fid |

---

## 关联子实体-子表 t_ifm_intobject_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ifm_intobject_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ifm_intobject_lk |  | fpkid |
| 2 | idx_ifm_intobject_lk_fk |  | fid |

---

## 存款利率配置-子表 t_ifm_intobject_depint_e

- **表名称：** 存款利率配置-子表
- **表名：** t_ifm_intobject_depint_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdepositamtbegin | 起始值 | numeric | 23 | 10 | √ | 0 | 起始值 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdepositamtend | 结束值 | numeric | 23 | 10 | √ | 0 | 结束值 |
| 5 | fintfloatway |  | varchar | 50 |  | √ | ' ' | ,枚举: add :上浮 subtract :下浮 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fintfloatpoint | 利率浮动基点（BP） | numeric | 23 | 10 | √ | 0 | 利率浮动基点（BP） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_intobject_depint_e_fid |  | fid |
| 2 | pk_t_ifm_intobject_depint_e |  | fentryid |

---

## 透支利率配置-子表 t_ifm_intobject_overint_e

- **表名称：** 透支利率配置-子表
- **表名：** t_ifm_intobject_overint_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdepositend | 结束值 | numeric | 23 | 10 | √ | 0 | 结束值 |
| 3 | foverintfloatpoint | 透支利率浮动基点（BP） | numeric | 23 | 10 | √ | 0 | 透支利率浮动基点（BP） |
| 4 | foverfloatway |  | varchar | 50 |  | √ | ' ' | ,枚举: add :上浮 subtract :下浮 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fdepositbegin | 起始值 | numeric | 23 | 10 | √ | 0 | 起始值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_intobj_overint_e_fid |  | fid |
| 2 | pk_t_ifm_intobject_overint_e |  | fentryid |
