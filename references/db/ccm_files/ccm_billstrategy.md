# （废弃）单据策略-ccm_billstrategy

## 检查策略取值分录-子表 t_ccm_bs_checkentry

- **表名称：** 检查策略取值分录-子表
- **表名：** t_ccm_bs_checkentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcheckformula_tag | 公式（后台废弃） | text | 0 |  |  | null | 公式（后台废弃） |
| 3 | fnewcheckformula_tag | 公式（后台）_详情 | text | 0 |  |  | null | 公式（后台）_详情 |
| 4 | fcheckfilter_tag | 过滤条件（后台废弃） | text | 0 |  |  | null | 过滤条件（后台废弃） |
| 5 | fnewcheckfilter_tag | 过滤条件（后台）_详情 | text | 0 |  |  | null | 过滤条件（后台）_详情 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcheckformula | 取值公式 | varchar | 510 |  | √ | ' ' | 取值公式 |
| 8 | fnewcheckfilter | 过滤条件（后台） | varchar | 255 |  | √ | ' ' | 过滤条件（后台） |
| 9 | fcheckfilter | 过滤条件 | varchar | 510 |  | √ | ' ' | 过滤条件 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fcheckdesc | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 12 | fnewcheckformula | 公式（后台） | varchar | 255 |  | √ | ' ' | 公式（后台） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_bsc_fid |  | fid |
| 2 | t_ccm_bs_checkentry_pkey |  | fentryid |

---

## （废弃）单据策略-主表 t_ccm_billstrategy

- **表名称：** （废弃）单据策略-主表
- **表名：** t_ccm_billstrategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcalculatedate | 计算日期 | varchar | 80 |  | √ | ' ' | 计算日期,枚举: |
| 3 | fdatafilter | 逾期条件 | varchar | 510 |  | √ | ' ' | 逾期条件 |
| 4 | fcheckpluginexplain | 插件说明 | varchar | 255 |  | √ | ' ' | 插件说明 |
| 5 | fincreaseops | 信用返还操作 | varchar | 2000 |  | √ | ' ' | 信用返还操作,枚举: unsubmit :撤销 unaudit :反审核 receivingrec :收款 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fplugintype | 插件类型 | varchar | 10 |  | √ | ' ' | 插件类型,枚举: java :java ks :ks |
| 8 | fcheckops | 检查信用操作 | varchar | 2000 |  | √ | ' ' | 检查信用操作,枚举: submit :提交 audit :审核 cancelrec :取消收款 |
| 9 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fchecktypeid | 信用控制形式 | int8 | 64 |  | √ | 0 | [（废弃）信用控制形式 ccm_checktype](../ccm_files/ccm_checktype.md) |
| 13 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 14 | fentityid | 业务单据 | varchar | 80 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 15 | fassingentityid | 逾期单据 | varchar | 80 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 16 | fnewdatafilter | 过滤条件(后台) | varchar | 255 |  | √ | ' ' | 过滤条件(后台) |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 19 | frecalculateplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | freduceops | 信用占用操作 | varchar | 2000 |  | √ | ' ' | 信用占用操作,枚举: submit :提交 audit :审核 cancelrec :取消收款 |
| 22 | frecalculateplugintype | 插件类型 | varchar | 10 |  | √ | ' ' | 插件类型,枚举: java :java ks :ks |
| 23 | fcalculateamt | 计算金额 | varchar | 80 |  | √ | ' ' | 计算金额,枚举: |
| 24 | fdatafilter_tag | 过滤条件(后台废弃) | text | 0 |  |  | null | 过滤条件(后台废弃) |
| 25 | fforwardaction | 信用方向 | varchar | 80 |  | √ | ' ' | 信用方向,枚举: reduce :占用 increase :返还 |
| 26 | frecalpluginexplain | 插件说明 | varchar | 255 |  | √ | ' ' | 插件说明 |
| 27 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 28 | fenable | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 30 | fnewdatafilter_tag | 过滤条件(后台)_详情 | text | 0 |  |  | null | 过滤条件(后台)_详情 |
| 31 | fischeck | 是否检查信用 | bpchar | 1 |  | √ | '0' | 是否检查信用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ccm_billstrategy_pkey |  | fid |
| 2 | idx_ccm_billstrategy_number |  | fnumber |

---

## （废弃）单据策略-多语言表 t_ccm_billstrategy_l

- **表名称：** （废弃）单据策略-多语言表
- **表名：** t_ccm_billstrategy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ccm_billstrategy_l_pkey |  | fpkid |
| 2 | idx_ccm_bs_fid_flocale |  | fid,flocaleid |

---

## 重算策略取值分录-子表 t_ccm_bs_recalentry

- **表名称：** 重算策略取值分录-子表
- **表名：** t_ccm_bs_recalentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnewrecalfilter_tag | 过滤条件（后台）_详情 | text | 0 |  |  | null | 过滤条件（后台）_详情 |
| 3 | fnewrecalformula_tag | 取值公式（后台）_详情 | text | 0 |  |  | null | 取值公式（后台）_详情 |
| 4 | fnewrecalformula | 取值公式（后台） | varchar | 255 |  | √ | ' ' | 取值公式（后台） |
| 5 | frecalformula_tag | 取值公式（后台废弃） | text | 0 |  |  | null | 取值公式（后台废弃） |
| 6 | frecaldesc | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | frecalfilter | 过滤条件 | varchar | 510 |  | √ | ' ' | 过滤条件 |
| 8 | frecalfilter_tag | 过滤条件（后台废弃） | text | 0 |  |  | null | 过滤条件（后台废弃） |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fnewrecalfilter | 过滤条件（后台） | varchar | 255 |  | √ | ' ' | 过滤条件（后台） |
| 11 | frecalformula | 取值公式 | varchar | 510 |  | √ | ' ' | 取值公式 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_bsr_fid |  | fid |
| 2 | t_ccm_bs_recalentry_pkey |  | fentryid |
