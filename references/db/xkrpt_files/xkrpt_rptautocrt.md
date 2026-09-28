# 报表自动生成方案-xkrpt_rptautocrt

## 报表范围分录-子表 t_xkrpt_rptautocrtentry

- **表名称：** 报表范围分录-子表
- **表名：** t_xkrpt_rptautocrtentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimensionfilter | 维度过滤 | varchar | 2000 |  | √ | ' ' | 维度过滤 |
| 3 | facctsystem | 核算体系 | int8 | 64 |  | √ | 0 | [核算体系 xkbd_accountingsys](../fibd_files/xkbd_accountingsys.md) |
| 4 | facctorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fpolicy | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 8 | fisfilldimension | 维度填充 | varchar | 1 |  | √ | ' ' | 维度填充,枚举: 1 :手工填充 2 :覆盖填充 3 :追加填充 |
| 9 | fsample | 报表模板 | varchar | 36 |  | √ | ' ' | [报表模板 xkrpt_rptsample](../xkrpt_files/xkrpt_rptsample.md) |
| 10 | frptadjust | 报表调整分录 | bpchar | 1 |  | √ | '0' | 报表调整分录 |
| 11 | fdimenfilterdetail_tag | 维度过滤值_详情 | text | 0 |  |  | null | 维度过滤值_详情 |
| 12 | fdimenfilterdetail | 维度过滤值 | varchar | 255 |  | √ | ' ' | 维度过滤值 |
| 13 | fiscompre | 综合本位币 | bpchar | 1 |  | √ | '1' | 综合本位币 |
| 14 | fcycleid | 周期 | varchar | 10 |  | √ | ' ' | 周期,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 15 | fscopetypeid | 合并方案 | int8 | 64 |  | √ | 0 | [合并方案 xkcr_scopetype](../xkcr_files/xkcr_scopetype.md) |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | facctbook | 取数账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 18 | funit | 金额单位 | int8 | 64 |  | √ | 0 | [金额单位 xkbd_amountunit](../fibd_files/xkbd_amountunit.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_rptautocrtentry |  | fentryid |
| 2 | idx_xkrpt_rptautocrtentry_fid |  | fid |

---

## 报表自动生成方案-多语言表 t_xkrpt_rptautocrt_l

- **表名称：** 报表自动生成方案-多语言表
- **表名：** t_xkrpt_rptautocrt_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_rptautocrt_l |  | fpkid |
| 2 | idx_xkrpt_rptautocrt_fid_l |  | fid,flocaleid |

---

## 报表自动生成方案-主表 t_xkrpt_rptautocrt

- **表名称：** 报表自动生成方案-主表
- **表名：** t_xkrpt_rptautocrt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fautolock | 执行锁 | bpchar | 1 |  | √ | '0' | 执行锁 |
| 4 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fispreperiod | 生成上期报表 | bpchar | 1 |  | √ | '1' | 生成上期报表 |
| 9 | fisupdaterpt | 生成覆盖已有报表 | bpchar | 1 |  | √ | '1' | 生成覆盖已有报表 |
| 10 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fprocesscount | 第 | int8 | 64 |  | √ | 0 | 第 |
| 12 | flastexetime | 最后生成执行时间 | timestamp | 0 |  |  | null | 最后生成执行时间 |
| 13 | ffrequency | 执行时间为 | bpchar | 1 |  | √ | '2' | 执行时间为,枚举: 1 :每日 2 :每期 3 :每月 4 :不执行 |
| 14 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fischeckaudit | 报表自动检查和审核 | bpchar | 1 |  | √ | '0' | 报表自动检查和审核 |
| 18 | fexeperiods | 执行期间 | varchar | 200 |  | √ | ' ' | 执行期间,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 11 :11 12 :12 |
| 19 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fdateforperiod | 天 | int4 | 32 |  | √ | 0 | 天 |
| 22 | fcycletype | 周期类型 | bpchar | 1 |  | √ | ' ' | 周期类型,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 25 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 26 | frpttype | 报表类型 | varchar | 2 |  | √ | ' ' | 报表类型,枚举: 1 :报表 16 :工作底稿 15 :合并报表 |
| 27 | fexetype | 执行条件 | bpchar | 1 |  | √ | ' ' | 执行条件,枚举: 1 :全部期间 2 :指定期间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_rptautocrt_num |  | fnumber |
| 2 | pk_xkrpt_rptautocrt |  | fid |
