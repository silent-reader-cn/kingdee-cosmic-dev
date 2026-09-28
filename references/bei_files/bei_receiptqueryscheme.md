# 电子回单联查方案-bei_receiptqueryscheme

## 电子回单联查方案-多语言表 t_bei_receiptqueryscheme_l

- **表名称：** 电子回单联查方案-多语言表
- **表名：** t_bei_receiptqueryscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_receiptqueryscheme_l |  | flocaleid,fname |
| 2 | pk_t_bei_receiptqueryscheme_l |  | fpkid |

---

## 查询链路单据体-子表 t_bei_receiptscheme_e

- **表名称：** 查询链路单据体-子表
- **表名：** t_bei_receiptscheme_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcequeryfield |  | varchar | 30 |  | √ | ' ' |  |
| 3 | fqueryrule |  | varchar | 30 |  | √ | ' ' |  |
| 4 | fsourcebillapp | 源单应用 | varchar | 255 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 5 | flinkname | 查询链路名称 | varchar | 50 |  | √ | ' ' | 查询链路名称 |
| 6 | ftargetbillname | 目标单名称 | varchar | 255 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fsourcebillname | 源单名称 | varchar | 255 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 10 | ftargetqueryfield |  | varchar | 30 |  | √ | ' ' |  |
| 11 | ftargetbillapp | 目标单应用 | varchar | 255 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bei_receiptscheme_e |  | fentryid |
| 2 | idx_bei_receiptscheme_e |  | fsourcebillname,ftargetbillapp,fqueryrule |

---

## 电子回单联查方案-主表 t_bei_receiptqueryscheme

- **表名称：** 电子回单联查方案-主表
- **表名：** t_bei_receiptqueryscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 4 | fistofundbill | 关联资金收付单据 | bpchar | 1 |  | √ | '0' | 关联资金收付单据 |
| 5 | fsourcebilltype | 源单类型 | varchar | 255 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 6 | fbizapp | 业务应用 | varchar | 255 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 7 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 10 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 11 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fqueryfilter | 查询条件 | varchar | 50 |  | √ | ' ' | 查询条件 |
| 17 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 方案编码 | varchar | 50 |  | √ | ' ' | 方案编码 |
| 20 | ffiltercondition | 过滤条件 | varchar | 500 |  | √ | ' ' | 过滤条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bei_receiptqueryscheme |  | fid |
| 2 | idx_bei_receiptqueryscheme |  | fsourcebilltype,fnumber |
