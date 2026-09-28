# 报表自动生成方案-xkrpt_rptautocrt

## 报表范围分录-子表 t_xkrpt_rptautocrtentry

- **表名称：** 报表范围分录-子表
- **表名：** t_xkrpt_rptautocrtentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimensionfilter | 维度过滤 | varchar | 2000 |  | √ | ' ' | 维度过滤 |
| 3 | facctsystem | 核算体系 | int8 | 64 |  | √ | 0 | 核算体系 xkbd_accountingsys |
| 4 | facctorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fpolicy | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 xkbd_policy |
| 8 | fisfilldimension | 维度填充 | varchar | 1 |  | √ | ' ' | 维度填充,枚举: 1 :手工填充 2 :覆盖填充 3 :追加填充 |
| 9 | fsample | 报表模板 | varchar | 36 |  | √ | ' ' | 报表模板 xkrpt_rptsample |
| 10 | fdimenfilterdetail_tag | 维度过滤值_详情 | text | 0 |  |  | null | 维度过滤值_详情 |
| 11 | fdimenfilterdetail | 维度过滤值 | varchar | 255 |  | √ | ' ' | 维度过滤值 |
| 12 | fiscompre | 综合本位币 | bpchar | 1 |  | √ | '1' | 综合本位币 |
| 13 | fcycleid | 周期 | varchar | 10 |  | √ | ' ' | 周期,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 14 | fscopetypeid | 合并方案 | int8 | 64 |  | √ | 0 | 合并方案 xkcr_scopetype |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | facctbook | 取数账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 17 | funit | 金额单位 | int8 | 64 |  | √ | 0 | 金额单位 xkbd_amountunit |

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
| 2 | ffrequency | 执行时间为 | bpchar | 1 |  | √ | '2' | 执行时间为,枚举: 1 :每日 2 :每期 3 :每月 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fischeckaudit | 报表自动检查和审核 | bpchar | 1 |  | √ | '0' | 报表自动检查和审核 |
| 7 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fautolock | 执行锁 | bpchar | 1 |  | √ | '0' | 执行锁 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fdateforperiod | 天 | int4 | 32 |  | √ | 0 | 天 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fispreperiod | 生成上期报表 | bpchar | 1 |  | √ | '1' | 生成上期报表 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fisupdaterpt | 生成覆盖已有报表 | bpchar | 1 |  | √ | '1' | 生成覆盖已有报表 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 21 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fprocesscount | 第 | int8 | 64 |  | √ | 0 | 第 |
| 23 | flastexetime | 最后生成执行时间 | timestamp | 0 |  |  | null | 最后生成执行时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_rptautocrt_num |  | fnumber |
| 2 | pk_xkrpt_rptautocrt |  | fid |
