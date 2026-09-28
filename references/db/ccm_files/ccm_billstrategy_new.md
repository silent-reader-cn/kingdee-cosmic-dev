# 信用单据策略-ccm_billstrategy_new

## 信用单据策略-主表 t_ccm_billstrategy_new

- **表名称：** 信用单据策略-主表
- **表名：** t_ccm_billstrategy_new

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcalculatedate | 计算日期 | varchar | 80 |  | √ | ' ' | 计算日期,枚举: |
| 3 | funcloseops | 信用反关闭操作 | varchar | 2000 |  | √ | ' ' | 信用反关闭操作,枚举: submit :提交 audit :审核 cancelrec :取消收款 |
| 4 | fdatafilter | 逾期条件 | varchar | 510 |  | √ | ' ' | 逾期条件 |
| 5 | fcloseops | 信用关闭操作 | varchar | 2000 |  | √ | ' ' | 信用关闭操作,枚举: submit :提交 audit :审核 cancelrec :取消收款 |
| 6 | fcheckpluginexplain | 插件说明 | varchar | 255 |  | √ | ' ' | 插件说明 |
| 7 | fincreaseops | 信用返还操作 | varchar | 2000 |  | √ | ' ' | 信用返还操作,枚举: unsubmit :撤销 unaudit :反审核 receivingrec :收款 |
| 8 | fishisupgrade | 是否历史数据升级 | bpchar | 1 |  | √ | ' ' | 是否历史数据升级 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fplugintype | 插件类型 | varchar | 10 |  | √ | ' ' | 插件类型,枚举: java :java ks :ks |
| 11 | fcheckops | 信用检查操作 | varchar | 2000 |  | √ | ' ' | 信用检查操作,枚举: submit :提交 audit :审核 cancelrec :取消收款 |
| 12 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | frecalclosefilter | 重算关闭条件 | varchar | 510 |  | √ | ' ' | 重算关闭条件 |
| 16 | fchecktypeid | 信用控制形式 | int8 | 64 |  | √ | 0 | [（废弃）信用控制形式 ccm_checktype](../ccm_files/ccm_checktype.md) |
| 17 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 18 | fentityid | 业务单据 | varchar | 80 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 19 | fassingentityid | 逾期单据 | varchar | 80 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 20 | fnewrecalbillfilter_tag | 重算占用条件（后台）_详情 | text | 0 |  |  | null | 重算占用条件（后台）_详情 |
| 21 | fnewdatafilter | 过滤条件(后台) | varchar | 255 |  | √ | ' ' | 过滤条件(后台) |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fname | 名称 | varchar | 130 |  | √ | ' ' | 名称 |
| 24 | frecalculateplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fnewrecalbillfilter | 重算占用条件（后台） | varchar | 255 |  | √ | ' ' | 重算占用条件（后台） |
| 27 | freduceops | 信用占用操作 | varchar | 2000 |  | √ | ' ' | 信用占用操作,枚举: submit :提交 audit :审核 cancelrec :取消收款 |
| 28 | frecalculateplugintype | 插件类型 | varchar | 10 |  | √ | ' ' | 插件类型,枚举: java :java ks :ks |
| 29 | fcalculateamt | 计算金额 | varchar | 80 |  | √ | ' ' | 计算金额,枚举: |
| 30 | fdatafilter_tag | 过滤条件(后台废弃) | text | 0 |  |  | null | 过滤条件(后台废弃) |
| 31 | fforwardaction | 信用方向 | varchar | 80 |  | √ | ' ' | 信用方向,枚举: reduce :占用 increase :返还 |
| 32 | frecalpluginexplain | 插件说明 | varchar | 255 |  | √ | ' ' | 插件说明 |
| 33 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 34 | frecalbillfilter | 重算条件 | varchar | 510 |  | √ | ' ' | 重算条件 |
| 35 | fnewrecalclosefilter_tag | 重算关闭条件（后台）_详情 | text | 0 |  |  | null | 重算关闭条件（后台）_详情 |
| 36 | fenable | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 37 | fnewrecalclosefilter | 重算关闭条件（后台） | varchar | 255 |  | √ | ' ' | 重算关闭条件（后台） |
| 38 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 39 | fnewdatafilter_tag | 过滤条件(后台)_详情 | text | 0 |  |  | null | 过滤条件(后台)_详情 |
| 40 | fischeck | 是否检查信用 | bpchar | 1 |  | √ | '0' | 是否检查信用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_billstrategy_number_n |  | fnumber |
| 2 | pk_t_ccm_billstrategy_new |  | fid |

---

## 信控取值配置-子表 t_ccm_bs_checkentry_new

- **表名称：** 信控取值配置-子表
- **表名：** t_ccm_bs_checkentry_new

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcheckformula_tag | fcheckformula_tag | text | 0 |  |  | null |  |
| 3 | fnewcheckformula_tag | 额度公式（后台）_详情 | text | 0 |  |  | null | 额度公式（后台）_详情 |
| 4 | fcheckfilter_tag | fcheckfilter_tag | text | 0 |  |  | null |  |
| 5 | fnewcheckfilter_tag | 过滤条件（后台）_详情 | text | 0 |  |  | null | 过滤条件（后台）_详情 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcheckformula | 信用额度取值公式 | varchar | 510 |  | √ | ' ' | 信用额度取值公式 |
| 8 | fnewcheckfilter | 过滤条件（后台） | varchar | 255 |  | √ | ' ' | 过滤条件（后台） |
| 9 | fcheckfilter | 业务单据过滤条件 | varchar | 510 |  | √ | ' ' | 业务单据过滤条件 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fcheckdesc | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 12 | fnewcheckformula | 额度公式（后台） | varchar | 255 |  | √ | ' ' | 额度公式（后台） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ccm_bs_checkentry_new |  | fentryid |
| 2 | idx_ccm_bsc_fid_n |  | fid |

---

## 信用单据策略-多语言表 t_ccm_billstrategy_new_l

- **表名称：** 信用单据策略-多语言表
- **表名：** t_ccm_billstrategy_new_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 130 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_bs_fid_flocale_n |  | fid,flocaleid |
| 2 | pk_t_ccm_billstrategy_new_l |  | fpkid |

---

## 重算策略取值分录-子表 t_ccm_bs_recalentry_new

- **表名称：** 重算策略取值分录-子表
- **表名：** t_ccm_bs_recalentry_new

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
| 1 | pk_t_ccm_bs_recalentry_new |  | fentryid |
| 2 | idx_ccm_bsr_fid_n |  | fid |
